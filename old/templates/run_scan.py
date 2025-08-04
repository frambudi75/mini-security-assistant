from scanner import scan_directory
from cleaner import clean_tmp_folder
from firewall import detect_brute_force, block_ip
from notifier import send_alert
from datetime import datetime

def run_scan():
    log = []
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log.append(f"[{timestamp}] 🔍 Manual scan started.")

    suspicious = scan_directory("/var/www")
    if suspicious:
        msg = f"🚨 Suspicious files found:\n" + "\n".join(suspicious)
        send_alert(msg)
        log.append(msg)
    else:
        log.append("✅ No suspicious files found.")

    cleaned = clean_tmp_folder()
    if cleaned:
        msg = f"🧹 Deleted {len(cleaned)} old files in /tmp"
        send_alert(msg)
        log.append(msg)
    else:
        log.append("🧹 No files deleted.")

    attackers = detect_brute_force()
    for ip in attackers:
        block_ip(ip)
        msg = f"🔐 Blocked brute-force IP: {ip}"
        send_alert(msg)
        log.append(msg)
    if not attackers:
        log.append("✅ No brute-force attempts detected.")

    with open("logs/assistant.log", "a") as f:
        f.write("\n".join(log) + "\n\n")
    
    return "\n".join(log)
