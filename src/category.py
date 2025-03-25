from src.product import Product
from src.exceptions import ZeroQuantityProductException


class Category:
    """Класс для описания категорий"""
    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        return self.__products

    @property
    def products_str(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product}\n"
        return products_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            if product.quantity != 0:
                self.__products.append(product)
                Category.product_count += 1
            else:
                raise ZeroQuantityProductException("Товар с нулевым количеством не может быть добавлен")
        else:
            raise TypeError("Невозможно добавить указанный продукт в категорию")

    def __str__(self):
        count_products = 0
        for product in self.__products:
            count_products += product.quantity
        return f'{self.name}, количество продуктов: {count_products} шт.'

    def middle_price(self):
        """ Функция возвращает среднюю цену всех товаров категории """
        try:
            result = sum([x.price for x in self.__products]) / len(self.__products)
        except ZeroDivisionError as e:
            result = 0

        return result



class ProductIterator:
    """Вспомогательный класс для перебора продуктов в категории"""

    def __init__(self, category: Category):
        self.__products = category.products
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index + 1 < len(self.__products):
            self.current_index += 1
            return self.__products[self.current_index]
        else:
            raise StopIteration
