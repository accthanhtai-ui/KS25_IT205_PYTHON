import unittest
from bt1 import Wallet, InvalidAmountError, InsufficientBalanceError

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet()

    def test_deposit_success(self):
        self.wallet.deposit(1000)
        self.assertEqual(self.wallet.get_balance(), 1000)

    def test_transfer_insufficient_balance(self):
        self.wallet.deposit(500)
        with self.assertRaises(InsufficientBalanceError):
            self.wallet.transfer("0987654321", 1000)

    def test_invalid_amount(self):
        with self.assertRaises(InvalidAmountError):
            self.wallet.deposit(-100)

    def test_value_error_phone(self):
        self.wallet.deposit(1000)
        with self.assertRaises(ValueError):
            self.wallet.transfer("abc", 100)

if __name__ == "__main__":
    unittest.main()
