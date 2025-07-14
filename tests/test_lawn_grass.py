import pytest


def test_lawn_grass_init(product_lawn_grass1):
    assert product_lawn_grass1.name == "Газонная трава"
    assert product_lawn_grass1.description == "Элитная трава для газона"
    assert product_lawn_grass1.quantity == 20
    assert product_lawn_grass1.price == 500.0
    assert product_lawn_grass1.germination_period == "7 дней"
    assert product_lawn_grass1.country == "Россия"
    assert product_lawn_grass1.color == "Зеленый"


def test_smartphone_add(product_lawn_grass1, product_lawn_grass2):
    assert product_lawn_grass1 + product_lawn_grass2 == 16750.0


def test_smartphone_add_error(product_lawn_grass1, product_lawn_grass2):
    with pytest.raises(TypeError):
        product_lawn_grass1 + 1
