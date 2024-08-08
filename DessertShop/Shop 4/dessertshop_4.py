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
          print(f'{item.name} has been added to your order.')
        case '2':            
          item = shop.user_prompt_cookie()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '3':            
          item = shop.user_prompt_icecream()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '4':            
          item = shop.user_prompt_sundae()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
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

    order_sub = order.order_cost()
    order_tax = order.order_tax()
    order_total = order_sub + order_tax
    receipt_list = []

    receipt_list.append(["Name", "Item Cost", "Tax"])

    for item in order:
        name = item.name
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        receipt_list.append([name, f"${cost:.2f}", f"${tax:.2f}"])

    receipt_list.append(["Order Subtotals", f"${order_sub:.2f}", f"${order_tax:.2f}"])
    receipt_list.append(["Order Total", "", f"${order_total:.2f}"])
    receipt_list.append(["Total items in the order", "", len(order)])

    make_receipt(receipt_list, "receipt.pdf")

if __name__ == "__main__":
      main()
