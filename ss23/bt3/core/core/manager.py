from datetime import datetime

def check_duplicate_id(flight_id, flights):
    flight_id = flight_id.strip().upper()

    for f in flights:
        if f["flight_id"] == flight_id:
            return True
    return False


def add_flight(flights):
    print("----- TIẾP NHẬN CHUYẾN BAY MỚI -----")

    flight_id = input("Nhập mã chuyến bay: ").strip().upper()

    if check_duplicate_id(flight_id, flights):
        print("Mã chuyến bay đã tồn tại!")
        return

    try:
        passengers = int(input("Nhập số lượng hành khách: "))
        depart_time = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ")
        duration = int(input("Nhập số phút bay: "))

        datetime.strptime(depart_time, "%Y-%m-%d %H:%M:%S")

    except ValueError:
        print("Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS")
        return

    flights.append({
        "flight_id": flight_id,
        "passengers": passengers,
        "depart_time": depart_time,
        "duration_min": duration
    })

    print(f">> Thêm chuyến bay {flight_id} thành công!")