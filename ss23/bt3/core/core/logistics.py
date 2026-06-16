import math

def show_flights(flights):
    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")

    for i, f in enumerate(flights, 1):
        bottles = math.ceil(f["passengers"] / 10)

        print(f"{i}. Mã: {f['flight_id']} | Khởi hành: {f['depart_time']} | Số khách: {f['passengers']} | Dự phòng: {bottles} thùng nước.")