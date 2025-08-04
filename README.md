# 🛡️ Security Assistant v2.2

**Security Assistant v2.2** adalah alat bantu keamanan otomatis untuk server Ubuntu/Debian, dilengkapi dengan web panel dan dukungan Telegram. Sistem ini dapat memindai file mencurigakan, membersihkan folder sementara, mendeteksi brute-force, dan mengirim notifikasi ke Telegram secara otomatis maupun manual.

---

## ✨ Fitur Utama

- 🔍 Scan file mencurigakan (.php, .sh, .exe, dll)
- 🧹 Bersihkan file sampah di `/tmp` (berumur > 24 jam)
- 🔐 Deteksi brute-force SSH dan blok IP-nya
- 📬 Kirim notifikasi ke Telegram otomatis
- 🖥️ Panel web login (port 5025) untuk:
  - Melihat log
  - Menjalankan scan manual dengan 1 klik
- 🔁 Support cronjob untuk scan otomatis berkala

---

## 📦 Struktur Folder

```
security_assistant_v2.2/
├── run_scan.py              # Fungsi utama untuk scan
├── panel.py                 # Web panel port 5025
├── scanner.py               # Scan file mencurigakan
├── cleaner.py               # Hapus file lama dari /tmp
├── firewall.py              # Deteksi brute-force dan blokir
├── notifier.py              # Kirim alert ke Telegram
├── templates/
│   ├── login.html           # Halaman login panel
│   └── index.html           # Dashboard + tombol scan
├── logs/                    # Log file (assistant.log)
├── reports/                 # Tempat hasil scan (opsional)
├── .env.example             # Contoh konfigurasi login & Telegram
├── requirements.txt         # Dependency pip
└── README.md
```

---

## 🚀 Cara Instalasi

1. **Clone atau download repo ini**
2. **Install Python dan pip (Python 3.7+)**
3. **Install dependency**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Copy konfigurasi .env**:
   ```bash
   cp .env.example .env
   ```
   Edit dan isi:
   ```
   TELEGRAM_TOKEN=isi_token_bot_kamu
   TELEGRAM_CHAT_ID=isi_chat_id_kamu
   PANEL_USER=admin
   PANEL_PASS=rahasia123
   ```

5. **Jalankan web panel**:
   ```bash
   python3 panel.py
   ```
   Akses di browser: `http://<ip-server>:5025`

---

## 🔁 Cronjob Otomatis

Jika ingin scan otomatis tanpa buka web:

```bash
crontab -e
```

Tambahkan:

```
*/30 * * * * /usr/bin/python3 /path/to/run_scan.py
```

> Ganti `/path/to/` dengan direktori sebenarnya

---

## 📡 Coming Soon (v2.3)

- 🤖 Telegram Bot Commands:
  - `/scan` → Scan manual via Telegram
  - `/log` → Kirim log ke Telegram
  - `/status` → Status keamanan terkini

---

## 📄 Lisensi

Open-source & gratis digunakan untuk keperluan pribadi atau perusahaan. Dilarang menjual ulang tanpa izin.

---

## 🤝 Kontribusi

Kritik, saran, dan pull request sangat diterima! Silakan fork atau hubungi saya langsung.

