# 1. phân tích và cấu trúc thư mục
# câu 1:
# Tại sao việc lạm dụng from math import * lại được coi là một "Anti-pattern" (thực hành xấu) trong Python?
# Hãy đề xuất cách import an toàn và tường minh hơn.
# vì nó import tất cả các hàm nên dễ bị trùng tên
# khiến người đọc không biết hàm nằm ở thư viện nào
# giải pháp là dùng import math

# câu 2:
# Để biến một thư mục thông thường thành một Package
# trong Python, chúng ta cần tệp cấu hình đặc biệt nào?
# Vai trò của tệp đó là gì?

# cần tệp có cấu hình file __init__.py
# vai trò là đánh dấu thư mục là package và cho phép python chứa các module bên trong

# câu 3:
# Hãy vẽ sơ đồ cấu trúc cây thư mục (Folder Tree)
# sau khi bạn tối ưu hóa dự án thành các package utils,
# core,
# và tệp thực thi main.py.
# RikkeiLogistics/
# │── main.py
# │── core/
# │   ├── __init__.py
# │   ├── geo_calculator.py
# │   └── time_estimator.py
# │── utils/
# │   ├── __init__.py
# │   └── file_helper.py
# │── logs/   (tự động tạo khi chạy)
from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta

import datetime

shipments = [
    {"id": "TRK-001", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 10.8231, "to_lon": 106.6297,
     "depart": "2026-06-10 08:00:00", "deadline": "2026-06-11 12:00:00"},
    {"id": "TRK-002", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 16.0544, "to_lon": 108.2022,
     "depart": "2026-06-10 09:30:00", "deadline": "2026-06-10 15:00:00"},
]

print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

create_log_dir("logs")
print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")

print("---------------------------------------------------------------------------")

for s in shipments:
    distance = calculate_distance(
        s["from_lat"],
        s["from_lon"],
        s["to_lat"],
        s["to_lon"]
    )

    eta = predict_eta(s["depart"], distance)

    deadline = datetime.datetime.strptime(
        s["deadline"],
        "%Y-%m-%d %H:%M:%S"
    )

    print(f"[CHUYẾN XE {s['id']}]")
    print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
    print(f" + Thời gian khởi hành: {s['depart']}")
    print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")

    if eta <= deadline:
        print(" + Trạng thái: 🟢 AN TOÀN (Kịp tiến độ trước deadline)\n")
    else:
        print(
            f" + Trạng thái: 🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline.strftime('%H:%M:%S')})\n"
        )

print("========================================================")