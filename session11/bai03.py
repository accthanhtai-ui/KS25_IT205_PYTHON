# Input:
#  Người dùng nhập menu từ 1 - 5
#  Nhập mã sản phẩm, tên sản phẩm, giá, số lượng

# Output:
#  Hiển thị danh sách sản phẩm
#  Thêm, sửa, xoá sản phẩm
#  Báo lỗi nếu dữ liệu không hợp lệ

# Ý tưởng:
#  Dùng list để lưu danh sách sản phẩm
#  Mỗi sản phẩm là 1 dictionary
#  Dùng while True để chạy menu
#  Dùng for để tìm sản phẩm


product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn: ")
    # CHỨC NĂNG 1: HIỂN THỊ SẢN PHẨM
    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")

            stt = 1
            for product in product_list:
                print(
                    f"{stt}. "
                    f"Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Số lượng: {product['quantity']}"
                )
                stt += 1
    # CHỨC NĂNG 2: THÊM SẢN PHẨM
    elif choice == "2":
        product_id = input("Nhập mã sản phẩm: ")
        product_id = product_id.strip().upper()
        check_duplicate = False
        for product in product_list:
            if product["product_id"] == product_id:
                check_duplicate = True
        if check_duplicate:
            print("Mã sản phẩm bị trùng")
        else:
            product_name = input("Nhập tên sản phẩm: ")
            price = input("Nhập giá sản phẩm: ")
            quantity = input("Nhập số lượng sản phẩm: ")
            if not price.isdigit() or not quantity.isdigit():
                print("Giá/Số lượng không hợp lệ")
            else:
                price = int(price)
                quantity = int(quantity)
                if price <= 0 or quantity <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    new_product = {
                        "product_id": product_id,
                        "product_name": product_name,
                        "price": price,
                        "quantity": quantity
                    }
                    product_list.append(new_product)
                    print("Thêm sản phẩm thành công")
    # CHỨC NĂNG 3: CẬP NHẬT
    elif choice == "3":
        update_id = input("Nhập mã sản phẩm cần cập nhật: ")
        update_id = update_id.strip().upper()
        found = False
        for product in product_list:
            if product["product_id"] == update_id:
                found = True
                new_name = input("Nhập tên mới: ")
                new_price = input("Nhập giá mới: ")
                new_quantity = input("Nhập số lượng mới: ")
                if not new_price.isdigit() or not new_quantity.isdigit():
                    print("Giá/Số lượng không hợp lệ")
                else:
                    new_price = int(new_price)
                    new_quantity = int(new_quantity)

                    if new_price <= 0 or new_quantity <= 0:
                        print("Giá/Số lượng không hợp lệ")
                    else:
                        product["product_name"] = new_name
                        product["price"] = new_price
                        product["quantity"] = new_quantity
                        print("Cập nhật sản phẩm thành công")

        if found == False:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
    # CHỨC NĂNG 4: XOÁ SẢN PHẨM
    elif choice == "4":
        delete_id = input("Nhập mã sản phẩm cần xoá: ")
        delete_id = delete_id.strip().upper()
        found = False
        for product in product_list:
            if product["product_id"] == delete_id:
                product_list.remove(product)
                found = True
                print("Xóa sản phẩm thành công")
                break
        if found == False:
            print("Không tìm thấy mã sản phẩm cần xoá!")
    # CHỨC NĂNG 5: THOÁT
    elif choice == "5":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")