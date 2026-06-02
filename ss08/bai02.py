shop_name = ""
product_name = ""
description = ""
category = ""
list_search = ""

while True:
    print("""
+============================================================+
|      HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE             |
+============================================================+
| 1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê           |
| 2. Chuẩn hóa tên shop                                      |
| 3. Kiểm tra mã giảm giá hợp lệ                             |
| 4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm       |
| 5. Thoát chương trình                                      |
+============================================================+
""")

    choice = input("> Mời bạn chọn chức năng (1-5): ")

    match choice:

        case "1":
            print("\n=== NHẬP DỮ LIỆU SẢN PHẨM ===")

            shop_name = input("Nhập tên shop: ")
            product_name = input("Nhập tên sản phẩm: ")
            description = input("Nhập mô tả sản phẩm: ")
            category = input("Nhập danh mục sản phẩm: ")
            list_search = input("Nhập danh sách từ khóa (cách nhau bằng dấu phẩy): ")

            print("\n=== BÁO CÁO THỐNG KÊ ===")
            print("Tên shop:", shop_name.strip())
            print("Tên sản phẩm:", product_name.strip().title())
            print("Mô tả sản phẩm:", description.strip())
            print("Độ dài mô tả:", len(description))
            print("Danh mục:", category.strip().lower())
            print("Danh sách từ khóa:", list_search.strip())

            keyword_count = list_search.count(",") + 1
            print("Số lượng từ khóa:", keyword_count)

            print("Mô tả chữ thường:", description.lower())
            print("Mô tả chữ hoa:", description.upper())

        case "2":
            if shop_name == "":
                print("Vui lòng nhập dữ liệu ở chức năng 1 trước!")
            else:
                print("\n=== CHUẨN HÓA TÊN SHOP ===")
                print("Tên shop ban đầu:", shop_name)

                new_shop = shop_name.strip().lower().replace(" ", "-")

                if not new_shop.startswith("shop-"):
                    new_shop = "shop-" + new_shop

                print("Tên shop sau chuẩn hóa:", new_shop)

        case "3":
            print("\n=== KIỂM TRA MÃ GIẢM GIÁ ===")

            voucher = input("Nhập mã giảm giá: ")

            if voucher == "":
                print("Mã giảm giá không được để trống!")

            elif " " in voucher:
                print("Mã giảm giá không được chứa khoảng trắng!")

            elif len(voucher) < 6 or len(voucher) > 12:
                print("Mã giảm giá phải từ 6 đến 12 ký tự!")

            elif not voucher.isupper():
                print("Mã giảm giá phải viết IN HOA!")

            elif not voucher.isalnum():
                print("Mã giảm giá chỉ gồm chữ và số!")

            elif not voucher.startswith("SALE"):
                print("Mã giảm giá phải bắt đầu bằng SALE!")

            else:
                print("Mã giảm giá hợp lệ!")

                hashtag_list = "#SALE2026,#SALE305"
                hashtag_list += ",#" + voucher

                print("Danh sách hashtag hiện tại:")
                print(hashtag_list)

        case "4":
            if description == "":
                print("Vui lòng nhập dữ liệu ở chức năng 1 trước!")
            else:
                print("\n=== TÌM KIẾM VÀ THAY THẾ ===")

                find_word = input("Nhập từ cần tìm: ")
                replace_word = input("Nhập từ thay thế: ")

                count_word = description.count(find_word)

                description = description.replace(
                    find_word,
                    replace_word
                )

                print("Mô tả sau khi thay thế:")
                print(description)

                print("Số lần tìm thấy:", count_word)

        case "5":
            print("Đã thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")
