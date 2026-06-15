import logging

# cấu hình logging ra terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# custom exceptions
class ItemNotFoundError(Exception):
    """Raised when the drink code does not exist in menu."""
    pass

class InvalidQuantityError(Exception):
    """Raised when the quantity is <= 0."""
    pass


DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


def view_menu():
    """In ra thực đơn Highlands Coffee với mã, tên và giá tiền."""
    print("--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, item in DRINK_MENU.items():
        print(f"[{code}] - {item['name']} - {item['price']:,} VNĐ")


def add_to_order(drink_code, quantity):
    """
    Thêm món vào giỏ hàng.
    Raise ItemNotFoundError nếu mã không tồn tại.
    Raise InvalidQuantityError nếu số lượng <= 0.
    Raise ValueError nếu nhập chữ thay vì số.
    """
    try:
        code = drink_code.strip().upper()
        if code not in DRINK_MENU:
            raise ItemNotFoundError(f"Code: {code}")
        if not isinstance(quantity, int):
            raise ValueError("Invalid quantity input")
        if quantity <= 0:
            raise InvalidQuantityError(f"Quantity: {quantity}")

        current_order.append({"code": code, "quantity": quantity})
        logging.info(f"Added {quantity} of {code} to order")
        print(f"Đã thêm {quantity} x {DRINK_MENU[code]['name']} vào giỏ hàng.")
    except ValueError:
        logging.error("ValueError - Invalid quantity input")
        print("Vui lòng nhập số lượng là một số nguyên!")
        raise
    except ItemNotFoundError as e:
        logging.warning(f"ItemNotFoundError - {e}")
        print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
        raise
    except InvalidQuantityError as e:
        logging.warning(f"InvalidQuantityError - {e}")
        print("Số lượng phải lớn hơn 0!")
        raise


def view_order():
    """In ra giỏ hàng hiện tại và tính tổng tiền. Trả về tổng tiền."""
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return 0

    print("--- GIỎ HÀNG HIỆN TẠI ---")
    print("Mã SP | Tên đồ uống          | Đơn giá  | Số lượng | Thành tiền")
    print("----------------------------------------------------------------")
    total = 0
    for item in current_order:
        code = item["code"]
        qty = item["quantity"]
        name = DRINK_MENU[code]["name"]
        price = DRINK_MENU[code]["price"]
        subtotal = price * qty
        total += subtotal
        print(f"{code:<5} | {name:<20} | {price:,}   | {qty:<8} | {subtotal:,} VNĐ")
    print("----------------------------------------------------------------")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    return total


def checkout():
    """Xác nhận thanh toán, ghi log và làm rỗng giỏ hàng nếu thành công."""
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return
    total = view_order()
    confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").lower()
    if confirm == "y":
        logging.info("Checkout successful")
        print("Thanh toán thành công.")
        current_order.clear()
        print("Giỏ hàng đã được làm trống.")
    elif confirm == "n":
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")


def main():
    """Hàm main chạy vòng lặp CLI."""
    while True:
        print("========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")
        choice = input("Chọn chức năng (1-5): ")

        match choice:
            case "1":
                view_menu()
            case "2":
                code = input("Nhập mã đồ uống: ")
                try:
                    qty = int(input("Nhập số lượng: "))
                except ValueError:
                    qty = "abc"  # để raise ValueError trong add_to_order
                try:
                    add_to_order(code, qty)
                except Exception:
                    pass
            case "3":
                view_order()
            case "4":
                checkout()
            case "5":
                logging.info("Cashier logged out. System shutdown.")
                print("Đã thoát ca làm việc. Hẹn gặp lại!")
                break
            case _:
                print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
