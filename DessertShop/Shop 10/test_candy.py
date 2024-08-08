import dessert
from unittest import TestCase

class TestCandy(TestCase):

    def test_calc_cost(self):
        candy = dessert.Candy("Test", 1, 2.4999)
        self.assertEqual(candy.calculate_cost(), 2.5)

    def test_calc_tax(self):
        candy_corn = dessert.Candy("Candy Corn", 40, .25)
        self.assertEqual(candy_corn.calculate_tax(), 0.72)
    
    def test_false(self):
        # Test if object has "False" values for attributes by default
        candy = dessert.Candy()

    def test_True(self):
        # Test if object accepts values for attributes
        candy = dessert.Candy("Test dessert", 2.5, 1.5)

    def test_types(self):
        # Tests if attributes are correct type, even when passed incorrect types
        candy = dessert.Candy(True, 2, "0.5")

    def test_packaging(self):
        candy = dessert.Candy(True, 2, "0.5")
        self.assertEqual(candy.packaging, "Bag")

    # New tests for Combinable functionality
    def test_can_combine_true(self):
        candy1 = dessert.Candy("Gummy Bears", 0.5, 0.25)
        candy2 = dessert.Candy("Gummy Bears", 1.25, 0.25)
        self.assertTrue(candy1.can_combine(candy2))

    def test_can_combine_false(self):
        candy = dessert.Candy("Gummy Bears", 0.5, 0.25)
        cookie = dessert.Cookie("Chocolate Chip", 6, 3.99)
        self.assertFalse(candy.can_combine(cookie))

    def test_combine(self):
        candy1 = dessert.Candy("Gummy Bears", 0.5, 0.25)
        candy2 = dessert.Candy("Gummy Bears", 1.25, 0.25)
        combined = candy1.combine(candy2)
        self.assertEqual(combined.candy_weight, 1.75)
        self.assertEqual(combined.name, "Gummy Bears")
        self.assertEqual(combined.price_per_pound, 0.25)

    def test_combine_fail(self):
        candy = dessert.Candy("Gummy Bears", 0.5, 0.25)
        cookie = dessert.Cookie("Chocolate Chip", 6, 3.99)
        with self.assertRaises(AttributeError):
            candy.combine(cookie)
