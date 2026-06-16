import datetime

def predict_eta(departure_str, distance_km, speed=60):
    # Chuyển chuỗi thời gian khởi hành thành datetime
    departure_time = datetime.datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")

    travel_hours = distance_km / speed
  
    eta = departure_time + datetime.timedelta(hours=travel_hours)
    return eta
