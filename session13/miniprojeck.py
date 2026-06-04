parking_lot = []
next_id = 1

while True:

    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Check-in xe")
    print("2. Báo cáo tồn kho")
    print("3. Tìm kiếm xe")
    print("4. Check-out xe")
    print("5. Thoát")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    if not choice.isdigit():
        print("ERR-08: Lựa chọn không hợp lệ")
        continue

    if choice == "1":

        plate = input("Nhập biển số xe: ").strip().upper()

        if plate == "":
            print("ERR-02: Biển số không được để trống")
            continue

        found = False

        for value in parking_lot:

            if plate == value.get("plate"):
                found = True
                break

        if found:
            print("ERR-03: Biển số đã tồn tại trong bãi")
            continue

        while True:

            vehicle_type = input(
                "Nhập loại xe (1-Xe máy | 2-Ô tô): "
            ).strip()

            if vehicle_type == "1" or vehicle_type == "2":
                break

            print("ERR-06: Loại xe không hợp lệ")

        while True:

            entry_time = input(
                "Nhập giờ vào: "
            ).strip()

            if entry_time == "":
                print("ERR-02: Giờ vào không được để trống")
                continue

            if entry_time.isdigit():

                entry_time = int(entry_time)

                if entry_time >= 0:
                    break

            print("ERR-07: Giờ vào không hợp lệ")

        if vehicle_type == "1":
            vehicle_name = "Xe máy"
        else:
            vehicle_name = "Ô tô"

        new_car = {
            "id": next_id,
            "plate": plate,
            "type": vehicle_name,
            "entry_time": entry_time
        }

        parking_lot.append(new_car)

        next_id += 1

        print("Check-in thành công!")

    elif choice == "2":

        if len(parking_lot) == 0:

            print("ERR-01: Bãi xe hiện đang trống")

        else:

            print("\n===== DANH SÁCH XE TRONG BÃI =====")

            print("-" * 60)

            print(
                f"{'ID':<5}"
                f"{'BIỂN SỐ':<20}"
                f"{'LOẠI XE':<15}"
                f"{'GIỜ VÀO':<10}"
            )

            print("-" * 60)

            for value in parking_lot:

                print(
                    f"{value.get('id'):<5}"
                    f"{value.get('plate'):<20}"
                    f"{value.get('type'):<15}"
                    f"{value.get('entry_time'):<10}"
                )

    elif choice == "3":

        plate = input(
            "Nhập biển số cần tìm: "
        ).strip().upper()

        if plate == "":
            print("ERR-02: Biển số không được để trống")
            continue

        found = False

        for value in parking_lot:

            if plate == value.get("plate"):

                found = True

                print("\nThông tin xe:")
                print(value)

                break

        if not found:
            print("ERR-04: Không tìm thấy xe")

    elif choice == "4":

        plate = input(
            "Nhập biển số cần check-out: "
        ).strip().upper()

        if plate == "":
            print("ERR-02: Biển số không được để trống")
            continue

        found = False

        for index, value in enumerate(parking_lot):

            if plate == value.get("plate"):

                found = True

                while True:

                    exit_time = input(
                        "Nhập giờ ra: "
                    ).strip()

                    if exit_time == "":
                        print("ERR-02: Giờ ra không được để trống")
                        continue

                    if exit_time.isdigit():

                        exit_time = int(exit_time)

                        if exit_time >= value.get("entry_time"):
                            break

                    print(
                        "ERR-05: Giờ ra phải lớn hơn hoặc bằng giờ vào"
                    )

                parking_hours = (
                    exit_time
                    - value.get("entry_time")
                )

                if value.get("type") == "Xe máy":
                    fee = parking_hours * 5000
                else:
                    fee = parking_hours * 10000

                print("\n===== HÓA ĐƠN CHECK-OUT =====")
                print(f"Biển số xe: {value.get('plate')}")
                print(f"Loại xe: {value.get('type')}")
                print(f"Giờ vào: {value.get('entry_time')}")
                print(f"Giờ ra: {exit_time}")
                print(f"Số giờ gửi: {parking_hours}")
                print(f"Tổng phí: {fee:,} VNĐ")

                parking_lot.pop(index)

                print("Check-out thành công!")

                break

        if not found:
            print("ERR-04: Không tìm thấy xe")

    elif choice == "5":

        print("Thoát chương trình!")
        break

    else:

        print("ERR-08: Lựa chọn không hợp lệ")