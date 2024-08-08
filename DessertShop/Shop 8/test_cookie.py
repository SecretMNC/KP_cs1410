import dessert
from unittest import TestCase

class TestCookie(TestCase):

    def test_calc_cost(self):
        cookie = dessert.Cookie("Test", 12, 2.4999)
        self.assertEqual(cookie.calculate_cost(), 2.5)

    def test_calc_tax(self):
        chocolate_chip = dessert.Cookie("Chocolate Chip", 12, 10)
        self.assertEqual(chocolate_chip.calculate_tax(), 0.72)

    def test_false(self):
        # Test if object has "False" values for attributes by default
        cookie = dessert.Cookie()

    def test_True(self):
        # Test if object accepts values for attributes
        cookie = dessert.Cookie("Test dessert", 2, 1.5)

    def test_types(self):
        # Tests if attributes are correct type, even when passed incorrect types
        cookie = dessert.Cookie(True, 2.0, "0.5")

    def test_packaging(self):
        cookie = dessert.Cookie("Test", 12, 2.4999)
        self.assertEqual(cookie.packaging, "Box")
