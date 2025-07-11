import unittest
from unittest.mock import patch, mock_open
import os
from src.product import Product
from src.category import Category
from src.utils import read_json, create_objects_from_json


class TestJsonFunctions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open,
           read_data='[{"name": "Category1", '
                     '"products": [{"name": "Product1", '
                     '"description": "512GB, Gray space",'
                     ' "quantity": 5, "price": 10.99}]}]')
    def test_read_json(self, mock_file):
        path = "fake/path/to/file.json"
        expected_output = [{"name": "Category1",
                            "products": [{"name": "Product1",
                                          "description": "512GB, Gray space",
                                          "quantity": 5, "price": 10.99}]}]
        result = read_json(path)
        self.assertEqual(result, expected_output)
        mock_file.assert_called_once_with(os.path.abspath(path), 'r', encoding="UTF-8")

    def test_create_objects_from_json(self):
        data = [{"name": "Category1",
                 "description": "Смартфоны, как средство не только коммуникации, "
                                "но и получения дополнительных функций для удобства жизни",
                 "products": [{"name": "Product1",
                               "description": "512GB, Gray space",
                               "quantity": 5, "price": 10.99}]}]
        categories = create_objects_from_json(data)

        self.assertEqual(len(categories), 1)
        self.assertIsInstance(categories[0], Category)
        self.assertEqual(categories[0].name, "Category1")
        self.assertEqual(len(categories[0].products), 40)
        self.assertIsInstance(categories[0].category_in_products[0], Product)
        self.assertEqual(categories[0].category_in_products[0].name, "Product1")
        self.assertEqual(categories[0].category_in_products[0].price, 10.99)
        self.assertEqual(categories[0].category_in_products[0].description, "512GB, Gray space")
        self.assertEqual(categories[0].category_in_products[0].quantity, 5)
