import os
import time

def clean_tmp_folder(folder='/tmp', max_age_hours=24):
    now = time.time()
    max_age = max_age_hours * 3600
    deleted_files = []

    for root, _, files in os.walk(folder):
        for name in files:
            file_path = os.path.join(root, name)
            if os.path.isfile(file_path) and now - os.path.getmtime(file_path) > max_age:
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                except Exception:
                    pass
    return deleted_files
