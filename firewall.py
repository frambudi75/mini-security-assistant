import subprocess

def deteksi_bruteforce_ssh():
    try:
        hasil = subprocess.getoutput("grep 'Failed password' /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head")
        return f"[FIREWALL] IP mencurigakan:\n{hasil}"
    except Exception as e:
        return f"[FIREWALL] Gagal analisa SSH: {e}"
