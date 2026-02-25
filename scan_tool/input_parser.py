import argparse
import sys

def parse_args():
    """
    Phân tích và trả về các đối số dòng lệnh.
    """
    parser = argparse.ArgumentParser(
        description="Công cụ quét cổng và phát hiện dịch vụ tự động hóa.",
        epilog="Ví dụ: sudo python main.py -t 192.168.1.1 -p 1-100 -sS"
    )

    parser.add_argument(
        "-t", "--target",
        dest="target",
        required=True,
        help="Mục tiêu quét (IP đơn, CIDR, hoặc file chứa IP)."
    )

    parser.add_argument(
        "-p", "--ports",
        dest="ports",
        default="1-1024",
        help="Cổng quét (ví dụ: '22,80,443' hoặc '1-1024'). Mặc định là 1-1024."
    )

    parser.add_argument(
        "--threads",
        dest="threads",
        type=int,
        default=50,
        help="Số luồng (threads) chạy đồng thời. Mặc định là 50."
    )

    parser.add_argument(
        "--timeout",
        dest="timeout",
        type=float,
        default=1.0,
        help="Thời gian chờ (giây) cho mỗi kết nối. Mặc định là 1.0 giây."
    )

    scan_group = parser.add_mutually_exclusive_group()
    scan_group.add_argument(
        "-sS", "--syn-scan",
        dest="scan_type",
        action="store_const",
        const="SYN",
        help="Thực hiện quét TCP SYN (yêu cầu quyền root)."
    )
    scan_group.add_argument(
        "-sT", "--connect-scan",
        dest="scan_type",
        action="store_const",
        const="CONNECT",
        help="Thực hiện quét TCP Connect (mặc định nếu không chọn)."
    )
    
    # Mặc định là Connect Scan nếu không chọn -sS hay -sT
    parser.set_defaults(scan_type="CONNECT")

    # Đối số cho file output
    parser.add_argument(
        "-oJ", "--output-json",
        dest="output_json",
        help="Tên file để lưu kết quả ra định dạng JSON."
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()

# Thêm đoạn này để kiểm tra nhanh
if __name__ == "__main__":
    args = parse_args()
    print("Các đối số đã phân tích:")
    print(args) 