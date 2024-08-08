from dessert import Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt

def main():
      # Manually tests object instantiation and method functionality
      new_order = Order()

      candy_corn = Candy("Candy Corn", 1.5, .25)
      gummy_bears = Candy("Gummy Bears", .25, .35)
      chocolate_chip = Cookie("Chocolate Chip", 6, 3.99)
      pistachio = IceCream("Pistachio", 2, .79)
      vanilla = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
      oatmeal_raisin = Cookie("Oatmeal Raisin", 2, 3.45)

      new_order.add(candy_corn)
      new_order.add(gummy_bears)
      new_order.add(chocolate_chip)
      new_order.add(pistachio)
      new_order.add(vanilla)
      new_order.add(oatmeal_raisin)

      order_sub = new_order.order_cost()
      order_tax = new_order.order_tax()
      order_total = order_sub + order_tax
      receipt_list = []

      receipt_list.append(["Name", "Item Cost", "Tax"])

      for item in new_order:
          name = item.name
          cost = item.calculate_cost()
          tax = item.calculate_tax()
          receipt_list.append([name, f"${cost:.2f}", f"${tax:.2f}"])

      receipt_list.append(["Order Subtotals", f"${order_sub:.2f}", f"${order_tax:.2f}"])
      receipt_list.append(["Order Total", "", f"${order_total:.2f}"])
      receipt_list.append(["Total items in the order", "", len(new_order)])

      make_receipt(receipt_list, "receipt.pdf")

if __name__ == "__main__":
      main()
