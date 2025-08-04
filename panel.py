from flask import Flask, render_template, request, redirect, session
from main import run_scan
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)

USER = os.getenv("PANEL_USER")
PASS = os.getenv("PANEL_PASS")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USER and request.form["password"] == PASS:
            session["logged_in"] = True
            return redirect("/dashboard")
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
    await update.message.reply_text("Scan selesai dan laporan sudah dikirim.")

if TOKEN:
    import threading
    from telegram.ext import ApplicationBuilder
    def start_bot():
        app_bot = ApplicationBuilder().token(TOKEN).build()
        app_bot.add_handler(CommandHandler("scan", scan_command))
        app_bot.run_polling()
    threading.Thread(target=start_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5025)
