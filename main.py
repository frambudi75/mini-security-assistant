from scanner import scan_file_mencurigakan
from cleaner import hapus_file_tmp
from firewall import deteksi_bruteforce_ssh
from logger import cek_log_sistem
from notifier import kirim_notifikasi_telegram

def run_scan():
    hasil = []
    hasil.append(scan_file_mencurigakan())
    hasil.append(hapus_file_tmp())
    hasil.append(deteksi_bruteforce_ssh())
    hasil.append(cek_log_sistem())

    laporan = "\n".join(hasil)
    kirim_notifikasi_telegram(laporan)

if __name__ == "__main__":
    run_scan()
