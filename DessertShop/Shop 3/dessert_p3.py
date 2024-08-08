from abc import ABC
from abc import abstractmethod

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
