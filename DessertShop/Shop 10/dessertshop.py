from dessert import DessertShop, Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt
from collections import defaultdict
import itertools
from typing import List, Tuple

class Customer:
    id_iter = itertools.count(10000)

    def __init__(self, customer_name: str):
        self.customer_name = str(customer_name)
        self.order_history: List[Order] = []
        self.customer_id: int = next(Customer.id_iter)

    def add2history(self, order: Order) -> 'Customer':
        self.order_history.append(order)
        return self

def get_item_key(item) -> Tuple:
    if isinstance(item, Candy):
        return ('Candy', item.name, item.price_per_pound)
    elif isinstance(item, Cookie):
        return ('Cookie', item.name, item.price_per_dozen)
    elif isinstance(item, IceCream):
        if isinstance(item, Sundae):
            return ('Sundae', item.name, item.price_per_scoop, item.topping_name, item.topping_price)
        return ('IceCream', item.name, item.price_per_scoop)
    else:
        return (type(item).__name__, item.name)

def process_order(shop: DessertShop) -> Order:
    order = Order()

    done: bool = False
    prompt = '\n'.join(['\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sundae',
            '5: View the current order',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])

    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':            
                item = shop.user_prompt_candy()
                order.add(item)
                print(item)
            case '2':            
                item = shop.user_prompt_cookie()
                order.add(item)
                print(item)
            case '3':            
                item = shop.user_prompt_icecream()
                order.add(item)
                print(item)
            case '4':            
                item = shop.user_prompt_sundae()
                order.add(item)
                print(item)
            case '5':
                for item in order:
                    print(item)
            case _:            
                print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
    
    order.sort()
    order.set_pay_type(shop.payment_method())
    return order

def print_receipt(order: Order):
    # Group similar items
    merged_items = defaultdict(list)
    for item in order:
        key = get_item_key(item)
        merged_items[key].append(item)
  
    # Outputs the receipt info to the terminal interface
    print(receipt_header(79))

    for key, items in merged_items.items():
        item = items[0]  # Take the first item as a representative
        print(f"{item.name} ({item.packaging})")
        
        total_cost = sum(i.calculate_cost() for i in items)
        total_tax = sum(i.calculate_tax() for i in items)
        part_2 = f"${total_cost:.2f}"
        part_3 = f"[Tax: ${total_tax:.2f}]"
        
        if isinstance(item, Candy):
            total_weight = sum(i.candy_weight for i in items)
            part_1 = f"\t{total_weight:.2f} lbs. @ ${item.price_per_pound}/lb.:"
        elif isinstance(item, Cookie):
            total_quantity = sum(i.cookie_quantity for i in items)
            part_1 = f"\t{total_quantity} cookies @ ${item.price_per_dozen}/dozen:"
        elif isinstance(item, IceCream) and not isinstance(item, Sundae):
            total_scoops = sum(i.scoop_count for i in items)
            part_1 = f"\t{total_scoops} scoops @ ${item.price_per_scoop}/scoop:"
        elif isinstance(item, Sundae):
            total_scoops = sum(i.scoop_count for i in items)
            print(f"\t{total_scoops} scoops @ ${item.price_per_scoop}/scoop")
            part_1 = f"{item.topping_name} @ ${item.topping_price}:"
        
        spacer = 62 - (len(part_1) + len(part_2) + len(part_3))
        print(part_1 + " " * spacer + part_2 + " " * 11 + part_3)
        
    print("-" * 79)
    print(f"Total number of items in order: {len(order)}")

    subtotal = f"${order.order_cost():.2f}"
    tax = f"[Tax: ${order.order_tax():.2f}]"
    order_total = f"${order.order_cost() + order.order_tax():.2f}"
    spacer = 53 - (len(subtotal) + len(tax))

    print("Order Subtotals:" + " " * spacer + subtotal + " " * 11 + tax)
    print("Order Total:" + " " * (67 - len(order_total)) + order_total)
    print("-" * 79)
    print(f"Paid with {order.pay_method}")

def generate_receipt_pdf(order: Order):
    receipt_list = [["Name", "Packaging", "Quantity", "Unit Price", "Cost", "Tax"]]

    merged_items = defaultdict(list)
    for item in order:
        key = get_item_key(item)
        merged_items[key].append(item)

    for key, items in merged_items.items():
        item = items[0]  # Take the first item as a representative
        if isinstance(item, Candy):
            total_weight = sum(i.candy_weight for i in items)
            cost = sum(i.calculate_cost() for i in items)
            tax = sum(i.calculate_tax() for i in items)
            receipt_list.append([f"{item.name}", "Bag", f"{total_weight:.2f} lbs", f"${item.price_per_pound:.2f}/lb", f"${cost:.2f}", f"${tax:.2f}"])
        elif isinstance(item, Cookie):
            total_quantity = sum(i.cookie_quantity for i in items)
            cost = sum(i.calculate_cost() for i in items)
            tax = sum(i.calculate_tax() for i in items)
            receipt_list.append([f"{item.name}", "Box", f"{total_quantity}", f"${item.price_per_dozen:.2f}/dozen", f"${cost:.2f}", f"${tax:.2f}"])
        elif isinstance(item, IceCream):
            cost = sum(i.calculate_cost() for i in items)
            tax = sum(i.calculate_tax() for i in items)
            total_scoops = sum(i.scoop_count for i in items)
            receipt_list.append([f"{item.name}", f"{item.packaging}", f"{total_scoops} scoops", f"${item.price_per_scoop:.2f}/scoop", f"${cost:.2f}", f"${tax:.2f}"])
            if isinstance(item, Sundae):
                receipt_list.append([f"{item.topping_name}", "", "", "", f"${item.topping_price:.2f}", ""])

    # Calculate totals
    order_sub = sum(item.calculate_cost() for item in order)
    order_tax = sum(item.calculate_tax() for item in order)
    order_total = order_sub + order_tax

    # Add totals to receipt
    receipt_list.extend([
        [""],
        ["Order Subtotals", "", "", "", f"${order_sub:.2f}", f"${order_tax:.2f}"],
        ["Order Total", "", "", "", f"${order_total:.2f}"],
        [""],
        ["Total number of items in the order", "", f"{len(order)}"],
        ["Paid with", "", f"{order.get_pay_type()}"]
    ])

    make_receipt(receipt_list, "receipt.pdf")

def main():
    shop = DessertShop()
    
    while True:
        order = process_order(shop)
        print_receipt(order)
        generate_receipt_pdf(order)
        
        another_order = input("\nWould you like to start another order? (y/n): ").lower().strip()
        if another_order != 'y':
            break

    print("Thank you for using the Dessert Shop!")

def receipt_header(width: int) -> str:
    spacer = int((width / 2) - 3)
    header = "-" * spacer + "Receipt" + "-" * spacer
    return header

if __name__ == "__main__":
    main()