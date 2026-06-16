# 1. Cấu trúc thư mục dự án (Folder Tree)
# Code
# rikkei_aviation/
# │
# ├── main.py                # Menu chính, chỉ điều hướng
# │
# ├── core/                  # Nghiệp vụ chính
# │   ├── logistics.py       # Hiển thị lịch trình & hậu cần
# │   └── manager.py         # Tiếp nhận chuyến bay mới
# │
# ├── utils/                 # Hàm phụ trợ
# │   ├── time_helper.py     # Tính ETA
# │   └── file_helper.py     # Tạo thư mục log
# │
# ├── data/                  # Dữ liệu ban đầu
# │   └── flights_data.py
# │
# └── docs/                  # README, tài liệu kiến trúc
# 👉 Ưu điểm: dễ bảo trì, dễ mở rộng, mỗi chức năng nằm riêng một module.

# 2. Vì sao không nên dùng from math import *
# Khi import *, tất cả hàm trong math sẽ vào namespace → dễ bị ghi đè tên.

# Ví dụ: nếu có biến ceil = 10, sau khi import thì ceil sẽ thành hàm math.ceil.

# Hậu quả: mất dữ liệu, khó debug, code thiếu rõ ràng.
# 👉 Giải pháp: chỉ import cái cần, ví dụ import math hoặc from math import ceil.

from core.logistics import show_flights
from core.manager import add_flight
from utils.time_helper import calculate_eta
from utils.file_helper import create_log_folder

flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
    {"flight_id": "RA002", "passengers": 85, "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
]

while True:
    print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
    print("1. Hiển thị lịch trình và Thống kê hậu cần")
    print("2. Tiếp nhận chuyến bay mới")
    print("3. Tính thời gian hạ cánh dự kiến (ETA)")
    print("4. Khởi tạo thư mục lưu trữ log hệ thống")
    print("5. Thoát chương trình")
    print("==================================================")

    try:
        choice = int(input("Nhập lựa chọn của bạn: "))

        if choice == 1:
            show_flights(flights)

        elif choice == 2:
            add_flight(flights)

        elif choice == 3:
            calculate_eta(flights)

        elif choice == 4:
            create_log_folder()

        elif choice == 5:
            print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
            break

        else:
            print("Vui lòng nhập từ 1 đến 5!")

    except ValueError:
        print("Lỗi nhập liệu! Vui lòng nhập số từ 1 đến 5!")