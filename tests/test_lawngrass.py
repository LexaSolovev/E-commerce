import pytest


def test_lawngrass_init(universal):
    assert universal.name == "Семена газонной травы, травосмесь Универсальная 5 кг"
    assert universal.description == ("газон универсальный, овсяница красная, "
                                               "мятлик, райграс, тимофеевка, овсяница луговая")
    assert universal.price == 2559.0
    assert universal.quantity == 10
    assert universal.country == "Россия"
    assert universal.germination_period == "6-8 дней"
    assert universal.color == "Зеленый"


def test_lawngrass_add(universal, canada_green):
    assert universal + canada_green == 37140.0


def test_lawngrass_add_error(universal):
    with pytest.raises(TypeError, match=r"Невозможно сложить объекты указанных типов*"):
        result = universal + 1
