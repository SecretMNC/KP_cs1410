from packaging import Packaging
from payable import Payable, PayType
from abc import abstractmethod

class DessertShop():
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

    @staticmethod
    def payment_method() -> PayType:
        while True:
            try:
                pay_type = input("\n1: Cash\n2: Card\n3: Phone\nEnter payment method: ").upper()
                if pay_type not in ["CASH", "CARD", "PHONE"]:
                    raise ValueError("Please type only type cash, card, or phone.")
            except ValueError as err:
                print(err)
                continue
            else:
                return pay_type

class DessertItem(Packaging):
    # Of the Packaging Protocol, contains abstractmethod calculate_cost and concrete method calculate_tax

    def __init__(self, name: str='', tax_percent: float=7.25):
        self.name = str(name)
        self.tax_percent = tax_percent
        self.packaging: str = None

    @abstractmethod
    def calculate_cost(self) -> float:
        # Abstract class intended to return the cost of the item
        return 0

    def calculate_tax(self) -> float:
        # Returns the tax of the item object
        return round(self.calculate_cost() * (self.tax_percent * 0.01), 2)

    def __eq__(self, other: object) -> bool:
        return self.calculate_cost() == other.calculate_cost()

    def __ne__(self, other: object) -> bool:
        return self.calculate_cost() != other.calculate_cost()

    def __lt__(self, other: object) -> bool:
        return self.calculate_cost() < other.calculate_cost()

    def __gt__(self, other: object) -> bool:
        return self.calculate_cost() > other.calculate_cost()

    def __ge__(self, other: object) -> bool:
        return self.calculate_cost() >= other.calculate_cost()

    def __le__(self, other: object) -> bool:
        return self.calculate_cost() <= other.calculate_cost()


class Candy(DessertItem):
    def __init__(self, name='', candy_weight=0.0, price_per_pound=0.0):
        super().__init__(name)
        self.name = str(name)
        self.candy_weight = float(candy_weight)
        self.price_per_pound = float(price_per_pound)
        self.packaging: str = "Bag"

    def calculate_cost(self) -> float:
        # Returns the cost of the item object, before tax
        return round(self.candy_weight * self.price_per_pound, 2)
      
    def __str__(self):
        # Returns the name, quantity, price per unit, cost, and tax 
        return f"{self.name}, {self.candy_weight}lbs, ${self.price_per_pound}/lb, ${self.calculate_cost()} {self.calculate_tax()}"

class Cookie(DessertItem):
    def __init__(self, name='', cookie_quantity=0, price_per_dozen=0.0):
        super().__init__(name)
        self.name = str(name)
        self.cookie_quantity = int(cookie_quantity)
        self.price_per_dozen = float(price_per_dozen)
        self.packaging: str = "Box"

    def calculate_cost(self) -> float:
        # Returns the cost of the item object, before tax
        return round(self.cookie_quantity / 12 * self.price_per_dozen, 2)

    def __str__(self):
        # Returns the name, quantity, price per unit, cost, and tax 
        return f"{self.name}, {self.cookie_quantity}, ${self.price_per_dozen}/dozen, ${self.calculate_cost()}, {self.calculate_tax()}"

class IceCream(DessertItem):
    def __init__(self, name='', scoop_count=0, price_per_scoop=0.0):
        super().__init__(name)
        self.name = str(name)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)
        self.packaging: str = "Bowl"

    def calculate_cost(self) -> float:
        # Returns the cost of the item object, before tax
        return round(self.scoop_count * self.price_per_scoop, 2)

    def __str__(self):
        # Returns the name, quantity, price per unit, cost, and tax 
        return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoops, ${self.calculate_cost()}, {self.calculate_tax()}"

class Sundae(IceCream):
    def __init__(self, name='', scoop_count=0, price_per_scoop=0.0, topping_name='', topping_price=0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.name = str(name)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)
        self.topping_name = str(topping_name)
        self.topping_price = float(topping_price)
        self.packaging: str = "Boat"

    def calculate_cost(self) -> float:
        # Returns the cost of the item object, before tax
        return round(self.scoop_count * self.price_per_scoop + self.topping_price, 2)

    def __str__(self):
        # Returns the name, quantity, price per unit, topping name, topping cost, total cost, and tax 
        return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoops, {self.topping_name}, ${self.topping_price}, ${self.calculate_cost()}, {self.calculate_tax()}"


class Order(Payable):
    def __init__(self, order: list[DessertItem]=None):
        if order is None:
              self.order = []
        else:
              self.order = order
        self.pay_method = "CASH"

    def sort(self) -> None:
        # Bubblesort algorithm to sort order list in ascending order

        prev_item = self.order[0]
        for num, item in enumerate(self.order):  # Iterate list, swapping misordered objects
            if prev_item > item:
                prev_index = self.order.index(prev_item)
                index = self.order.index(item)
                self.order.insert(prev_index, self.order[num])
                del self.order[index + 1]

            prev_item = item  # Setting prev_item as the item that was just iterated with

        prev_item = self.order[0]
        for item in self.order:  # Check if list is ascending, if not, do again
            if prev_item <= item:  # If all items pass through here, the sort ends
                prev_item = item
            elif prev_item > item:
                self.sort()
                

    def get_pay_type(self) -> PayType:
        # Returns the current payment method for this order

        if self.pay_method not in ["CASH", "CARD", "PHONE"]:
            raise ValueError("Payment method is currently NOT valid!")
        else:
            return self.pay_method

    def set_pay_type(self, payment_method: PayType) -> None:
        # Change the payment method of the order to Cash, Card, or Phone

        if payment_method not in ["CASH", "CARD", "PHONE"]:
            raise ValueError("Must be either 'CASH', 'CARD', or 'PHONE'.")
        else:
            self.pay_method = payment_method

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

    def __str__(self) -> str:
        # Returns the name, quantity, price per unit, cost, and tax of all items in the order
        return f"""{list(self.order)}
        Paid with {self.pay_method}"""
