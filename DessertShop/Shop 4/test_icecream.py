import dessert
from unittest import TestCase

class TestIceCream(TestCase):

    def test_calc_cost(self):
        icecream = dessert.IceCream("Test", 2, 2)
        self.assertEqual(icecream.calculate_cost(), 4)

    def test_calc_tax(self):
        pistachio = dessert.IceCream("Pistachio", 10, 1)
        self.assertEqual(pistachio.calculate_tax(), 0.72)

    def test_false(self):
        # Test if object has "False" values for attributes by default
        icecream = dessert.IceCream()

    def test_True(self):
        # Test if object accepts values for attributes
        icecream = dessert.IceCream("Test dessert", 2, 1.5)

    def test_types(self):
        # Tests if attributes are correct type, even when passed incorrect types
        icecream = dessert.IceCream(True, 2.0, "0.5")

