import dessert
from unittest import TestCase

class TestDessertItem(TestCase):

    def test_calc_cost(self):
        candy = dessert.Candy("Test", 1, 2.4999)
        self.assertEqual(candy.calculate_cost(), 2.5)

    def test_calc_tax(self):
        candy = dessert.Candy("Test", 10, 1)
        self.assertEqual(candy.calculate_tax(), 0.72)
    
    def test_false(self):
        # Test if object has "False" values for attributes by default
        pass

    def test_true(self):
        # Test if object can accept a string for name
        pass

    def test_types(self):
        # Test if attribute is correct type, even if passed incorrect type
        pass

