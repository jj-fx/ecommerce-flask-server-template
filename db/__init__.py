from tinydb import TinyDB


class DB:
    def __init__(self):
        self.items = TinyDB('db_items.json')
        self.animals = TinyDB('db_animals.json')
        self.categories = TinyDB('db_categories.json')
