from src.product import Product


def test_product_init1(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_init2(second_product):
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8

def test_product_new_product(capsys):
    product = Product.new_product(
        {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    product.price = 190000.0
    assert product.price == 190000.0
    product.price = -1
    message = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in message.out.strip()

def test_product_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_product_add(first_product, second_product):
    assert first_product + second_product == 2580000.0
