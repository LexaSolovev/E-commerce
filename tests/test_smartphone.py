
def test_smartphone_init(samsung):
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5
    assert samsung.efficiency == "Samsung"
    assert samsung.model == "Galaxy S23 Ultra"
    assert samsung.memory == "256GB"
    assert samsung.color == "Серый"
