import psutil

def get_free_port(start=5000, end=5100):
    used_ports = {conn.laddr.port for conn in psutil.net_connections() if conn.status == psutil.CONN_LISTEN}
    for port in range(start, end):
        if port not in used_ports:
            return port
    raise RuntimeError("No free port found.")
