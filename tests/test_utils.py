import os

from config import PATH_DATA
from src.category import Category
from src.utils import read_json


def test_read_json():
    Category.category_count = 0
    Category.product_count = 0
    path_to_json = os.path.join(PATH_DATA, "products.json")
    categories = read_json(path_to_json)
    assert Category.category_count == 2
    assert Category.product_count == 4
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == ("Смартфоны, как средство не только коммуникации, "
                                         "но и получение дополнительных функций для удобства жизни")
    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[1].name == "Телевизоры"
    assert categories[1].description == ("Современный телевизор, "
                                         "который позволяет наслаждаться просмотром, станет вашим другом и помощником")
    assert categories[1].products[0].name == "55\" QLED 4K"
