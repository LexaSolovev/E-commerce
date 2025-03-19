import pytest


def test_smartphone_init(samsung):
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5
    assert samsung.efficiency == 1455382
    assert samsung.model == "Galaxy S23 Ultra"
    assert samsung.memory == "256GB"
    assert samsung.color == "Серый"


def test_smartphone_add(samsung, iphone):
    assert samsung + iphone == 2580000.0


def test_smartphone_add_error(samsung, second_category):
    with pytest.raises(TypeError, match=r"Невозможно сложить объекты указанных типов*"):
        print(samsung + second_category)
