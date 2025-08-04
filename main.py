from scanner import scan_file_mencurigakan
from cleaner import hapus_file_tmp
from firewall import deteksi_bruteforce_ssh
from logger import cek_log_sistem
from notifier import kirim_notifikasi_telegram
from datetime import datetime
import os

def run_scan():
    hasil = []
    hasil.append(scan_file_mencurigakan())
    hasil.append(hapus_file_tmp())
    hasil.append(deteksi_bruteforce_ssh())
    hasil.append(cek_log_sistem())

    laporan = "\n".join(hasil)
    kirim_notifikasi_telegram(laporan)
    simpan_ke_report(laporan)

def simpan_ke_report(isi):
    now = datetime.now().strftime("%Y-%m-%d")
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/log-{now}.txt", "a") as f:
        f.write(isi + "\n\n")

def get_status_ringkas():
    import shutil
    total, used, free = shutil.disk_usage("/")
    persentase = (used / total) * 100
    status = f"💾 Disk Usage: {persentase:.1f}%\n"
    status += scan_file_mencurigakan() + "\n"
    status += deteksi_bruteforce_ssh()
    return status

if __name__ == "__main__":
    run_scan()
