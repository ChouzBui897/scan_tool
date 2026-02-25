import socket

def grab_banner(ip, port, timeout=2.0):
    """
    Thực hiện Banner Grabbing trên một cổng đã biết là MỞ.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))
        
        banner = sock.recv(1024)
        
        if not banner and (port == 80 or port == 8080 or port == 443):
            sock.send(b"HEAD / HTTP/1.0\r\nHost: " + ip.encode() + b"\r\n\r\n")
            banner = sock.recv(1024)

        sock.close()
        
        return banner.decode('utf-8', errors='ignore').strip()
        
    except Exception as e:
        return "Unknown"
    finally:
        if 'sock' in locals() and sock:
            sock.close()