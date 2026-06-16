# 1. Vấn đề với from datetime import *
# Khi import kiểu *, tất cả tên trong thư viện datetime sẽ được đưa vào không gian tên (namespace) của chương trình.
# Nếu trong code có biến global time = 120, thì sau khi import, biến này sẽ bị ghi đè bởi lớp time của datetime.
# Hậu quả: biến time không còn là số 120 nữa, mà trở thành đối tượng/lớp datetime.time.
# Dễ gây lỗi logic, khó debug, và làm code thiếu rõ ràng.
# Ví dụ sinh viên: “Em đặt biến time = 120 để tính số giây, nhưng sau khi import thì chạy không ra kết quả, vì time đã biến thành class.

# 2. Hàm thay thế os.mkdir()
# os.mkdir() chỉ tạo được một thư mục, nếu thư mục cha chưa có thì sẽ báo lỗi.
# Hàm tối ưu hơn: os.makedirs(path, exist_ok=True)
# Tạo được nhiều cấp thư mục lồng nhau.
# Tham số exist_ok=True giúp không bị lỗi nếu thư mục đã tồn tại.
# Dùng os.makedirs() là an toàn và tiện hơn.

# 3. Cấu trúc cây thư mục cho dự án Rikkei Media
# Code
# rikkei_media/
# │
# ├── main.py              # File chạy chính
# ├── config/              # Cấu hình hệ thống
# │   ├── settings.py
# │   └── logging_conf.py
# │
# ├── core/                # Các tiện ích chung
# │   ├── utils.py
# │   ├── exceptions.py
# │   └── base_model.py
# │
# ├── media/               # Quản lý dữ liệu media
# │   ├── models/          # Định nghĩa dữ liệu (ORM)
# │   │   ├── video.py
# │   │   ├── audio.py
# │   │   └── image.py
# │   ├── services/        # Xử lý logic
# │   │   ├── video_service.py
# │   │   ├── audio_service.py
# │   │   └── image_service.py
# │   └── controllers/     # API cho media
# │       ├── video_controller.py
# │       ├── audio_controller.py
# │       └── image_controller.py
# │
# ├── users/               # Quản lý người dùng
# │   ├── models/
# │   │   └── user.py
# │   ├── services/
# │   │   └── user_service.py
# │   └── controllers/
# │       └── user_controller.py
# │
# ├── database/            # Kết nối và migration DB
# │   ├── connection.py
# │   └── migrations/
# │
# ├── tests/               # Unit test & Integration test
# │   ├── test_media.py
# │   ├── test_users.py
# │   └── test_core.py
# │
# └── docs/                # Tài liệu dự án
#     ├── architecture.md
#     └── api_spec.md
from storage.disk_manager import calculate_disk_blocks, calculate_aspect_ratio
from storage.io_helper import safe_create_dir, move_file
from analytics.time_validator import parse_and_validate_date, classify_upload_time

raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

safe_create_dir("media_vault/audio")
safe_create_dir("media_vault/video")

print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
print("---------------------------------------------------------------------------")

success = 0

for f in raw_files:
    filename = f["filename"]
    size_bytes = f["size_bytes"]
    upload_at = f["upload_at"]

    print(f"\n[TỆP TIN: {filename}]")
    print(f" + Dung lượng thực tế: {size_bytes} Bytes")

    date_obj, valid = parse_and_validate_date(upload_at)

    if not valid:
        print(f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_at}' không tồn tại)")
        continue

    blocks = calculate_disk_blocks(size_bytes)

    file_type = "audio" if filename.endswith(".mp3") else "video"

    time_status = classify_upload_time(date_obj)

    if file_type == "video":
        aspect_ratio = calculate_aspect_ratio(1920, 1080)
    else:
        aspect_ratio = "N/A"

    target_path = move_file(filename, f"media_vault/{file_type}")

    print(f" + Số khối phân vùng (4KB Block): {blocks} Blocks")
    print(f" + Aspect Ratio: {aspect_ratio}")
    print(f" + Trạng thái thời gian: {time_status}")
    print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{file_type}')")

    success += 1

print("========================================================")
print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success}/{len(raw_files)} tệp tin thành công. Hệ thống ổn định.")