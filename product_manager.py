from product import Product
from storage import Storage 

class ProductManager:
    def __init__(self):
        self.storage = Storage("products.json")
        self.products =  self.storage.load()

    def add_product(self, product: Product):

        product_dict = product.to_dict()
        self.products.append(product_dict)
        self.storage.save(self.products)
        return product_dict
    
    def find_exchange_matches(self, product_id):
        pass

        