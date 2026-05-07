from product import Product
from storage import Storage 


class ProductManager:
    def __init__(self):
        self.storage = Storage("products.json")
        self.products =  self.storage.load()
        self.session_products = []

    def add_product(self, product: Product):

        product_dict = product.to_dict()

        self.session_products.append(product_dict)
        self.products.append(product_dict)

        self.storage.save(self.products)

        return product_dict
    
    def view_my_products(self):
        return self.session_products

    def view_all_products(self):
        return self.products
    
    def search_products(self, keyword):
        keyword = keyword.lower()
        results = []
        for p in self.products:
            if (keyword in p['name'].lower()):
                results.append(p)
        return results
    
    def find_exchange_matches(self, my_product):

        category_map = {
            "phone":["electronics"],
            "laptop": ["electronics"],
            "electronics": ["phone", "laptop"],
            "bike": ["car"],
            "car": ["bike"],

        }

        matches = []

        for p in self.products:

            if p["id"] == my_product["id"]:
               continue
            score = 0

        # category match
            if p["category"].lower() == my_product["category"].lower():
                score += 40
            elif my_product["category"].lower() in category_map:
                if p["category"].lower() in category_map[my_product["category"].lower()]:
                    score +=25

        # price similarity
            price_diff = abs(p["price"] - my_product["price"])
            price_limit = my_product["price"] * 0.2

            if price_diff <= price_limit:
                score +=40

            if p["condition"].lower() == my_product["condition"].lower():
                score +=20

            if score > 0:
                matches.append((score, p))

        matches.sort(reverse=True, key=lambda x:x[0])
        return matches
                

        