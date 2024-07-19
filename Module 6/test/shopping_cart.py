class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f"{self.name}: ${self.price}"

def test_function():
    return f"This is a test fuction from product module"


class ShoppingCart:
    order_id = 1000

    def __init__(self):
        self.cart = []
        self.order_id = ShoppingCart.order_id
        ShoppingCart.order_id += 1  

    def add_item(self, product):
        self.cart.append(product)

    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += item.price 
        return total
    
    def remove_item(self, item):
        for product in self.cart:
            if product.name == item:
                self.cart.remove(product)

    def display(self):
        for product in self.cart:
            print(product.name, product.price)


product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 20)

cart1 = ShoppingCart()
cart1.add_item(product1)
cart1.add_item(product2)

# Display the items and total along with the order ID
print(f"Order ID: {cart1.order_id}")
for item in cart1.cart:
    print(item.display())

print(f"Total: ${cart1.calculate_total()}")

# Creating another shopping cart
product3 = Product("Headphones", 50)

cart2 = ShoppingCart()
cart2.add_item(product3)

# Display the items and total along with the order ID for the second cart
print(f"\nOrder ID: {cart2.order_id}")
for item in cart2.cart:
    print(item.display())

print(f"Total: ${cart2.calculate_total()}")

cart1.remove_item('Mouse')
