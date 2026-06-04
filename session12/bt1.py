# (1) Phân tích và thiết kế giải pháp
# Input / Output
# Input:

# Người dùng nhập lựa chọn menu (1–5).

# Khi thêm/cập nhật: nhập id, name, number, price.

# Khi xóa: nhập id.

# Output:

# Bảng chi tiết giỏ hàng (STT, ID, Tên, SL, Đơn giá, Thành tiền).

# Tổng số lượng và tổng tiền.

# Thông báo khi thêm/cập nhật/xóa thành công hoặc khi dữ liệu không hợp lệ.

# Thông báo khi nhập sai menu hoặc sản phẩm không tồn tại.

# Giải pháp
# Dùng list chứa dictionary để quản lý giỏ hàng.

# Viết các hàm riêng cho từng chức năng: show_cart(), add_product(), update_product(), delete_product().

# Kiểm tra dữ liệu hợp lệ (số lượng > 0, đơn giá > 0).

# Validate menu bằng match-case hoặc if-elif.

# Dùng vòng lặp while True để chạy CLI cho đến khi chọn thoát.

# Pseudocode
# Code
# cart_items = [ {id, name, number, price}, {...} ]

# function show_cart():
#     if cart empty -> print "Giỏ hàng trống"
#     else:
#         in bảng sản phẩm
#         tính tổng số lượng, tổng tiền
#         in kết quả

# function add_product():
#     nhập id, name, number, price
#     validate number > 0, price > 0
#     nếu id tồn tại -> cộng dồn số lượng
#     nếu chưa tồn tại -> append vào list

# function update_product():
#     nhập id, number
#     validate number > 0
#     nếu id tồn tại -> cập nhật số lượng
#     nếu không -> báo lỗi

# function delete_product():
#     nhập id
#     nếu id tồn tại -> xóa khỏi list
#     nếu không -> báo lỗi

# while True:
#     in menu
#     nhập choice
#     match choice:
#         case "1": show_cart()
#         case "2": add_product()
#         case "3": update_product()
#         case "4": delete_product()
#         case "5": break
#         case _: báo lỗi

cart_items = [
    {"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000}
]
while True:
    print("SHOPEE CART MANAGEMENT SYSTEM")
    print("1. Xem chi tiết giỏ hàng và tính tổng tiền\n"+
          "2.Thêm sản phẩm mới / Cộng dồn số lượng\n" +
          "3. Cập nhật số lượng của một sản phẩm\n" +
          "4. Xóa sản phẩm khỏi giỏ hàng\n" +
          "5. Thoát chương trình\n")
    choice = input("nhập lựa chọn của bạn :")
    match choice:
            case "1":
                    print("-Chi tiết giỏ hàng-")
                    print(f"{'STT':<3} | {'Mã SP':<5} | {'Tên sản phẩm':<20} | {'SL':<5} | {'Đơn giá':<10} | {'Thành tiền':<15}")
                    total_product = 0
                    total_money = 0
                    for index, value in enumerate(cart_items, start=1):
                        money_product = value.get('number') * value.get('price')
                        print(f"{index:<3} | {value.get('id'):<5} | {value.get('name'):<20} | {value.get('number'):<5} | {value.get('price'):<10} | {money_product:<15}")
                        total_product += value.get('number')
                        total_money += money_product
                    print("Tổng số lượng sản phẩm trong giỏ:", total_product)
                    print("TỔNG TIỀN THANH TOÁN:", total_money)

            case "2":
                    pro_id = input("Nhập mã sản phẩm: ")
                    pro_name = input("Nhập tên sản phẩm: ")

                    while True:
                        pro_number = input("Nhập số lượng: ")
                        if pro_number.isdigit():
                            pro_number = int(pro_number)
                            break
                        else:
                            print("Bạn nhập không hợp lệ!")

                    while True:
                        pro_price = input("Nhập đơn giá: ")
                        if pro_price.isdigit():
                            pro_price = int(pro_price)
                            break
                        else:
                            print("Bạn nhập không phải số!")
                    # kiểm tra tồn tại hay không => dùng for để tìm kiếm
                    found = False
                    for index, value in enumerate(cart_items):
                        if pro_id == value.get("id"):
                            print("Có tồn tại, tiến hành cập nhật")
                            cart_items[index]["number"] += pro_number
                            found = True
                            break

                    if not found:
                        print("Không có tồn tại, tiến hành thêm mới")
                        new_product = {
                            'id': pro_id,
                            'name': pro_name,
                            'number': pro_number,
                            'price': pro_price
                        }
                        cart_items.append(new_product)
            case "3":
                        update_pro_id = input("Nhập vào id cần cập nhật: ")
                        while True:
                            update_pro_number = input("Nhập vào số lượng cần cập nhật: ")
                            if update_pro_number.isdigit():
                                update_pro_number = int(update_pro_number)
                                break
                            else:
                                print("Bạn nhập không hợp lệ!")

                        found = False
                        for index, value in enumerate(cart_items):
                            if (update_pro_id == value.get("id")):
                                print("Có tồn tại, tiến hành cập nhật!")
                                cart_items[index]["number"] = update_pro_number
                                found = True
                                break
                        if (not found):
                            print("Không có tồn tại!")
            case "4":
                        del_pro_id = input("Nhập vào id cần xóa: ") 
                        found = False; 
                        for index, value in enumerate(cart_items):
                            if (del_pro_id == value.get("id")):
                                print("Có tồn tại, tiến hành xóa!")
                                del cart_items[index]
                                found = True
                                break  
                        if (not found):        
                            print("Không có tồn tại")
                        print()
            case "5":
                        print("Thoát chương trình!")
                        break
            case _:
                          print("Lựa chọn không hợp lệ!")
                        

        
                                                                                