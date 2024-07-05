import time
from itertools import groupby

class ShoppingCart:
    '''Define the ShoppingCart class'''

    order_id_num = 10000

    def __init__(self, first_name, last_name, date, cart=[], order_id=order_id_num) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.date: str = date
        self.cart: list = cart
        self.order_id: int = order_id

        self.update_order_id()

    def add_items(self, item, qty):
        for ele in range(qty):
            self.cart.append(item)

    def remove_items(self, item):
        while True:
            if item in self.cart:
                item_index = self.cart.index(item)
            else:
                break
            if item in self.cart:
                self.cart.pop(item_index)

    def modify_items(self, item, qty):
        item_qty = 0
        for ele in self.cart:
            if ele == item:
                item_qty += 1
        if qty > item_qty:
            add_num = qty - item_qty
            print(add_num)
            for ele in range(add_num):
                self.cart.append(item)
        elif qty < item_qty:
            sub_num = item_qty - qty
            print(sub_num)
            item_index = self.cart.index(item)
            for ele in range(sub_num):
                self.cart.pop(item_index)

    def get_cart(self):
        return self.cart
    
    def get_id(self):
        return self.order_id
    
    @classmethod
    def update_order_id(cls):
        cls.order_id_num += 1

cart1 = ShoppingCart('Kevin', 'Pett', time.localtime())
cart1.add_items('chocolate', 5)
print(cart1.get_cart())
cart1.modify_items('chocolate', 3)
print(cart1.get_cart())
cart1.remove_items('chocolate')
print(cart1.get_cart())
cart2 = ShoppingCart('Kevin', 'Jeffrey', time.localtime())

print(cart1.get_id(),cart2.get_id())