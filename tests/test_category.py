import pytest

from src.category import Category, ProductIterator
from src.exceptions import ZeroQuantityProductException


def test_category_init1(first_category, first_product, second_product):
    products = [first_product, second_product]
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert first_category.products == products
    assert Category.category_count == 1
    assert Category.product_count == 2
    first_category.add_product(second_product)
    assert Category.product_count == 3
    assert first_category.products_str == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                           "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                           "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n")


def test_category_init2(second_category, third_product):
    products = [third_product]
    assert second_category.name == "Телевизоры"
    assert second_category.description == ("Современный телевизор, который позволяет наслаждаться просмотром,"
                                           " станет вашим другом и помощником")
    assert second_category.products == products
    assert Category.category_count == 2
    assert Category.product_count == 4
    assert second_category.products_str == "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_product_iterator(first_product, second_product, first_category):
    product_iterator = ProductIterator(first_category)
    assert next(product_iterator) == first_product
    assert next(product_iterator) == second_product
    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_add_product_error(first_category):
    with pytest.raises(TypeError, match="Невозможно добавить указанный продукт в категорию"):
        first_category.add_product("Непонятно что")


def test_category_middle_price(first_category):
    assert first_category.middle_price() == 195000.0


def test_category_middle_price_empty_products():
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0


def test_add_product_with_zero_quantity(zero_quantity_product, first_category):
    with pytest.raises(ZeroQuantityProductException):
        first_category.add_product(zero_quantity_product)
        