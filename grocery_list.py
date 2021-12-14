from grocery_list_functions import *

while True:
    print("\nEnter 1 to create a new shopping list")
    print("Enter 2 to add to a list")
    print("Enter 3 to view all shopping lists")
    print("Enter 4 to delete an item")
    print("Enter 5 to delete an entire shopping list")
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
        try:
            list_choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a number associated with a list.")
        try:
            shopping_list = shopping_lists[list_choice - 1]
            item = input("Enter the item you'd like to add: ")
            shopping_list.add_grocery_item(GroceryItem(item))
        except IndexError:
            print("Please enter a number associated with a list.")
    elif choice == '3':
        display_all_shopping_lists()
    elif choice == '4':
        print("Select a list to delete an item from it: ")
        display_all_shopping_lists()
        list_choice = int(input("Enter choice: "))
        shopping_list = shopping_lists[list_choice - 1]
        for index1 in range(0, len(shopping_list.grocery_items)):
            list = shopping_list.grocery_items[index1]
            print(f"\t{index1+1} - {list.name}")
        del_choice = int(
            input("Enter the number associated with the item you'd like to delete: "))
        shopping_list.grocery_items.pop(del_choice-1)
    elif choice == '5':
        print("Which list would you like to delete? ")
        display_all_shopping_lists()
        list_choice = int(input("Enter choice: "))
        shopping_lists.pop(list_choice-1)
    elif choice == 'q':
        break
    else:
        print("Please enter a valid option.")
