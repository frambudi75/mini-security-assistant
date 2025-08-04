import os, time

def hapus_file_tmp(path='/tmp'):
    hitung = 0
    now = time.time()
    for root, dirs, files in os.walk(path):
        for f in files:
            file_path = os.path.join(root, f)
            try:
                if os.stat(file_path).st_mtime < now - 86400:
                    os.remove(file_path)
                    hitung += 1
            except:
                continue
    return f"[CLEAN] Dihapus {hitung} file dari {path}."
