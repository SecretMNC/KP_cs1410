from dessert import Candy, Cookie, IceCream, Sundae, Order

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

      for item in new_order.order:
            print(item.name)

      print(f"Total number of items in order: {len(new_order)}")

if __name__ == "__main__":
      main()
