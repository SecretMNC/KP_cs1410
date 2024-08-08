import dessert
from unittest import TestCase

class TestOrder(TestCase):
    item = dessert.Candy("Test", 1, .12)
    order = dessert.Order()
    order.add(item)

    def test_cash(self):
        # Tests if "CASH" is a valid dessert object pay method
        TestOrder.order.set_pay_type("CASH")
        self.assertEqual(TestOrder.order.pay_method, "CASH")

    def test_card(self):
        # Tests if "CARD" is a valid dessert object pay method
        TestOrder.order.set_pay_type("CARD")
        self.assertEqual(TestOrder.order.pay_method, "CARD")

    def test_phone(self):
        # Tests if "PHONE" is a valid dessert object pay method
        TestOrder.order.set_pay_type("PHONE")
        self.assertEqual(TestOrder.order.pay_method, "PHONE")

    def test_set_paytype(self):
        # Tests if an invalid value for pay method will is error handled
        try:
            TestOrder.order.set_pay_type("asdf")
        except ValueError as err:
            self.assertTrue(err)
        else:
            self.assertTrue("")

    def test_get_paytype(self):
        # Tests if an invalid value that's already in pay method is error handled
        TestOrder.order.pay_method = "ASDF"
        try:
            TestOrder.order.get_pay_type()
        except ValueError as err:
            self.assertTrue(err)
        else:
            self.assertTrue("")

    def test_order(self):
        # Tests if the bubblesort algorithm works as expected
        cookie1 = dessert.Cookie("COOKIE1", 12, 10)       # Should be index 4
        cookie2 = dessert.Cookie("COOKIE2", 12, 6)        # Should be index 1
        candy1 = dessert.Candy("CANDY1", 1, 3)            # Should be index 0
        icecream1 = dessert.IceCream("IC1", 2, 4)         # Should be index 2
        sundae1 = dessert.Sundae("SUNDAE", 2, 4, "a", 1)  # Should be index 3

        test_order = dessert.Order([cookie1, cookie2, candy1, icecream1, sundae1])        
        test_order.sort()
        
        self.assertEqual(test_order.order[0], candy1)
        self.assertEqual(test_order.order[1], cookie2)
        self.assertEqual(test_order.order[2], icecream1)
        self.assertEqual(test_order.order[3], sundae1)
        self.assertEqual(test_order.order[4], cookie1)
