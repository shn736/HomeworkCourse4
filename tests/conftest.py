import pytest
from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def category():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром",
        ["Iphone 15", "512GB, Gray space"]
    )


@pytest.fixture
def product():
    return [
        {"Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5},
        {"Iphone 15", "512GB, Gray space", 210000.0, 8}
    ]


@pytest.fixture
def product_smartphone1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_smartphone2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def product_lawn_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_lawn_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
