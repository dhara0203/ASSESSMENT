class Fruit:
    """Represents a Fruit in the store."""

    def __init__(self, name, price_per_kg):
        self.name = name
        self.price_per_kg = price_per_kg

    def __str__(self):
        return f"{self.name.title()} - ${self.price_per_kg:.2f} per kg"


class FruitStore:
    """Represents the Fruit Store logic and inventory."""

    def __init__(self):
        self.inventory = {
            "apple": Fruit("apple", 3.50),
            "banana": Fruit("banana", 1.20),
            "orange": Fruit("orange", 2.00),
            "mango": Fruit("mango", 4.00)
        }
        self.cart = {}

    def display_fruits(self):
        print("\nAvailable Fruits:")
        for fruit in self.inventory.values():
            print(f"- {fruit}")

    def add_to_cart(self, fruit_name, quantity_kg):
        fruit_name = fruit_name.lower()
        if fruit_name in self.inventory:
            if fruit_name in self.cart:
                self.cart[fruit_name] += quantity_kg
            else:
                self.cart[fruit_name] = quantity_kg
            print(f"{quantity_kg} kg of {fruit_name.title()} added to cart.")
        else:
            print("Sorry, that fruit is not available.")

    def view_cart(self):
        if not self.cart:
            print("\nCart is empty.")
            return

        print("\nYour Cart:")
        total = 0
        for name, qty in self.cart.items():
            fruit = self.inventory[name]
            cost = qty * fruit.price_per_kg
            total += cost
            print(f"{qty} kg of {name.title()} - ${cost:.2f}")
        print(f"Total: ${total:.2f}")

    def checkout(self):
        if not self.cart:
            print("\nNothing to checkout.")
            return

        self.view_cart()
        confirm = input("\nProceed to checkout? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Thank you for shopping with us!")
            self.cart.clear()
        else:
            print("Checkout cancelled.")


def main():
    store = FruitStore()

    while True:
        print("\n=== Fruit Store Menu ===")
        print("1. Display Fruits")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            store.display_fruits()
        elif choice == '2':
            fruit_name = input("Enter fruit name: ")
            try:
                quantity = float(input("Enter quantity in kg: "))
                if quantity <= 0:
                    raise ValueError
                store.add_to_cart(fruit_name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a positive number.")
        elif choice == '3':
            store.view_cart()
        elif choice == '4':
            store.checkout()
        elif choice == '5':
            print("Exiting the store. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
