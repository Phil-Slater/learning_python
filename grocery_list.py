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
        for item in (shopping_list.grocery_items):
            print(item.name)


while True:
    print("\nEnter 1 to create a new shopping list")
    print("Enter 2 to add to a list")
    print("Enter 3 to view all shopping lists")
    print("Enter q to quit\n")

    choice = input("Enter choice: ")

    if choice == '1':
        display_all_shopping_lists()
        name = input("Enter name of shopping list: ")
        address = input("Enter shopping list address: ")
        shopping_list = ShoppingList(name, address)
        shopping_lists.append(shopping_list)
    elif choice == '2':
        print("To which list would you like to add? ")
        display_all_shopping_lists()
        list_choice = int(input("Enter choice: "))
        shopping_list = shopping_lists[list_choice - 1]
        item = input("Enter the item you'd like to add: ")
        shopping_list.add_grocery_item(GroceryItem(item))
    elif choice == '3':
        display_all_shopping_lists()
    elif choice == 'q':
        break
    else:
        print("Please enter a valid option.")
