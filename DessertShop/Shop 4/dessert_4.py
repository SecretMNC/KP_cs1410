from abc import ABC
from abc import abstractmethod

class DessertShop:
    # User interface for entering in order data

    @staticmethod
    def user_prompt_candy() -> object:
        # Prompts user to enter data for a candy order. Validates entries.

        while True:
            try:
                name = input("What's the name of the candy?\n-->")
                weight = input("What's the weight of the candy in pounds?\n-->")
                price = input("What's the price of the candy per pound?\n-->")
                if name.isdigit():
                    raise ValueError("Make sure name only has letters.")
                f_weight = float(weight)
                f_price = float(price)
            except ValueError as err:
                if name.isdigit():
                    print(err)
                else:
                    print("Make sure the weight of candy and price are only numbers.")
                print("Please try again.\n")
                continue
            else:
                candy = Candy(name, f_weight, f_price)
                return candy

    @staticmethod
    def user_prompt_cookie() -> object:
        # Prompts user to enter data for a cookie order. Validates entries.

        while True:
            try:
                name = input("What's the name of the cookie?\n-->")
                qty = input("How many cookies are there?\n-->")
                price = input("What's the price of the cookies per dozen?\n-->")
                if name.isdigit():
                    raise ValueError("Make sure name only has letters.")
                elif not qty.isdigit() or int(qty) <= 0:
                    raise ValueError("Make sure the number of cookies is a whole number.")
                f_price = float(price)
            except ValueError as err:
                if name.isdigit():
                    print(err)
                else:
                    print("Make sure price only contains numbers.")
                print("Please try again.\n")
                continue
            else:
                cookie = Cookie(name, int(qty), f_price)
                return cookie

    @staticmethod
    def user_prompt_icecream() -> object:
        # Prompts user to enter data for an ice cream order. Validates entries.

        while True:
            try:
                name = input("What's the name of the ice cream?\n-->")
                scoops = input("How many scoops are there?\n-->")
                price = input("What's the price per scoop?\n-->")
                if name.isdigit():
                    raise ValueError("Make sure name only has letters.")
                elif not scoops.isdigit() or int(scoops) <= 0:
                    raise ValueError("Make sure scoops is a whole number.")
                f_price = float(price)
            except ValueError as err:
                if name.isdigit():
                    print(err)
                else:
                    print("Price must only contain numbers")
                print("Please try again.\n")
                continue
            else:
                icecream = IceCream(name, int(scoops), f_price)
                return icecream

    @staticmethod
    def user_prompt_sundae() -> object:
        # Prompts user to enter data for a sundae order. Validates entries.

        while True:
            try:
                name = input("What's the name of the sundae?\n-->")
                scoops = input("How many scoops are there?\n-->")
                price = input("What's the price per scoop?\n-->")
                topping = input("What's the name of the topping?\n-->")
                topping_price = input("What's the price of the topping?\n-->")
                if name.isdigit() or topping.isdigit():
                    raise ValueError("Make sure name and topping are only letters.")
                elif not scoops.isdigit() or int(scoops) <= 0:
                    raise ValueError("Make sure scoops is a whole number.")
                f_price = float(price)
                f_topping_price = float(topping_price)
            except ValueError as err:
                if name.isdigit() or topping.isdigit():
                    print(err)
                else:
                    print("Price or topping price must contain only numbers.")
                print("Please try again.\n")
                continue
            else:
                sundae = Sundae(name, int(scoops), f_price, topping, f_topping_price)
                return sundae

class DessertItem(ABC):
    def __init__(self, name: str='', tax_percent: float=7.25):
        self.name = str(name)
        self.tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self) -> float:
        return 0

    def calculate_tax(self) -> float:
        return round(self.calculate_cost() * (self.tax_percent * 0.01), 2)

class Candy(DessertItem):
    def __init__(self, name='', candy_weight=0.0, price_per_pound=0.0):
        super().__init__(name)
        self.name = str(name)
        self.candy_weight = float(candy_weight)
        self.price_per_pound = float(price_per_pound)

    def calculate_cost(self) -> float:
        return round(self.candy_weight * self.price_per_pound, 2)

class Cookie(DessertItem):
    def __init__(self, name='', cookie_quantity=0, price_per_dozen=0.0):
        super().__init__(name)
        self.name = str(name)
        self.cookie_quantity = int(cookie_quantity)
        self.price_per_dozen = float(price_per_dozen)

    def calculate_cost(self) -> float:
        return round(self.cookie_quantity / 12 * self.price_per_dozen, 2)

class IceCream(DessertItem):
    def __init__(self, name='', scoop_count=0, price_per_scoop=0.0):
        super().__init__(name)
        self.name = str(name)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)

    def calculate_cost(self) -> float:
        return round(self.scoop_count * self.price_per_scoop, 2)

class Sundae(IceCream):
    def __init__(self, name='', scoop_count=0, price_per_scoop=0.0, topping_name='', topping_price=0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.name = str(name)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)
        self.topping_name = str(topping_name)
        self.topping_price = float(topping_price)

    def calculate_cost(self) -> float:
        return round(self.scoop_count * self.price_per_scoop + self.topping_price, 2)

class Order:
    def __init__(self, order: list[DessertItem]=None):
        if order is None:
              self.order = []
        else:
              self.order = order

    def add(self, item: DessertItem) -> None:
        # Appends item parameter into the order list
        self.order.append(item)

    def order_cost(self) -> float:
        # Returns the cost of all items in the order list
        subtotal = 0
        for item in self.order:
            subtotal += item.calculate_cost()
        return round(subtotal, 2)
            
    def order_tax(self) -> float:
        # Returns the total tax for all items in the order list
        tax = 0
        for item in self.order:
            tax += item.calculate_tax()
        return round(tax, 2)

    def __len__(self) -> int:
        # Returns the number of items in the order list
        return len(self.order)

    def __iter__(self) -> None:
        # Returns an iterable of the order instance variable
        return iter(self.order)
