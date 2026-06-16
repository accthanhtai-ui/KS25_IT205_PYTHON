from datetime import datetime, timedelta

def calculate_eta(flights):
    print("----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")

    flight_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()

    for f in flights:
        if f["flight_id"] == flight_id:

            depart = datetime.strptime(f["depart_time"], "%Y-%m-%d %H:%M:%S")
            eta = depart + timedelta(minutes=f["duration_min"])

            print(f"-> Chuyến bay {flight_id} cất cánh lúc: {depart.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
            return

    print("Không tìm thấy chuyến bay!")