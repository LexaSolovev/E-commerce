from src.base_product import BaseProduct
from src.mixin_print import MixinPrint


class Product(MixinPrint, BaseProduct):
    """Класс для описания продуктов"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                user_answer = input("Вы уверены, что хотите уменьшить цену? (y/n):")
                if user_answer == "y":
                    self.__price = new_price
            else:
                self.__price = new_price

    @classmethod
    def new_product(cls, new_product: dict):
        return Product(**new_product)

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.__price * self.quantity) + (other.price * other.quantity)

        raise TypeError(f"Невозможно сложить объекты указанных типов: {type(self)} и {type(other)}")
