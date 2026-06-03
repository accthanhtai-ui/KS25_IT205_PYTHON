#Input:
# Người dùng nhập lựa chọn menu (1 - 5)
# Nhập mã sản phẩm
# Nhập số lượng mua / nhập kho

#Output:
# Hiển thị danh sách sản phẩm
# Bán sản phẩm thành công
# Nhập thêm hàng thành công
# Báo cáo doanh thu
# Thông báo lỗi nếu nhập sai

#2. Giải pháp thực hiện
# Dùng list để lưu danh sách sản phẩm
# Mỗi sản phẩm là dictionary
# Dùng vòng lặp while True để chạy menu
# Dùng strip() và upper() để chuẩn hóa mã sản phẩm
# Dùng try-except kiểm tra dữ liệu nhập vào
# Dùng vòng lặp for để tìm sản phẩm theo mã

#3. Thuật toán
#B1: Hiển thị menu
#B2: Người dùng chọn chức năng

#Nếu chọn 1:
# Hiển thị danh sách sản phẩm
# Kiểm tra trạng thái tồn kho

#Nếu chọn 2:
# Nhập mã sản phẩm
# Kiểm tra tồn tại
# Nhập số lượng mua
# Kiểm tra hợp lệ
# Trừ tồn kho
# Tăng số lượng đã bán
# Tính tiền

#Nếu chọn 3:
# Nhập mã sản phẩm
# Kiểm tra tồn tại
# Nhập số lượng thêm
# Cộng vào tồn kho

#Nếu chọn 4:
# Tính doanh thu từng sản phẩm
# Tính tổng doanh thu
# Tìm sản phẩm bán chạy nhất

#Nếu chọn 5:
# Thoát chương trình
#Nếu nhập sai menu:
# Báo lỗi và nhập lại

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
    print("===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("""1. Hiển thị danh sách sản phẩm
2. Bán sản phẩm
3. Nhập thêm hàng
4. Xem báo cáo doanh thu
5. Thoát chương trình
    """)
    choice = input("Nhập lựa chọn của bạn: ").strip()
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")
            for index, product in enumerate(product_list, start=1):
                print(
                    f"{index}. "
                    f"Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Số lượng: {product['quantity']}"
                )
    elif choice == "2":
        product_id = input(
            "Nhập mã sản phẩm: "
        ).strip().upper()
        product_name = input(
            "Nhập tên sản phẩm: "
        ).strip()
        is_duplicate = False
        for product in product_list:
            if product["product_id"] == product_id:
                is_duplicate = True
                break
        if is_duplicate:
            print("Mã sản phẩm bị trùng")
        else:
            try:
                price = int(
                    input("Nhập giá sản phẩm: ")
                )
                quantity = int(
                    input("Nhập số lượng sản phẩm: ")
                )
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
            except:
                print("Giá/Số lượng không hợp lệ")
    elif choice == "3":
        update_id = input(
            "Nhập mã sản phẩm cần cập nhật: "
        ).strip().upper()
        found_product = None
        for product in product_list:
            if product["product_id"] == update_id:
                found_product = product
                break
        if found_product is None:
            print(
                "Không tìm thấy mã sản phẩm cần cập nhật!"
            )
        else:
            new_name = input(
                "Nhập tên sản phẩm mới: "
            ).strip()

            try:
                new_price = int(
                    input("Nhập giá sản phẩm mới: ")
                )
                new_quantity = int(
                    input("Nhập số lượng mới: ")
                )
                if new_price <= 0 or new_quantity <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    found_product["product_name"] = new_name
                    found_product["price"] = new_price
                    found_product["quantity"] = new_quantity
                    print(
                        "Cập nhật sản phẩm thành công"
                    )
            except:
                print("Giá/Số lượng không hợp lệ")

    elif choice == "4":
        delete_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip().upper()
        found_product = None
        for product in product_list:
            if product["product_id"] == delete_id:
                found_product = product
                break
        if found_product is None:
            print("Không tìm thấy mã sản phẩm cần xoá!")
        else:
            product_list.remove(found_product)
            print("Xóa sản phẩm thành công")
    elif choice == "5":
        print("Thoát chương trình.")
        break
    else:
        print(
            "Lựa chọn không hợp lệ, vui lòng nhập lại!"
        )