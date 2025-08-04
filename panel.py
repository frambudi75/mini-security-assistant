from flask import Flask, render_template, request, redirect, session
import os
from dotenv import load_dotenv
from run_scan import run_scan

load_dotenv()
app = Flask(__name__)
app.secret_key = 'supersecretkey'

USERNAME = os.getenv("PANEL_USER", "admin")
PASSWORD = os.getenv("PANEL_PASS", "admin")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["user"] = USERNAME
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")
    log_data = ""
    scan_result = None
    if request.method == "POST" and request.form.get("action") == "scan":
        scan_result = run_scan()
    try:
        with open("logs/assistant.log", "r") as f:
            log_data = f.read()
    except:
        log_data = "Log file not found."
    return render_template("index.html", logs=log_data, result=scan_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5025)
