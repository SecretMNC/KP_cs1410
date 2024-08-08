import dessert
from unittest import TestCase

class TestSundae(TestCase):

    def test_calc_cost(self):
        sundae = dessert.Sundae("Test", 2, 1.99, "test", 1.03)
        self.assertEqual(sundae.calculate_cost(), 5.01)

    def test_calc_tax(self):
        vanilla = dessert.Sundae("Vanilla", 19, .5, "Hot Fudge", .5)
        self.assertEqual(vanilla.calculate_tax(), 0.72)

    def test_false(self):
        # Test if object has "False" values for attributes by default
        sundae = dessert.Sundae()

    def test_True(self):
        # Test if object accepts values for attributes
        sundae = dessert.Sundae("Test dessert", 2, 1.5, "Test Topping", 0.5)

    def test_types(self):
        # Tests if attributes are correct type, even when passed incorrect types
        sundae = dessert.Sundae(True, 2.0, "0.5", 100, 1)

