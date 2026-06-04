#  Phân tích & Thiết kế Giải pháp
# Input / Output
# Input:
# Lựa chọn menu (số nguyên 1–4).
# Mã đơn hàng (chuỗi).
# Trạng thái đơn hàng (chuỗi).
# Vị trí đơn hàng (số nguyên).

# Output:
# Hiển thị danh sách đơn hàng.
# Thông báo thêm/sửa/xóa thành công.
# Thống kê số lượng đơn hàng theo trạng thái.
# Thông báo lỗi khi nhập sai hoặc không tìm thấy.
# Giải pháp
# Dùng List để lưu trữ đơn hàng dưới dạng "MÃ - TRẠNG_THÁI".
# Các thao tác:
# append() → thêm đơn hàng mới.
# insert() hoặc gán index → sửa đơn hàng theo vị trí.
# pop() → xóa đơn hàng theo vị trí.
# remove() → xóa theo giá trị (không dùng trong bài này).

# Chuẩn hóa dữ liệu nhập:
# strip() để xóa khoảng trắng.
# upper() để chuyển thành chữ hoa.
# Dùng vòng lặp while True + match-case để hiển thị menu và xử lý.
# Dùng try/except để bắt lỗi nhập sai kiểu dữ liệu.

# Pseudocode
# order_list = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]
# while True:
#     hiển thị menu chính
#     nhập lựa chọn
#     nếu lựa chọn == 1:
#         nếu rỗng → báo trống
#         ngược lại → in danh sách
#     nếu lựa chọn == 2:
#         hiển thị menu con
#         nhập lựa chọn con
#         nếu thêm → nhập mã + trạng thái, chuẩn hóa, append
# nếu sửa → nhập vị trí, kiểm tra hợp lệ, nhập dữ liệu mới, cập nhật
# nếu xóa → nhập vị trí, kiểm tra hợp lệ, pop và báo đơn hàng bị xóa
# nếu quay lại → continue
    
#nếu lựa chọn == 3:
#duyệt danh sách, tách trạng thái, đếm số lượng
#in thống kê
    
# nếu lựa chọn == 4:
# in thông báo thoát
# break
    
#nếu nhập sai → báo lỗi

# Hệ thống quản lý đơn hàng Grab Express

order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("""1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình
    """)
    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case "1":
            if not order_list:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for i, order in enumerate(order_list, start=1):
                    print(f"{i}. {order}")

        case "2":
            while True:
                print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("""1. Thêm đơn hàng mới
2. Sửa đơn hàng theo vị trí
3. Xóa đơn hàng theo vị trí
4. Quay lại menu chính
                """)
                sub_choice = input("Nhập lựa chọn: ")

                match sub_choice:
                    case "1":
                        code = input("Nhập mã đơn hàng: ").strip().upper()
                        status = input("Nhập trạng thái đơn hàng: ").strip().upper()
                        order_list.append(f"{code} - {status}")
                        print(f"Đã thêm đơn hàng {code} - {status} vào danh sách.")

                    case "2":
                        try:
                            pos = int(input("Nhập vị trí đơn hàng cần sửa: ")) - 1
                            if 0 <= pos < len(order_list):
                                code = input("Nhập mã đơn hàng mới: ").strip().upper()
                                status = input("Nhập trạng thái mới: ").strip().upper()
                                order_list[pos] = f"{code} - {status}"
                                print("Đã cập nhật đơn hàng thành công.")
                            else:
                                print("Không tồn tại đơn hàng ở vị trí này!")
                        except ValueError:
                            print("Vị trí không hợp lệ!")

                    case "3":
                        try:
                            pos = int(input("Nhập vị trí đơn hàng cần xóa: ")) - 1
                            if 0 <= pos < len(order_list):
                                removed_order = order_list.pop(pos)
                                print(f"Đã xóa đơn hàng: {removed_order}")
                            else:
                                print("Không tồn tại đơn hàng ở vị trí này!")
                        except ValueError:
                            print("Vị trí không hợp lệ!")

                    case "4":
                        break

                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

        case "3":
            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            statuses = {"PENDING": 0, "DELIVERING": 0, "COMPLETED": 0, "CANCELLED": 0}
            for order in order_list:
                parts = order.split(" - ")
                if len(parts) == 2:
                    status = parts[1]
                    if status in statuses:
                        statuses[status] += 1
            for key, value in statuses.items():
                print(f"{key}: {value}")
            print(f"Tổng số đơn hàng: {len(order_list)}")

        case "4":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
