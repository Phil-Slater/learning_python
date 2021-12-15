from grocery_list_functions import *
import unittest


class GroceryItem:
    def __init__(self, name):
        self.name = name


test_class = GroceryItem("Flour")


class TestAddGroceryItem(unittest.TestCase):
    def test_add_grocery_item(self):
        print("test add grocery item")
        grocery_items = []
        grocery_items.append("Flour")
        actual = grocery_items[0]
        expected = "Flour"
        self.assertEqual(actual, expected)


unittest.main()
