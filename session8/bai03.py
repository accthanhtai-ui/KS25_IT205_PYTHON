name_gui = ""
phone_gui = ""
address_lay = ""
name_nhan = ""
phone_nhan = ""
address_giao = ""
note = ""

while True:
    print("""
+============================================================+
|    HỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS         |
+============================================================+
|    1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê        |
|    2. Chuẩn hóa mã đơn hàng                                |
|    3. Ẩn số điện thoại khách hàng                          |
|    4. Tìm kiếm và thay thế từ khóa trong ghi chú đơn hàng  |
|    5. Thoát chương trình                                   |
+============================================================+
""")

    choice = input("> Mời bạn chọn chức năng (1-5): ")

    match choice:

        case "1":
            print("\n=== NHẬP DỮ LIỆU ĐƠN HÀNG ===")

            name_gui = input("Nhập tên người gửi: ")
            phone_gui = input("Nhập số điện thoại người gửi: ")
            address_lay = input("Nhập địa chỉ lấy hàng: ")

            name_nhan = input("Nhập tên người nhận: ")
            phone_nhan = input("Nhập số điện thoại người nhận: ")
            address_giao = input("Nhập địa chỉ giao hàng: ")

            note = input("Nhập ghi chú giao hàng: ")

            print("\n=== BÁO CÁO THỐNG KÊ ===")

            print("Tên người gửi:", name_gui.strip().title())
            print("Tên người nhận:", name_nhan.strip().title())

            print("Địa chỉ lấy hàng:", address_lay.strip())
            print("Địa chỉ giao hàng:", address_giao.strip())

            print("Ghi chú giao hàng:", note.strip())
            print("Độ dài ghi chú:", len(note))

            word_count = note.count(" ") + 1
            print("Số từ trong ghi chú:", word_count)

            print("Ghi chú chữ thường:", note.lower())
            print("Ghi chú chữ hoa:", note.upper())

        case "2":
            print("\n=== CHUẨN HÓA MÃ ĐƠN HÀNG ===")

            order_code = input("Nhập mã đơn hàng: ")

            print("Mã đơn hàng ban đầu:", order_code)

            new_order_code = order_code.strip().upper().replace(" ", "-")

            if not new_order_code.startswith("GRAB-"):
                new_order_code = "GRAB-" + new_order_code

            print("Mã đơn hàng sau chuẩn hóa:", new_order_code)

        case "3":
            print("\n=== ẨN SỐ ĐIỆN THOẠI ===")

            if phone_gui == "" or phone_nhan == "":
                print("Vui lòng nhập dữ liệu ở chức năng 1 trước!")

            else:
                if not phone_gui.isdigit():
                    print("SĐT người gửi chỉ được chứa chữ số")

                elif len(phone_gui) != 10:
                    print("SĐT người gửi phải có đúng 10 số")

                else:
                    hidden_gui = phone_gui[:3] + "*" * 5 + phone_gui[-2:]
                    print("SĐT người gửi:", hidden_gui)

                if not phone_nhan.isdigit():
                    print("SĐT người nhận chỉ được chứa chữ số")

                elif len(phone_nhan) != 10:
                    print("SĐT người nhận phải có đúng 10 số")

                else:
                    hidden_nhan = phone_nhan[:3] + "*" * 5 + phone_nhan[-2:]
                    print("SĐT người nhận:", hidden_nhan)

        case "4":
            if note == "":
                print("Vui lòng nhập dữ liệu ở chức năng 1 trước!")

            else:
                print("\n=== TÌM KIẾM VÀ THAY THẾ ===")

                find_word = input("Nhập từ khóa cần tìm: ")
                replace_word = input("Nhập từ khóa thay thế: ")

                count_word = note.count(find_word)

                note = note.replace(find_word, replace_word)

                print("Ghi chú sau khi thay thế:")
                print(note)

                print("Số lần tìm thấy:", count_word)

        case "5":
            print("Đã thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")
