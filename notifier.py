import os
import requests
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def kirim_notifikasi_telegram(pesan):
    if not TOKEN or not CHAT_ID:
        return "[NOTIF] Token/chat ID tidak ditemukan"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": pesan}
    try:
        requests.post(url, data=data)
        return "[NOTIF] Pesan dikirim."
    except:
        return "[NOTIF] Gagal mengirim pesan."
