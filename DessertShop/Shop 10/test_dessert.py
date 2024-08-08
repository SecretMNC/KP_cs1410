import dessert
from unittest import TestCase

class TestDessertItem(TestCase):

    def test_calc_cost(self):
        candy = dessert.Candy("Test", 1, 2.4999)
        self.assertEqual(candy.calculate_cost(), 2.5)

    def test_calc_tax(self):
        candy = dessert.Candy("Test", 10, 1)
        self.assertEqual(candy.calculate_tax(), 0.72)
    
    def test_eq(self):
        cookie1 = dessert.Cookie("Cookie1", 12, 3)
        cookie2 = dessert.Cookie("Cookie2", 6, 6)
        self.assertTrue(cookie1 == cookie2)

    def test_ne(self):
        cookie1 = dessert.Cookie("Cookie1", 12, 3)
        cookie2 = dessert.Cookie("Cookie2", 12, 6)
        self.assertTrue(cookie1 != cookie2)

    def test_lt(self):
        cookie1 = dessert.Cookie("Cookie1", 12, 3)
        cookie2 = dessert.Cookie("Cookie2", 12, 6)
        self.assertTrue(cookie1 < cookie2)

    def test_gt(self):
        cookie1 = dessert.Cookie("Cookie1", 12, 10)
        cookie2 = dessert.Cookie("Cookie2", 12, 6)
        self.assertTrue(cookie1 > cookie2)

    def test_le(self):
        cookie1 = dessert.Cookie("Cookie1", 12, 3)
        cookie2 = dessert.Cookie("Cookie2", 12, 6)
        self.assertTrue(cookie1 <= cookie2)

        cookie1 = dessert.Cookie("Cookie1", 12, 6)
        cookie2 = dessert.Cookie("Cookie2", 12, 6)
        self.assertTrue(cookie1 <= cookie2)

    def test_ge(self):
        cookie1 = dessert.Cookie("Cookie1", 12, 10)
        cookie2 = dessert.Cookie("Cookie2", 12, 6)
        self.assertTrue(cookie1 >= cookie2)

        cookie1 = dessert.Cookie("Cookie1", 12, 6)
        cookie2 = dessert.Cookie("Cookie2", 12, 6)
        self.assertTrue(cookie1 >= cookie2)
