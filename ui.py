from product_manager import ProductManager
from product import Product

class CLI:

    def __init__(self):
        self.manager = ProductManager()
        
    def print_menu(self):
        print("\n------ Exchange Platform ------")
        print("1. Add Product")
        print("2. Find Exchange Matches")
        print("3. Search Products")
        print("4. View All Products")
        print("5. Update Product Price")
        print("6. Delete Product")
        print("0. Exit")

    def add_product(self):

        pid = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter product price: "))
        condition = input("Enter product condition (New/Used): ")
        description = input("Enter product description: ")

        p = Product(pid, name, category, price, condition, description)
        added_product = self.manager.add_product(p)

        print("\nProduct added successfully!")
        print("Your Product Details:")
        print(f"ID: {added_product['id']}")
        print(f"Name: {added_product['name']}")
        print(f"Category: {added_product['category']}")
        print(f"Price: {added_product['price']}")
        print(f"Condition: {added_product['condition']}")
        print(f"Description: {added_product['description']}")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_product()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


