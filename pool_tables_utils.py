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
