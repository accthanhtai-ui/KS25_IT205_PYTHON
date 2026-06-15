import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


def view_menu():
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, item in DRINK_MENU.items():
        print(f"[{code}] - {item['name']} - {item['price']:,} VNĐ")


def add_to_order():
    try:
        print("\n--- THÊM MÓN VÀO GIỎ ---")

        code = input("Nhập mã đồ uống: ").strip().upper()

        if code not in DRINK_MENU:
            raise Exception("ItemNotFound")

        quantity = int(input("Nhập số lượng: "))

        if quantity <= 0:
            raise Exception("InvalidQuantity")

        current_order.append({
            "code": code,
            "quantity": quantity
        })

        logging.info(f"Added {quantity} of {code} to order")

        print(
            f"Đã thêm {quantity} x "
            f"{DRINK_MENU[code]['name']} vào giỏ hàng."
        )

    except ValueError:
        logging.error("ValueError - Invalid quantity input")
        print("Vui lòng nhập số lượng là một số nguyên!")

    except Exception as e:

        if str(e) == "ItemNotFound":
            logging.warning(
                f"ItemNotFoundError - Code: {code}"
            )
            print(
                "Mã đồ uống không hợp lệ, "
                "vui lòng kiểm tra lại thực đơn!"
            )

        elif str(e) == "InvalidQuantity":
            logging.warning(
                f"InvalidQuantityError - Quantity: {quantity}"
            )
            print("Số lượng phải lớn hơn 0!")


def calculate_total():
    total = 0

    for item in current_order:
        code = item["code"]
        quantity = item["quantity"]

        total += DRINK_MENU[code]["price"] * quantity

    return total


def view_order():

    if len(current_order) == 0:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    total = calculate_total()

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")

    for item in current_order:
        code = item["code"]
        quantity = item["quantity"]

        name = DRINK_MENU[code]["name"]
        price = DRINK_MENU[code]["price"]

        print(
            f"{code} - {name} - "
            f"{quantity} x {price:,} VNĐ"
        )

    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")


def checkout():

    if len(current_order) == 0:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    total = calculate_total()

    confirm = input(
        f"Xác nhận thanh toán {total:,} VNĐ? (y/n): "
    ).lower()

    if confirm == "y":
        logging.info("Checkout successful")
        print("Thanh toán thành công.")
        current_order.clear()

    elif confirm == "n":
        print("Đã hủy thao tác thanh toán.")

    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")


while True:

    print("\n========== HIGHLANDS MINI POS ==========")
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")

    choice = input("Chọn chức năng (1-5): ")

    match choice:

        case "1":
            view_menu()

        case "2":
            add_to_order()

        case "3":
            view_order()

        case "4":
            checkout()

        case "5":
            logging.info(
                "Cashier logged out. System shutdown."
            )
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            break

        case _:
            print("Lựa chọn không hợp lệ.")
