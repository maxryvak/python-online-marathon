import unittest


class Product:
    def __init__(self, name, price, count):
        self.name, self.price, self.count = name, price, count


class Cart:
    def __init__(self, products):
        self.products = products

    def get_total_price(self):
        total = 0
        for product in self.products:
            count = product.count
            cost = count * product.price

            if 5 <= count < 7:
                total += cost - cost * 0.05
            elif 7 <= count < 10:
                total += cost - cost * 0.1
            elif 10 <= count < 20:
                total += cost - cost * 0.2
            elif count == 20:
                total += cost - cost * 0.3
            elif count >= 20:
                total += cost * 0.5
            else:
                total += cost
        return total


class CartTest(unittest.TestCase):
    def test_between_5_and_7(self):
        p = (Product('p1', 100, 5),)
        cart = Cart(p)
        self.assertEqual(cart.get_total_price(), 475)

    def test_between_7_and_10(self):
        p = (Product('p1', 100, 7),)
        cart = Cart(p)
        self.assertEqual(cart.get_total_price(), 630)

    def test_between_10_and_20(self):
        p = (Product('p1', 100, 12),)
        cart = Cart(p)
        self.assertEqual(cart.get_total_price(), 960)

    def test_equal_20(self):
        p = (Product('p1', 100, 20),)
        cart = Cart(p)
        self.assertEqual(cart.get_total_price(), 1400)

    def test_more_20(self):
        p = (Product('p1', 100, 25),)
        cart = Cart(p)
        self.assertEqual(cart.get_total_price(), 1250)
