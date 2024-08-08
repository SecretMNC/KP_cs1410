class DessertItem:
    def __init__(self, name: str='') -> None:
        self.name = str(name)

class Candy(DessertItem):
    def __init__(self, name='', candy_weight: float=0.0, price_per_pound: float=0.0) -> None:
        super().__init__(name)
        self.name = str(name)
        self.candy_weight = float(candy_weight)
        self.price_per_pound = float(price_per_pound)

class Cookie(DessertItem):
    def __init__(self, name='', coookie_quantity: int=0, price_per_dozen: float=0.0) -> None:
        super().__init__(name)
        self.name = str(name)
        self.coookie_quantity = int(coookie_quantity)
        self.price_per_dozen = float(price_per_dozen)

class IceCream(DessertItem):
    def __init__(self, name='', scoop_count: int=0, price_per_scoop: float=0.0) -> None:
        super().__init__(name)
        self.name = str(name)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)

class Sundae(IceCream):
    def __init__(self, name='', scoop_count: int=0, price_per_scoop: float=0.0, topping_name: str='', topping_price: float=0.0) -> None:
        super().__init__(name, scoop_count, price_per_scoop)
        self.name = str(name)
        self.scoop_count = int(scoop_count)
        self.price_per_scoop = float(price_per_scoop)
        self.topping_name = str(topping_name)
        self.topping_price = float(topping_price)

    def __str__(self) -> str:
        return f'{self.name}, {self.scoop_count}, {self.price_per_scoop}, {self.topping_name}, {self.topping_price}'

sundae = Sundae("Hot Fudge", 1, 3, "Fudge", 2)

print(sundae)
