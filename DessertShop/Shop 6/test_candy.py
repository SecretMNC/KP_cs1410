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
