from dessert import DessertShop, Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt
from collections import defaultdict

'''
Code to implement the main loop of terminal-based user interface for
Dessert Shop Part 4. Students should be able to paste this code into their own 
main() method as-is and use it without change.

Author: George Rudolph
Date: 2 Jun 2023
'''
def main():
    shop = DessertShop()
    order = Order()

    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
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
          #print(f'{item.name} has been added to your order.')
          print(item)
        case '2':            
          item = shop.user_prompt_cookie()
          order.add(item)
          #print(f'{item.name} has been added to your order.')
          print(item)
        case '3':            
          item = shop.user_prompt_icecream()
          order.add(item)
          #print(f'{item.name} has been added to your order.')
          print(item)
        case '4':            
          item = shop.user_prompt_sundae()
          order.add(item)
          #print(f'{item.name} has been added to your order.')
          print(item)
        case '5':
          for item in order:
            print(item)
        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
    order.sort()
    order.set_pay_type(shop.payment_method())

    # Group similar items
    merged_items = defaultdict(list)
    for item in order:
        if isinstance(item, (Candy, Cookie)):
            key = (type(item), item.name, item.price_per_pound if isinstance(item, Candy) else item.price_per_dozen)
            merged_items[key].append(item)
        else:
            merged_items[item].append(item)
  
    # Outputs the receipt info to the terminal interface
    print(receipt_header(79))

    for item in order:
        print(f"{item.name} ({item.packaging})")
        part_2 = f"${item.calculate_cost():.2f}"
        part_3 = f"[Tax: ${item.calculate_tax():.2f}]"
        
        if isinstance(item, Candy):
            part_1 = f"\t{item.candy_weight} lbs. @ ${item.price_per_pound}/lb.:"
            spacer = 62 - (len(part_1) + len(part_2) + len(part_3))
            print(part_1 + " " * spacer + part_2 + " " * 11 + part_3)
        elif isinstance(item, Cookie):
            part_1 = f"\t{item.cookie_quantity} cookies @ ${item.price_per_dozen}/dozen:"
            spacer = 62 - (len(part_1) + len(part_2) + len(part_3))
            print(part_1 + " " * spacer + part_2 + " " * 11 + part_3)
        elif isinstance(item, IceCream) and not isinstance(item, Sundae):
            part_1 = f"\t{item.scoop_count} scoops @ ${item.price_per_scoop}/scoop:"
            spacer = 62 - (len(part_1) + len(part_2) + len(part_3))
            print(part_1 + " " * spacer + part_2 + " " * 11 + part_3)
        elif isinstance(item, Sundae):
            print(f"\t{item.scoop_count} scoops @ ${item.price_per_scoop}/scoop")
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

    # Outputs a receipt PDF file
    order_sub = order.order_cost()
    order_tax = order.order_tax()
    order_total = order_sub + order_tax
    receipt_list = []
    sundae_occurances = 0

    receipt_list.append(["Name", "Packaging", "Quantity", "Unit Price", "Cost", "Tax"])

    for key, items in merged_items.items():
        if isinstance(key, tuple):  # Merged Candy or Cookie
            item_type, name, unit_price = key
            if item_type == Candy:
                total_weight = sum(item.candy_weight for item in items)
                cost = sum(item.calculate_cost() for item in items)
                tax = sum(item.calculate_tax() for item in items)
                receipt_list.append([f"{name}", "Bag", f"{total_weight:.2f} lbs", f"${unit_price:.2f}/lb", f"${cost:.2f}", f"${tax:.2f}"])
            elif item_type == Cookie:
                total_quantity = sum(item.cookie_quantity for item in items)
                cost = sum(item.calculate_cost() for item in items)
                tax = sum(item.calculate_tax() for item in items)
                receipt_list.append([f"{name}", "Box", f"{total_quantity}", f"${unit_price:.2f}/dozen", f"${cost:.2f}", f"${tax:.2f}"])
        else:  # Single item (IceCream or Sundae)
            item = items[0]
            if isinstance(item, IceCream):
                receipt_list.append([f"{item.name}", f"{item.packaging}" f"{item.scoop_count} scoops", f"${item.price_per_scoop:.2f}/scoop", f"${item.calculate_cost():.2f}", f"${item.calculate_tax():.2f}"])
                if isinstance(item, Sundae):
                    receipt_list.append([f"{item.topping_name}", "", "", "", f"${item.topping_price:.2f}", ""])

    # Calculate totals
    order_sub = sum(item.calculate_cost() for item in order)
    order_tax = sum(item.calculate_tax() for item in order)
    order_total = order_sub + order_tax

    # Add totals to receipt
    receipt_list.append([""])
    receipt_list.append(["Order Subtotals", "", "", "", f"${order_sub:.2f}", f"${order_tax:.2f}"])
    receipt_list.append(["Order Total", "", "", "", f"${order_total:.2f}"])
    receipt_list.append([""])
    receipt_list.append(["Total number of items in the order", "", f"{len(order)}"])
    receipt_list.append(["Paid with", "", f"{order.get_pay_type()}"])

    make_receipt(receipt_list, "receipt.pdf")

def receipt_header(width: int) -> str:
    # Programmatically adds the "---Receipt---" header to stretch the width of the receipt print
    spacer = int((width / 2) - 3)
    header = "-" * spacer + "Receipt" + "-" * spacer

    return header

if __name__ == "__main__":
      main()
