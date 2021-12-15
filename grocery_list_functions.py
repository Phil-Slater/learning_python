shopping_lists = []


class GroceryItem:
    def __init__(self, name):
        self.name = name


class ShoppingList:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.grocery_items = []

    def add_grocery_item(self, item):
        self.grocery_items.append(item)


def display_all_shopping_lists():
    for index in range(0, len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print(f"{index+1}: {shopping_list.name} - {shopping_list.address}")
        for index1 in range(0, len(shopping_list.grocery_items)):
            list = shopping_list.grocery_items[index1]
            print(f"\t{index1+1} - {list.name}")
