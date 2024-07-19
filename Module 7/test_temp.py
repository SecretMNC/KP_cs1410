import unittest
from temp import Temperature
        
class TestTemperature(unittest.TestCase):
    def setUp(self):
        self.temp = Temperature()
        self.f_c_error = "error: Temperature cannot be below absolute zero (-459.67 F)"
        self.c_f_error = "error: Temperature cannot be below absolute zero (-273.15 C)"
    
    def test_convert_f_to_c(self):
        self.assertEqual(self.temp.convert_fahrenheit_to_celsius(32), 0)
        self.assertEqual(self.temp.convert_fahrenheit_to_celsius(212), 100)
        self.assertEqual(self.temp.convert_fahrenheit_to_celsius(-500), self.f_c_error)
        
    def test_convert_c_to_f(self):
        self.assertEqual(self.temp.convert_celsius_to_fahrenheit(0), 32)
        self.assertEqual(self.temp.convert_celsius_to_fahrenheit(100), 212)
        self.assertEqual(self.temp.convert_celsius_to_fahrenheit(-300), self.c_f_error)

if __name__ == "__main__":
    unittest.main()