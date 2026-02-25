import json

def print_console(results):
    """
    In kết quả quét đẹp mắt ra màn hình.
    """
    print("\n" + "="*50)
    print(f"{'IP Address':<15} | {'Port':<7} | {'Status':<10} | {'Service/Banner'}")
    print("-" * 50)
    
    for host, host_results in results.items():
        for p_res in host_results:
            banner = p_res.get('banner', 'N/A')
            print(f"{host:<15} | {p_res['port']:<7} | {p_res['status']:<10} | {banner}")
    print("="*50 + "\n")

def save_json(results, filename):
    """
    Lưu kết quả quét ra file định dạng JSON.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        print(f"[+] Kết quả đã được lưu tại: {filename}")
    except Exception as e:
        print(f"[-] Lỗi khi lưu file JSON: {e}")