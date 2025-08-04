def cek_log_sistem():
    try:
        with open("/var/log/syslog", "r") as f:
            lines = f.readlines()[-10:]
        return "[LOG] 10 baris terakhir:\n" + "".join(lines)
    except:
        return "[LOG] Tidak bisa baca /var/log/syslog"

def reset_log_aplikasi(path="/var/www/html/logs/app.log"):
    try:
        open(path, "w").close()
        return "[LOG] Log aplikasi direset."
    except:
        return "[LOG] Gagal reset log aplikasi."
