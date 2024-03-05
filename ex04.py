'''Create a class called Restaurant with the attributes name, category, asset and create 2 more attributes.'''

class Restaurant:
    def __init__(self, name, category, asset=False, capacity, grade):
        self.name = name
        self.category = category
        self.asset = asset
        self.capacity = capacity
        
