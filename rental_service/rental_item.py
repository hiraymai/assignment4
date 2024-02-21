class RentalItem:
    def __init__(self, name, category, price_per_day, available=True):
        self.name = name
        self.category = category
        self.price_per_day = price_per_day
        self.available = available

    def __str__(self):
        return f"{self.name} - {self.category}: {'Available' if self.available else 'Not Available'} " \
               f"for {self.price_per_day}/day"