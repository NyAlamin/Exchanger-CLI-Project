class Product:
    def __init__(self, pid, name, category, price, condition, description):
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price
        self.condition = condition
        self.description = description

    def __str__(self):
        return {
            "id": self.pid,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "condition": self.condition,
            "description": self.description
        }