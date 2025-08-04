import os

SUSPICIOUS_EXTENSIONS = ['.php', '.sh', '.py', '.exe', '.js']

def scan_directory(path):
    found = []
    for root, _, files in os.walk(path):
        for file in files:
            if any(file.endswith(ext) for ext in SUSPICIOUS_EXTENSIONS):
                full_path = os.path.join(root, file)
                if os.path.getsize(full_path) > 0:
                    found.append(full_path)
    return found
