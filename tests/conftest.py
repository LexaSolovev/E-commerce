import pytest

from src.product import Product


@pytest.fixture
def first_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def second_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


