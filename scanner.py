import os

def scan_file_mencurigakan(direktori='/var/www'):
    mencurigakan = []
    ekstensi_berbahaya = ['.php', '.sh', '.exe', '.py']
    for root, dirs, files in os.walk(direktori):
        for f in files:
            if any(f.endswith(ext) for ext in ekstensi_berbahaya):
                mencurigakan.append(os.path.join(root, f))
    if mencurigakan:
        return f"[SCAN] Ditemukan {len(mencurigakan)} file mencurigakan."
    return "[SCAN] Tidak ada file mencurigakan."
