from rental_item import RentalItem
from data_storage import DataStorage

class RentalService:
    def __init__(self):
        self.storage = DataStorage()
        self.items = self.load_items()

    def load_items(self):
        data = self.storage.load_data()
        return [RentalItem(**item) for item in data]

    def add_item(self, item):
        self.items.append(item)
        self.save_items()

    def find_items(self, category=None):
        return [item for item in self.items if item.category == category or category is None]

    def save_items(self):
        self.storage.save_data([item.__dict__ for item in self.items])
