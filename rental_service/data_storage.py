import json

class DataStorage:
    def __init__(self, filename='rental_data.json'):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []