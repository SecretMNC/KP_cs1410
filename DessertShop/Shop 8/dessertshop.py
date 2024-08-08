from dessert import DessertShop, Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt

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
    print()
  #
  #add your code below here to print the PDF receipt as the last thing in main()
  #
    '''
    candy_corn = Candy("Candy Corn", 1.5, .25)
    gummy_bears = Candy("Gummy Bears", .25, .35)
    chocolate_chip = Cookie("Chocolate Chip", 6, 3.99)
    pistachio = IceCream("Pistachio", 2, .79)
    vanilla = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    oatmeal_raisin = Cookie("Oatmeal Raisin", 2, 3.45)
    
    order.add(candy_corn)
    order.add(gummy_bears)
    order.add(chocolate_chip)
    order.add(pistachio)
    order.add(vanilla)
    order.add(oatmeal_raisin)
    '''
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

    for item in order:
        name = item.name
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        if isinstance(item, Candy):
            qty = item.candy_weight
            unit_price = item.price_per_pound
            receipt_list.append([name, item.packaging, f"{qty}lbs", f"${unit_price}/lb", f"${cost:.2f}", f"${tax:.2f}"])
        elif isinstance(item, Cookie):
            qty = item.cookie_quantity
            unit_price = item.price_per_dozen
            receipt_list.append([name, item.packaging, f"{qty}", f"${unit_price}/doz", f"${cost:.2f}", f"${tax:.2f}"])
        elif isinstance(item, IceCream):
            qty = item.scoop_count
            unit_price = item.price_per_scoop
            if isinstance(item, Sundae):
                receipt_list.append([name, item.packaging, f"{qty} scoops", f"${unit_price}/scoop", f"${cost:.2f}", f"${tax:.2f}"])
                receipt_list.append([item.topping_name, "", "", "", f"${item.topping_price:.2f}"])
                sundae_occurances += 1
            else:
                receipt_list.append([name, item.packaging, f"{qty} scoops", f"${unit_price}/scoop", f"${cost:.2f}", f"${tax:.2f}"])

    receipt_list.append(["Order Subtotals", "", "", "", f"${order_sub:.2f}", f"${order_tax:.2f}"])
    receipt_list.append(["Order Total", "", "", "", f"${order_total:.2f}"])
    receipt_list.append(["Total items in the order", "", len(order)])
    receipt_list.append([f"Paid with {order.get_pay_type()}", "", order.pay_method])

    # order_length = len(order) + sundae_occurances # Used if the receipt grid needs to be formatted

    make_receipt(receipt_list, "receipt.pdf")

def receipt_header(width: int) -> str:
    # Programmatically adds the "---Receipt---" header to stretch the width of the receipt print
    spacer = int((width / 2) - 3)
    header = "-" * spacer + "Receipt" + "-" * spacer

    return header

if __name__ == "__main__":
      main()
