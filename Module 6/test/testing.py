import unittest
from shopping_cart import ShoppingCart, Product

class TestShoppingCart(unittest.TestCase):
    def test_calculate_total(self):
        self.product1 = Product('computer', 1000)
        self.product2 = Product('keyboard', 50)
        self.cart = ShoppingCart()
        self.cart.add_item(self.product1)
        self.cart.add_item(self.product2)
        self.assertEqual(self.cart.calculate_total(), 1000)
        
        
if __name__ == "__main__":
    unittest.main()