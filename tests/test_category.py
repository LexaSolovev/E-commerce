from src.category import Category


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
