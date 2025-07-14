import pytest

from src.product import Product


def test_category_init(category):
    assert category.name == "Телевизоры"
    assert category.description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert category.category_in_products == ["Iphone 15", "512GB, Gray space"]


def test_category_initialization(category):
    assert category.name == 'Телевизоры'
    assert category.description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert len(category.category_in_products) == 2
    assert category.product_count == 4


def test_add_product(category, first_product):
    new_product = Product(name="Продукт 2", description="Описание категории", price=200, quantity=5)
    category.add_product(new_product)

    assert len(category.category_in_products) == 3
    assert category.product_count == 11


def test_product_representation(category):
    expected_output = ['Iphone 15', '512GB, Gray space']
    assert category.category_in_products == expected_output


def test_set_products(category):
    new_product = Product(name="Продукт 3", description="Описание категории", price=150, quantity=3)
    category.products = new_product

    assert len(category.category_in_products) == 3
    assert category.product_count == 16


def test_category_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_products_property(category):
    assert category.products == 'Iphone 15.\n512GB, Gray space.\n'


def test_category_products_setter(category, first_product):
    assert len(category.category_in_products) == 2
    category.products = first_product
    assert len(category.category_in_products) == 3


def test_category_products_setter_error(category, first_product):
    with pytest.raises(TypeError):
        category.products = "Not a product"


def test_category_products_setter_smartphone(category, product_smartphone1):
    category.products = product_smartphone1
    assert category.category_in_products[0] == 'Iphone 15'
