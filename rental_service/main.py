from rental_service import RentalService
from rental_item import RentalItem

def main():
    service = RentalService()

    while True:
        action = input("Are you a rent-giver (add) or a rent-seeker (find)? (exit to quit): ").lower()
        if action == 'add':
            name = input("Enter the name of the item: ")
            category = input("Enter the category of the item: ")
            price_per_day = float(input("Enter the price per day: "))
            item = RentalItem(name, category, price_per_day)
            service.add_item(item)
            print("Item added successfully!")
        elif action == 'find':
            category = input("Enter the category to search for (leave blank for all): ").strip()
            items = service.find_items(category or None)
            if items:
                for item in items:
                    print(item)
            else:
                print("No items found.")
                if input("Would you like to add an item in this category? (yes/no): ").lower() == 'yes':
                    name = input("Enter the name of the item: ")
                    price_per_day = float(input("Enter the price: "))
                    item = RentalItem(name, category, price_per_day)
                    service.add_item(item)
                    print("Item added successfully!")
        elif action == 'exit':
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
