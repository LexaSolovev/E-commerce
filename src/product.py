
class Product:
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
