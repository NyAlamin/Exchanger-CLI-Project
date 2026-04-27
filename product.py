class Product:
    def __init__(self, pid, name, category, price, condition, description):
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price
        self.condition = condition
        self.description = description

    def to_dict(self):
        return {
            "id": self.pid,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "condition": self.condition,
            "description": self.description
        }
    






    

    # def __str__(self):
    #     return  f"ID: {self.pid}, Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, Condition: {self.condition}, Description: {self.description}"