
from pool_tables_utils import *

# create 12 pool tables
for i in range(1, 13):
    pool_tables.append(PoolTable(i))


while True:
    print('Enter 1 to checkout table: ')
    print('Enter 2 to checkin table: ')
    print('Enter 3 to display all tables: ')
    print('Enter q to quit: ')

    choice = input('Enter choice: ')

    if choice == '1':
        display_all_pool_tables()
        table_number = int(
            input("Enter the table number you'd like to checkout: "))
        pool_table = pool_tables[table_number - 1]
        if pool_table.is_occupied == True:
            print(
                f"Pool table {pool_table.table_number} is currently occupied!")
        else:
            pool_table.checkout()
            print(
                f"You have checked out table number {table_number}. Have fun!")
    elif choice == '2':
        display_all_pool_tables()
        choice = int(
            input("Enter the table number that you'd like to check in: "))
        pool_table = pool_tables[choice - 1]
        if pool_table.is_occupied == True:
            pool_table.checkin()
            all_pool_tables.append(pool_table.__dict__)
            print(
                f"Pool table {choice} has been checked in. You played for {pool_table.total_time_played} minutes and owe ${pool_table.total_cost}")
            write_to_txt(pool_table)
            write_to_json(pool_table)
        else:
            print("That table is not currently occupied.")
    elif choice == '3':
        display_all_pool_tables()
    elif choice == 'q':
        break
