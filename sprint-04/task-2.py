import itertools


class Pizza:
    order_number = itertools.count()
    ingredients = []

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.order_number = next(Pizza.order_number) + 1

    @staticmethod
    def hawaiian():
        Pizza.ingredients = ['ham', 'pineapple']
        obj = object.__new__(Pizza, Pizza.ingredients)
        obj.order_number = next(Pizza.order_number) + 1
        return obj

    @staticmethod
    def meat_festival():
        Pizza.ingredients = ['beef', 'meatball', 'bacon']
        obj = object.__new__(Pizza, Pizza.ingredients)
        obj.order_number = next(Pizza.order_number) + 1
        return obj

    @staticmethod
    def garden_feast():
        Pizza.ingredients = ['spinach', 'olives', 'mushroom']
        obj = object.__new__(Pizza, Pizza.ingredients)
        obj.order_number = next(Pizza.order_number) + 1
        return obj
