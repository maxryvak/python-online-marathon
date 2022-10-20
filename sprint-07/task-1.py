from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    name = "Fettuccine Alfredo"

    def cook(self):
        print(f"Italian main course prepared: {self.name}")


class Tiramisu(Product):
    name = "Tiramisu"

    def cook(self):
        print(f"Italian dessert prepared: {self.name}")


class DuckALOrange(Product):
    name = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {self.name}")


class CremeBrulee(Product):
    name = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {self.name}")


class Factory(ABC):
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        elif type_of_meal == "dessert":
            return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()
        elif type_of_meal == "dessert":
            return CremeBrulee()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory()
        elif type_of_factory == "french":
            return FrenchDishesFactory()
