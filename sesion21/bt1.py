import logging

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidAmountError(Exception):
    """Raised when the transaction amount is invalid (<= 0)."""
    pass

class InsufficientBalanceError(Exception):
    """Raised when the wallet balance is insufficient for transfer."""
    pass


class Wallet:
    """Ví MoMo giả lập với các chức năng nạp tiền, chuyển tiền và xem số dư."""

    def __init__(self):
        """Khởi tạo ví với số dư mặc định = 0."""
        self.balance = 0

    def deposit(self, amount: float):
        """
        Nạp tiền vào ví.
        Raise InvalidAmountError nếu số tiền <= 0.
        """
        try:
            if amount <= 0:
                raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")
            self.balance += amount
            logging.info(f"Deposit successful: +{amount} VND. Current Balance: {self.balance}")
            return self.balance
        except InvalidAmountError as e:
            logging.error(f"InvalidAmountError: Attempted to process {amount} VND.")
            raise e

    def transfer(self, phone: str, amount: float):
        """
        Chuyển tiền tới số điện thoại.
        Raise InvalidAmountError nếu số tiền <= 0.
        Raise InsufficientBalanceError nếu số dư không đủ.
        Raise ValueError nếu số điện thoại không hợp lệ.
        """
        try:
            if amount <= 0:
                raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")
            if amount > self.balance:
                raise InsufficientBalanceError("Số dư của bạn không đủ.")
            if len(phone) != 10 or not phone.isdigit():
                raise ValueError("Số điện thoại không hợp lệ.")

            if amount >= 10_000_000:
                logging.warning(f"High value transaction detected: {amount} VND to {phone}")

            self.balance -= amount
            logging.info(f"Transfer successful: -{amount} VND to {phone}. Current Balance: {self.balance}")
            return self.balance
        except InvalidAmountError as e:
            logging.error(f"InvalidAmountError: Attempted to process {amount} VND.")
            raise e
        except InsufficientBalanceError as e:
            logging.error(f"InsufficientBalanceError: Attempted to transfer {amount} VND with balance {self.balance} VND.")
            raise e

    def get_balance(self):
        """
        Trả về số dư hiện tại của ví.
        """
        try:
            logging.info(f"Balance checked. Current Balance: {self.balance}")
            return self.balance
        except Exception as e:
            logging.error("Unexpected error when checking balance.")
            raise e


def display_menu():
    """In ra menu CLI cho người dùng."""
    print("========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("====================================")


def main():
    """Hàm main chạy vòng lặp CLI."""
    wallet = Wallet()
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-4): ")

        try:
            match choice:
                case "1":
                    amount = float(input("Nhập số tiền cần nạp: "))
                    wallet.deposit(amount)
                    print(f"Nạp tiền thành công: +{amount:,} VND")
                    print(f"Số dư hiện tại: {wallet.get_balance():,} VND")

                case "2":
                    phone = input("Nhập số điện thoại người nhận: ")
                    amount = float(input("Nhập số tiền cần chuyển: "))
                    wallet.transfer(phone, amount)
                    print(f"Chuyển tiền thành công tới {phone}.")
                    print(f"Số dư còn lại: {wallet.get_balance():,} VND")

                case "3":
                    print(f"Số dư hiện tại: {wallet.get_balance():,} VND")

                case "4":
                    logging.info("System shutdown")
                    print("Cảm ơn bạn đã sử dụng dịch vụ.")
                    break

                case _:
                    print("Lựa chọn không hợp lệ.")

        except ValueError:
            logging.error("ValueError: Invalid numeric input.")
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
        except InvalidAmountError as e:
            print(f"Lỗi: {e}")
        except InsufficientBalanceError as e:
            print(f"Giao dịch thất bại: {e}")


if __name__ == "__main__":
    main()
