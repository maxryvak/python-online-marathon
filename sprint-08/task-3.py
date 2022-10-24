import unittest
import math


def quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c

    if a == b == c == 0:
        raise ValueError
    elif b == c == 0:
        return 0
    elif b == 0 and -c / a > 0:
        return math.sqrt(-c / a), -math.sqrt(-c / a)
    elif b == 0 and -c / a < 0:
        return None
    elif c == 0:
        return 0, -b / a
    elif D < 0:
        return None
    elif D == 0:
        return -b / (2 * a)
    elif D > 0:
        return (-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a)


class QuadraticEquationTest(unittest.TestCase):
    def test_abc_0(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 0, 0)

    def test_bc_0(self):
        self.assertEqual(quadratic_equation(1, 0, 0), 0)

    def test_b0_ac_less_0(self):
        self.assertIsNone(quadratic_equation(1, 0, 4))

    def test_b0_ac_grater_0(self):
        self.assertEqual(quadratic_equation(-1, 0, 4), (2, -2))

    def test_c_0(self):
        self.assertEqual(quadratic_equation(1, 2, 0), (0, -2))

    def test_D_less_0(self):
        self.assertIsNone(quadratic_equation(1, -3, 4))

    def test_D_equal_0(self):
        self.assertEqual(quadratic_equation(1, -4, 4), 2)

    def test_D_grater_0(self):
        self.assertEqual(quadratic_equation(1, 4, -21), (3, -7))
