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
