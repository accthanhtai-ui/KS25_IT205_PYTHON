
# Phân tích & Thiết kế Giải pháp
# Input / Output
# Input:
# Lựa chọn menu (số nguyên 1–4).
# Mã đơn hàng (chuỗi, có thể nhập sai định dạng: thừa khoảng trắng, viết thường).
# Output:
# Hiển thị danh sách đơn hàng hiện tại.
# Thông báo thêm/xóa thành công.
# Thông báo lỗi khi nhập sai hoặc không tìm thấy mã đơn hàng.
#  Giải pháp
# Dùng List để lưu trữ danh sách đơn hàng.
# Các thao tác:
# append() → thêm đơn hàng mới vào cuối.
# remove(value) → xóa đơn hàng theo mã.
# len() và enumerate() → hiển thị danh sách.
# Chuẩn hóa dữ liệu nhập:
# strip() để xóa khoảng trắng.
# upper() để chuyển thành chữ hoa.
# Dùng vòng lặp while True để hiển thị menu liên tục.
# Dùng try/except để bắt lỗi nhập sai kiểu dữ liệu.
#  Pseudocode
# 
# order_list = ["GE001", "GE002", "GE003"]
# while True:
#     hiển thị menu
#     nhập lựa chọn
    
#     nếu lựa chọn == 1:
#         nếu danh sách rỗng → báo trống
#         ngược lại → in danh sách
    
#     nếu lựa chọn == 2:
#         nhập mã đơn hàng mới
#         chuẩn hóa (strip + upper)
#         append vào danh sách
    
#     nếu lựa chọn == 3:
#         nhập mã cần xóa
#         chuẩn hóa (strip + upper)
#         nếu tồn tại → remove
#         ngược lại → báo không tìm thấy
    
#     nếu lựa chọn == 4:
#         in thông báo thoát
#         break
    
#     nếu nhập sai → báo lỗi và yêu cầu nhập lại
order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("""1. Hiển thị danh sách đơn hàng
2. Thêm đơn hàng mới
3. Xóa đơn hàng theo mã
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
            new_order = input("Nhập mã đơn hàng mới: ").strip().upper()
            order_list.append(new_order)
            print(f"Đã thêm đơn hàng {new_order} vào danh sách.")

        case "3":
            delete_order = input("Nhập mã đơn hàng cần xóa: ").strip().upper()
            if delete_order in order_list:
                order_list.remove(delete_order)
                print(f"Đã xóa đơn hàng {delete_order} khỏi danh sách.")
            else:
                print("Không tìm thấy mã đơn hàng cần xóa!")

        case "4":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
