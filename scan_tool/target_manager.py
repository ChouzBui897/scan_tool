import ipaddress
import os

def parse_targets(target_str):
    """
    Chuyển đổi chuỗi mục tiêu (IP đơn, CIDR hoặc file) thành danh sách các địa chỉ IP.
    """
    targets = []
    
    # Kiểm tra nếu target_str là một đường dẫn file tồn tại
    if os.path.isfile(target_str):
        try:
            with open(target_str, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        targets.extend(parse_targets(line)) # Đệ quy để xử lý từng dòng
            return targets
        except Exception as e:
            print(f"[-] Lỗi khi đọc file mục tiêu: {e}")
            return []

    # Xử lý dải IP (CIDR) hoặc IP đơn
    try:
        if '/' in target_str:
            # Ví dụ: 192.168.1.0/24
            network = ipaddress.ip_network(target_str, strict=False)
            for ip in network.hosts():
                targets.append(str(ip))
        else:
            # Ví dụ: 192.168.1.1
            targets.append(str(ipaddress.ip_address(target_str)))
    except ValueError:
        print(f"[-] Mục tiêu không hợp lệ: {target_str}")
    
    return targets

def parse_ports(port_str):
    """
    Chuyển đổi chuỗi cổng (ví dụ: '80,443' hoặc '1-1024') thành danh sách số nguyên.
    """
    ports = []
    try:
        for part in port_str.split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                ports.extend(range(start, end + 1))
            else:
                ports.append(int(part))
    except ValueError:
        print(f"[-] Cổng không hợp lệ: {port_str}")
        
    return sorted(list(set(ports))) # Xóa trùng và sắp xếp