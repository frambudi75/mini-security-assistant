                +-------------------------+
                |    Web Panel (panel.py) |
                |   Port 5025, Login .env |
                +-------------------------+
                 |        |           |
          tombol "Scan"   |           | /scan Telegram
                 |        v           v
               +-----------------------------+
               |  run_scan() dari main.py    |
               | - scan file                 |
               | - bersih /tmp               |
               | - deteksi brute-force       |
               | - update logs               |
               +-----------------------------+

               +-----------------------------+
               |  Cronjob tetap jalan biasa  |
               | (eksekusi langsung main.py) |
               +-----------------------------+
