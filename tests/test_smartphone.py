import pytest


def test_smartphone_init(product_smartphone1):
    assert product_smartphone1.name == "Iphone 15"
    assert product_smartphone1.description == "512GB, Gray space"
    assert product_smartphone1.quantity == 8
    assert product_smartphone1.price == 210000.0
    assert product_smartphone1.efficiency == 98.2
    assert product_smartphone1.model == "15"
    assert product_smartphone1.memory == 512
    assert product_smartphone1.color == "Gray space"


def test_smartphone_add(product_smartphone1, product_smartphone2):
    assert product_smartphone1 + product_smartphone2 == 2114000.0


def test_smartphone_add_error(product_smartphone1, product_smartphone2):
    with pytest.raises(TypeError):
        product_smartphone2 + 1
