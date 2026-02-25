# Công cụ tự động hóa Port Scanning & Service Detection

[cite_start]Công cụ được phát triển trong khuôn khổ đề tài Nghiên cứu Khoa học Sinh viên năm học 2025-2026[cite: 4, 5].

## Tính năng
* [cite_start]Hỗ trợ quét TCP Connect (-sT) và TCP SYN (-sS)[cite: 468, 469, 470].
* [cite_start]Tự động nhận diện dịch vụ qua Banner Grabbing[cite: 471].
* [cite_start]Tối ưu hóa hiệu năng bằng cơ chế đa luồng (Multi-threading)[cite: 474, 492].
* [cite_start]Xuất kết quả ra định dạng JSON[cite: 472].

## Hướng dẫn sử dụng

### 1. Cài đặt môi trường
Kích hoạt môi trường ảo và cài đặt các thư viện cần thiết:
```bash
# Kích hoạt venv (Windows)
.\venv\Scripts\activate

# Cài đặt thư viện
pip install -r requirements.txt