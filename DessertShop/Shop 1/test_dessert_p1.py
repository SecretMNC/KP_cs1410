import dessert
from unittest import TestCase

class TestDessertItem(TestCase):

    def test_false(self):
        item = dessert.DessertItem()

    def test_true(self):
        item = dessert.DessertItem('Test item')

    def test_types(self):
        item = dessert.DessertItem(True)


class TestCandy(TestCase):

    def test_false(self):
        candy = dessert.Candy()

    def test_True(self):
        candy = dessert.Candy("Test dessert", 2.5, 1.5)

    def test_types(self):
        candy = dessert.Candy(True, 2, "0.5")

class TestCookie(TestCase):

    def test_false(self):
        cookie = dessert.Cookie()

    def test_True(self):
        cookie = dessert.Cookie("Test dessert", 2, 1.5)

    def test_types(self):

        cookie = dessert.Cookie(True, 2.0, "0.5")

class TestIceCream(TestCase):

    def test_false(self):
        icecream = dessert.IceCream()

    def test_True(self):
        icecream = dessert.IceCream("Test dessert", 2, 1.5)

    def test_types(self):
        icecream = dessert.IceCream(True, 2.0, "0.5")

class TestSundae(TestCase):

    def test_false(self):
        sundae = dessert.Sundae()

    def test_True(self):
        sundae = dessert.Sundae("Test dessert", 2, 1.5, "Test Topping", 0.5)

    def test_types(self):
        sundae = dessert.Sundae(True, 2.0, "0.5", 100, 1)

