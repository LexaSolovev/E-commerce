def test_mixin_print(capsys, third_product, iphone, canada_green):
    message = capsys.readouterr().out.strip()
    assert 'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)' in message
    assert 'Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)' in message
    assert 'LawnGrass(Canada Green Village 5 кг, Газонная трава семена Канада Грин Дачная 5 кг, 2310.0, 5)' in message
