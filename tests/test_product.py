from src.product import Product
import pytest

def test_product_init(first_product, second_product):
    assert first_product.name == 'Samsung Galaxy S23 Ultra'
    assert first_product.description == '256GB, Серый цвет, 200MP камера'
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == 'Iphone 15'
    assert second_product.description == '512GB, Gray space'
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_new_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    new_product.name = "Samsung Galaxy S23 Ultra"
    new_product.description = "256GB, Серый цвет, 200MP камера"
    new_product.price = 180000.0
    new_product.quantity = 5


def test_product_str(first_product):
    assert str(first_product) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_product_add(first_product, second_product):
    assert first_product + second_product == 2580000.0


def test_product_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product(
            name="Samsung Galaxy S23 Ultra",
            description="256GB, Серый цвет, 200MP камера",
            price=180000.0,
            quantity=0
        )

