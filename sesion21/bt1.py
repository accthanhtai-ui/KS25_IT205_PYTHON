import logging

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def display_menu():
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("====================================")


def deposit(balance):
    print("\n--- NẠP TIỀN VÀO VÍ ---")

    try:
        amount = float(input("Nhập số tiền cần nạp: "))

        if amount <= 0:
            raise Exception("Số tiền giao dịch phải lớn hơn 0.")

        balance += amount

        logging.info(
            f"Deposit successful: +{amount} VND. "
            f"Current Balance: {balance}"
        )

        print(f"Nạp tiền thành công: +{amount:,.0f} VND")
        print(f"Số dư hiện tại: {balance:,.0f} VND")

    except ValueError:
        logging.error(
            "ValueError: Invalid numeric input for deposit."
        )
        print("Lỗi: Vui lòng nhập số tiền hợp lệ.")

    except Exception as e:
        logging.error(
            f"InvalidAmountError: Attempted to process {amount} VND."
        )
        print("Lỗi:", e)

    return balance


def transfer(balance):
    print("\n--- CHUYỂN TIỀN ---")

    phone = input("Nhập số điện thoại người nhận: ")

    try:
        amount = float(input("Nhập số tiền cần chuyển: "))

        if amount <= 0:
            raise Exception("Số tiền giao dịch phải lớn hơn 0.")

        if amount > balance:
            raise Exception("Số dư của bạn không đủ.")

        if len(phone) != 10 or not phone.isdigit():
            raise Exception("Số điện thoại không hợp lệ.")

        if amount >= 10000000:
            logging.warning(
                f"High value transaction detected: "
                f"{amount} VND to {phone}"
            )

        balance -= amount

        logging.info(
            f"Transfer successful: -{amount} VND to {phone}. "
            f"Current Balance: {balance}"
        )

        print(f"Chuyển tiền thành công tới số điện thoại {phone}.")
        print(f"Số dư còn lại: {balance:,.0f} VND")

    except ValueError:
        logging.error(
            "ValueError: Invalid numeric input for transfer."
        )
        print("Lỗi: Vui lòng nhập số tiền hợp lệ.")

    except Exception as e:
        logging.error(str(e))
        print("Giao dịch thất bại:", e)

    return balance


def check_balance(balance):
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {balance:,.0f} VND")

    logging.info(
        f"Balance checked. Current Balance: {balance}"
    )


balance = 0

while True:
    display_menu()

    choice = input("Chọn chức năng (1-4): ")

    match choice:
        case "1":
            balance = deposit(balance)

        case "2":
            balance = transfer(balance)

        case "3":
            check_balance(balance)

        case "4":
            logging.info("System shutdown")
            print("Cảm ơn bạn đã sử dụng dịch vụ.")
            break

        case _:
            print("Lựa chọn không hợp lệ.")
