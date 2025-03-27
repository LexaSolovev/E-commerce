import pytest

from src.exceptions import ZeroQuantityProductException


def test_zero_quantity_product_exception():
    with pytest.raises(ZeroQuantityProductException, match="Товар с нулевым количеством не может быть добавлен"):
        raise ZeroQuantityProductException

    with pytest.raises(ZeroQuantityProductException, match="Тестовое сообщение об ошибке"):
        raise ZeroQuantityProductException("Тестовое сообщение об ошибке")
