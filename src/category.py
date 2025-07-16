from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Category:
    name: str
    description: str
    products: dict
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += product.quantity
        else:
            raise TypeError

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}.\n"
        return products_str

    @products.setter
    def products(self, product: Product):
        if isinstance(product, Product):
            try:
                if len(self.__products) == 0:
                    raise ZeroQuantityProduct("Нельзя добавить товар с нулевым количеством")
            except ZeroDivisionError as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def category_in_products(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([products.price for products in self.category_in_products]) / len(self.category_in_products)
        except ZeroDivisionError:
            return 0
