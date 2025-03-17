import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def first_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def second_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def third_product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def first_category(first_product, second_product):
    products = [first_product, second_product]
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products
    )
    return category


@pytest.fixture
def second_category(third_product):
    category = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [third_product]
    )
    return category


@pytest.fixture
def samsung():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        "Samsung",
        "Galaxy S23 Ultra",
        "256GB",
        "Серый"
    )


@pytest.fixture
def iphone():
    return Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        "Apple",
        "Iphone 15",
        "512GB",
        "Gray space"
    )


@pytest.fixture
def universal():
    return LawnGrass(
        "Семена газонной травы, травосмесь Универсальная 5 кг",
        "газон универсальный, овсяница красная, мятлик, райграс, тимофеевка, овсяница луговая",
        2559.0,
        10,
        "Россия",
        "6-8 дней",
        "Зеленый"
    )


@pytest.fixture
def canada_green():
    return LawnGrass(
        "Canada Green Village 5 кг",
        "Газонная трава семена Канада Грин Дачная 5 кг",
        2310.0,
        5,
        "Канада",
        "7-14 дней",
        "Зеленый"
    )
