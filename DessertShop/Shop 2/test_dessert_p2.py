import dessert
from unittest import TestCase

class TestDessertItem(TestCase):

      def test_false(self):
            # Test if object has "False" values for attributes by default
            item = dessert.DessertItem()


      def test_true(self):
            # Test if object can accept a string for name
            item = dessert.DessertItem('Test item')


      def test_types(self):
            # Test if attribute is correct type, even if passed incorrect type
            item = dessert.DessertItem(True)


class TestCandy(TestCase):

      def test_false(self):
            # Test if object has "False" values for attributes by default
            candy = dessert.Candy()


      def test_True(self):
            # Test if object accepts values for attributes
            candy = dessert.Candy("Test dessert", 2.5, 1.5)


      def test_types(self):
            # Tests if attributes are correct type, even when passed incorrect types
            candy = dessert.Candy(True, 2, "0.5")


class TestCookie(TestCase):

      def test_false(self):
            # Test if object has "False" values for attributes by default
            cookie = dessert.Cookie()


      def test_True(self):
            # Test if object accepts values for attributes
            cookie = dessert.Cookie("Test dessert", 2, 1.5)


      def test_types(self):
            # Tests if attributes are correct type, even when passed incorrect types
            cookie = dessert.Cookie(True, 2.0, "0.5")


class TestIceCream(TestCase):

      def test_false(self):
            # Test if object has "False" values for attributes by default
            icecream = dessert.IceCream()


      def test_True(self):
            # Test if object accepts values for attributes
            icecream = dessert.IceCream("Test dessert", 2, 1.5)


      def test_types(self):
            # Tests if attributes are correct type, even when passed incorrect types
            icecream = dessert.IceCream(True, 2.0, "0.5")

class TestSundae(TestCase):

      def test_false(self):
            # Test if object has "False" values for attributes by default
            sundae = dessert.Sundae()
 

      def test_True(self):
            # Test if object accepts values for attributes
            sundae = dessert.Sundae("Test dessert", 2, 1.5, "Test Topping", 0.5)


      def test_types(self):
            # Tests if attributes are correct type, even when passed incorrect types
            sundae = dessert.Sundae(True, 2.0, "0.5", 100, 1)


