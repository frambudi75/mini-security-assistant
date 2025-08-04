from flask import Flask, render_template, request, redirect, session, abort
from main import run_scan, get_status_ringkas
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)

USER = os.getenv("PANEL_USER")
PASS = os.getenv("PANEL_PASS")
LOGIN_ATTEMPT = {}
BLOCKED_IP = {}

@app.route("/", methods=["GET", "POST"])
def login():
    ip = request.remote_addr
    if BLOCKED_IP.get(ip) and datetime.now() < BLOCKED_IP[ip]:
        return "Terlalu banyak percobaan. Coba lagi nanti."

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == USER and password == PASS:
            session["logged_in"] = True
            LOGIN_ATTEMPT[ip] = 0
            return redirect("/dashboard")
        else:
            LOGIN_ATTEMPT[ip] = LOGIN_ATTEMPT.get(ip, 0) + 1
            if LOGIN_ATTEMPT[ip] >= 3:
                BLOCKED_IP[ip] = datetime.now().replace(microsecond=0) + timedelta(minutes=5)
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/")
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    if not session.get("logged_in"):
        return redirect("/")
    run_scan()
    return redirect("/dashboard")

# Telegram Bot
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def scan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    run_scan()
    await update.message.reply_text("✅ Scan selesai dan laporan dikirim.")

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hasil = get_status_ringkas()
    await update.message.reply_text(f"📊 Status Ringkas:\n{hasil}")

async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open("logs/assistant.log", "r") as f:
            lines = f.readlines()[-20:]
        await update.message.reply_text("📝 Log Terakhir:\n" + "".join(lines))
    except:
        await update.message.reply_text("❌ Gagal membaca log.")

if TOKEN:
    from telegram.ext import ApplicationBuilder
    from threading import Thread
    from datetime import timedelta

    def start_bot():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        app_bot = ApplicationBuilder().token(TOKEN).build()
        app_bot.add_handler(CommandHandler("scan", scan_command))
        app_bot.add_handler(CommandHandler("status", status_command))
        app_bot.add_handler(CommandHandler("log", log_command))
        loop.run_until_complete(app_bot.initialize())
        loop.run_until_complete(app_bot.start())
        loop.run_until_complete(app_bot.updater.start_polling())
        loop.run_forever()

    Thread(target=start_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5025)
