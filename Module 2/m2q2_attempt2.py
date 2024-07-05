class ShoppingCart:
    order_id = 10000
    
    def __init__(self, first_name, last_name, order_number=order_id):
        self.first_name = first_name
        self.last_name = last_name
        self.date = 'today'
        self.cart = []
        self.order_number = order_number
        
    @classmethod
    def update_order_num(cls):
        cls.order_id += 1
        
    def add_item(self, item):
        if item not in self.cart:
            self.cart.append(item)
        else:
            print(f'The item {item} is already in the cart.')

    def remove_item(self, item):
        self.cart.remove(item)
    
    def modify_cart(self, item, qty):
        current_qty = 0
        for ele in self.cart:
            if ele == item:
                current_qty += 1
        if current_qty - qty >= 0:
            for num in range(qty):
                self.cart.remove(item)
        else:
            for num in range(current_qty):
                self.cart.remove(item)
    
    def view_cart(self):
        print('Items in your cart:')
        for item in self.cart:
            print(f'--> {item}')
        
first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')
items_list = ['computer', 'keyboard', 'mouse', 'monitor', 'speakers', 'chair', 'desk']
order_1 = ShoppingCart(first_name, last_name)

while True:
    to_do = input('''What would you like to do?
"1" for add item
"2" for remove item
"3" for modify item quantity
"4" for view items available for purchase
"5" to view the current cart\n''')
    if to_do == '1':
        print(f'Available items: \n --> {items_list}')
        new_item = input('What item would you like to add?')
        order_1.add_item(new_item) 
    elif to_do == '2':
        rm_item = input('Please enter the item you want to remove from cart:\n')
        order_1.remove_item(rm_item)
    elif to_do == '3':
        print("This doesn't do anything yet.")
    elif to_do == '4':
        print('Here are items available for purchase:\n')
        for item in items_list:
            print(f'--> {item}')
        input('Press enter to continue...')
    elif to_do == '5':
        print('Here is your current cart:\n')
    else:
        print('Please enter in a valid number')

