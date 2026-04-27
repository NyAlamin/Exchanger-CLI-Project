from product import Product
from storage import Storage 
import pandas as pd   


class ProductManager:
    def __init__(self):
        self.storage = Storage("products.json")
        self.products =  self.storage.load()

    def add_product(self, product: Product):

        product_dict = product.to_dict()
        self.products.append(product_dict)
        self.storage.save(self.products)
        return product_dict
    
    def view_all_products(self):
        return self.products
    def search_products(self, keyword):
        keyword = keyword.lower()
        results = []
        for p in self.products:
            if (keyword in p['name'].lower()):
                results.append(p)
        return results
    


def find_exchange_matches(self, product_id):
        pass


        