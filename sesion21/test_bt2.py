import unittest
from bt2 import add_to_order, view_order, current_order, InvalidQuantityError, ItemNotFoundError

class TestHighlandsPOS(unittest.TestCase):
    def setUp(self):
        current_order.clear()

    def test_calculate_total(self):
        add_to_order("P1", 2)
        add_to_order("F1", 1)
        result = view_order()
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        with self.assertRaises(InvalidQuantityError):
            add_to_order("T1", -1)

    def test_item_not_found(self):
        with self.assertRaises(ItemNotFoundError):
            add_to_order("X9", 1)

    def test_value_error_quantity(self):
        with self.assertRaises(ValueError):
            add_to_order("P1", "abc")

if __name__ == "__main__":
    unittest.main()
