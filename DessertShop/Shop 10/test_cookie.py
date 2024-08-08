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

    # New tests for Combinable functionality
    def test_can_combine_true(self):
        cookie1 = dessert.Cookie("Chocolate Chip", 6, 3.99)
        cookie2 = dessert.Cookie("Chocolate Chip", 12, 3.99)
        self.assertTrue(cookie1.can_combine(cookie2))

    def test_can_combine_false(self):
        cookie = dessert.Cookie("Chocolate Chip", 6, 3.99)
        candy = dessert.Candy("Gummy Bears", 0.5, 0.25)
        self.assertFalse(cookie.can_combine(candy))

    def test_combine(self):
        cookie1 = dessert.Cookie("Chocolate Chip", 6, 3.99)
        cookie2 = dessert.Cookie("Chocolate Chip", 12, 3.99)
        combined = cookie1.combine(cookie2)
        self.assertEqual(combined.cookie_quantity, 18)
        self.assertEqual(combined.name, "Chocolate Chip")
        self.assertEqual(combined.price_per_dozen, 3.99)

    def test_combine_fail(self):
        cookie = dessert.Cookie("Chocolate Chip", 6, 3.99)
        candy = dessert.Candy("Gummy Bears", 0.5, 0.25)
        with self.assertRaises(AttributeError):
            cookie.combine(candy)
