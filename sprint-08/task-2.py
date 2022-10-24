import unittest


def divide(num_1, num_2):
    return float(num_1) / num_2


class DivideTest(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 4, 0)

    def test_division_by_int(self):
        self.assertLess(divide(50, 3), 50)

    def test_division_by_float(self):
        self.assertGreater(divide(50, 0.3), 50)

    def test_division_minus(self):
        self.assertLess(divide(456, -4), 0)

    def test_divider_3(self):
        self.assertAlmostEqual(divide(40, 3), 13.33, 2)
