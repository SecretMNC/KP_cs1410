class Temperature:
    
    def convert_fahrenheit_to_celsius(self, value):
        
        if value < -459.67:
            return("error: Temperature cannot be below absolute zero (-459.67 F)")
        else:
            return round(5/9 * (value - 32))
        
    def convert_celsius_to_fahrenheit(self, value):
        if value < -273.15:
            return("error: Temperature cannot be below absolute zero (-273.15 C)")
        else:
            return round(value *(9/5) + 32, 2)
