class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class ShoppingCart:
    order_id = 1000
    
    def __init__(self):
        self.list = []
        self.order_num = ShoppingCart.order_id
        ShoppingCart.order_id += 1
        
    def add_item(self, product):
        self.list.append(product)
    
    def calculate_price(self):
        total = 0
        for product in self.item:
            total += product.price
            
sc1 = ShoppingCart()
sc2 = ShoppingCart()

print(sc1.order_num, sc2.order_num)