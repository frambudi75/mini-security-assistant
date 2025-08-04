import subprocess
import re

def detect_brute_force(log_file='/var/log/auth.log', threshold=5):
    ip_count = {}
    try:
        with open(log_file) as f:
            for line in f:
                if "Failed password" in line:
                    ip_match = re.search(r"from (\\d+\\.\\d+\\.\\d+\\.\\d+)", line)
                    if ip_match:
                        ip = ip_match.group(1)
                        ip_count[ip] = ip_count.get(ip, 0) + 1
        return [ip for ip, count in ip_count.items() if count >= threshold]
    except FileNotFoundError:
        return []

def block_ip(ip):
    subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
