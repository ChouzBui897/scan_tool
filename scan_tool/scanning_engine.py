import socket
from scapy.all import IP, TCP, sr1, RandShort, send
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def connect_scan(ip, port, timeout):
    """
    Thực hiện TCP Connect Scan bằng thư viện socket.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            return "open"
        else:
            return "closed"
            
    except socket.timeout:
        return "filtered"
    except socket.error as e:
        return "error"
    finally:
        sock.close()

def syn_scan(ip, port, timeout):
    """
    Thực hiện TCP SYN Scan bằng thư viện Scapy.
    """
    try:
        syn_packet = IP(dst=ip) / TCP(sport=RandShort(), dport=port, flags="S")
        
        response = sr1(syn_packet, timeout=timeout, verbose=0)
        
        if response is None:
            return "filtered"
        
        if response.haslayer(TCP):
            flags = response.getlayer(TCP).flags
            
            if flags == 0x12:
                rst_packet = IP(dst=ip) / TCP(sport=syn_packet[TCP].sport, dport=port, flags="R")
                send(rst_packet, verbose=0)
                return "open"
            
            elif flags == 0x14:
                return "closed"
                
    except Exception as e:
        return "error"
        
    return "filtered"