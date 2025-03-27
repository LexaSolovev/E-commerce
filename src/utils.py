import json
import os.path

from config import PATH_DATA
from src.category import Category
from src.product import Product


def read_json(path_to_json: str) -> list[Category]:
    """Функция для чтения json файла с категориями и продуктами, возвращает список словарей"""
    with open(path_to_json, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)

    categories = []
    for category in data:
        new_category = Category(
            category["name"],
            category["description"],
            [Product(**product) for product in category["products"]]
        )
        categories.append(new_category)

    return categories


if __name__ == "__main__":
    path_to_json = os.path.join(PATH_DATA, "products.json")
    categories = read_json(path_to_json)
    print(Category.category_count)
    print(Category.product_count)
