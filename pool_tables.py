
import datetime
import json

pool_tables = []
all_pool_tables = []


class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = None
        self.end_time = None
        self.is_occupied = False
        self.total_time_played = 0
        self.total_cost = 0.0
        self.total_cost_per_hour = 30.0

    def checkout(self):
        self.is_occupied = True
        self.start_time = datetime.datetime.now()

    def checkin(self):
        self.is_occupied = False
        self.end_time = datetime.datetime.now()
        self.total_time_played = self.end_time - self.start_time
        self.total_time_minutes = self.total_time_played.total_seconds() / 60
        self.total_cost = round((self.total_cost_per_hour / 60) *
                                self.total_time_minutes, 2)


def occupiedStatus(is_occupied):
    if is_occupied:
        return "Occupied"
    else:
        return "Not occupied"


# create 12 pool tables
for i in range(1, 13):
    pool_tables.append(PoolTable(i))


def display_all_pool_tables():
    for table in pool_tables:
        print(
            f"Table {table.table_number} - Checkout Status: {occupiedStatus(table.is_occupied)} - {table.start_time}")


def name_of_file():
    return "%B %d %Y"


def write_to_txt(table):
    filename = datetime.datetime.now()
    name = filename.strftime(name_of_file())
    with open(f"{name}.txt", "a") as file:
        file.write(
            f"\n\nPool Table: {table.table_number}\nStart Time: {table.start_time}\nEnd Time: {table.end_time}\nTotal Time Played: {table.total_time_played}\nCost: ${table.total_cost}")


def write_to_json(table):
    filename = datetime.datetime.now()
    name = filename.strftime(name_of_file())
    with open(f"{name}.json", 'w') as file:
        json.dump(all_pool_tables, file, default=str)


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
            # filename = datetime.datetime.now()
            # with open(filename.strftime("%B %d %Y"), "a") as file:
            #   file.write(
            #      f"\n\nPool Table: {pool_table.table_number}\nStart Time: {pool_table.start_time}\nEnd Time: {pool_table.end_time}\nTotal Time Played: {pool_table.total_time_played}\nCost: ${pool_table.total_cost}")
        else:
            print("That table is not currently occupied.")
    elif choice == '3':
        display_all_pool_tables()
    elif choice == 'q':
        break
