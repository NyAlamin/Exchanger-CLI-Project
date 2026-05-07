from product_manager import ProductManager
from product import Product

class CLI:

    def __init__(self):
        self.manager = ProductManager()
        
    def print_menu(self):
        print("================================")
        print("       EXCHANGER PLATFORM       ")
        print("    Second Hand Marketplace     ")
        print("================================")
        print("1. Add Product")
        print("2. View My Products")
        print("3. Update Product Price")
        print("4. Find Exchange Matches")
        print("5. View All Products")
        print("6. Search Products")
        print("7. Delete Product")
        print("8. Summary Report")
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
        # print("Your Product Details:")
        # print(f"ID: {added_product['id']}")
        # print(f"Name: {added_product['name']}")
        # print(f"Category: {added_product['category']}")
        # print(f"Price: {added_product['price']}")
        # print(f"Condition: {added_product['condition']}")
        # print(f"Description: {added_product['description']}")

    def view_my_products(self):
        my_products = self.manager.view_my_products()

        if not my_products:
            print("You have no products listed.")
            return

        print("Your Products:")
        for p in my_products:
            print(f"ID: {p['id']}")
            print(f"Name: {p['name']}")
            print(f"Category: {p['category']}")
            print(f"Price: {p['price']}")
            print(f"Condition: {p['condition']}")
            print(f"Description: {p['description']}")
            print("================================")

    def view_products(self):

        products = self.manager.view_all_products()

        if not products:
            print("No products found.")
            return

        for p in products:
            print(p)

    def search_products(self):
        keyword = input("Enter keyword to search: ")
        results = self.manager.search_products(keyword)

        if not results:
            print("No products found matching the keyword.")
            return

        for p in results:
            print(p)

    def exchange_matches(self):
        if not self.manager.session_products:
            print("You have no products listed to find matches for.")
            return
        print("Your Products:")
        for p in self.manager.session_products:
            print(f"ID: {p['id']}")
            print(f"Name: {p['name']}")
            print(f"Category: {p['category']}")
            print(f"Price: {p['price']}")
            print(f"Condition: {p['condition']}")
            print(f"Description: {p['description']}")
            print("================================")


        pid= input("Enter your product ID to find exchange matches: ")
        my_product = None

        for p in self.manager.session_products:
            if p["id"] == pid:
                my_product = p
                break
        if not my_product:
            print("Product not found.")
            return
        matches = self.manager.find_exchange_matches(my_product)

        if not matches:
            print("No exchange matches found.")
            return
        
        for p in matches:
            print(f"Match Score: {p[0]}%")
            print(f"ID: {p[1]['id']}")
            print(f"Name: {p[1]['name']}")
            print(f"Category: {p[1]['category']}")
            print(f"Price: {p[1]['price']}")
            print(f"Condition: {p[1]['condition']}")
            print(f"Description: {p[1]['description']}")
            print("================================")


        
    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_product()

            elif choice == "2":
                self.view_my_products()

            elif choice == "4":
                self.exchange_matches()

            elif choice == "5":
                self.view_products()

            elif choice == "6":
                self.search_products()
            
            
            
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


