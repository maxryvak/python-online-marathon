import unittest
import math

class TriangleNotValidArgumentException(Exception):
    def __str__(self):
       return 'Not valid arguments'


class TriangleNotExistException(Exception):
    def __str__(self):
        return 'Can`t create triangle with this arguments'


class Triangle:
    def __init__(self, sides):
        if type(sides) == tuple:
            if len(sides) == 3:
                if all(isinstance(item, int) for item in sides):
                    self.sides = sorted(sides, reverse=True)
                    if self.sides[0] < self.sides[1] + self.sides[2]:
                        self.p = 0.5 * sum(self.sides)
                    else:
                        raise TriangleNotExistException
                else:
                    raise TriangleNotValidArgumentException
            else:
                raise TriangleNotValidArgumentException
        else:
            raise TriangleNotValidArgumentException

    def get_area(self):
        return math.sqrt(self.p * (self.p - self.sides[0]) *
                         (self.p - self.sides[1]) * (self.p - self.sides[2]))


class TriangleTest(unittest.TestCase):
    def test_valid_data(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        for i in valid_test_data:
            with self.subTest(i=i):
                t = Triangle(i[0])
                self.assertEqual(t.get_area(), i[1])
    def test_not_valid_data(self):
        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            10
        ]
        for i in not_valid_arguments:
            with self.assertRaises(TriangleNotValidArgumentException):
                t = Triangle(i)

    def test_not_valid_triangle(self):
        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        for i in not_valid_triangle:
            with self.assertRaises(TriangleNotExistException):
                t = Triangle(i)
