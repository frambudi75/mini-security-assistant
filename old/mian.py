from scanner import scan_directory
from cleaner import clean_tmp_folder
from firewall import detect_brute_force, block_ip
from notifier import send_alert

def main():
    suspicious = scan_directory("/var/www")
    if suspicious:
        send_alert("🚨 Suspicious files detected:\n" + "\n".join(suspicious))

    cleaned = clean_tmp_folder()
    if cleaned:
        send_alert(f"🧹 Deleted {len(cleaned)} old files in /tmp")

    attackers = detect_brute_force()
    for ip in attackers:
        block_ip(ip)
        send_alert(f"🔐 Blocked brute-force IP: {ip}")

if __name__ == "__main__":
    main()
