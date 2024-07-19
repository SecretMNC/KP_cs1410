class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, new_temp: float):
        if new_temp >= -273.16:
            self._celsius = new_temp
        
    @property
    def fahrenheit(self):
        return float((self._celsius * 9/5) + 32)
    
celsius_temp = input("What is the temperature in Celsius?\n--> ")
temp = Temperature(float(celsius_temp))

while True:
    user_input = input("""What would you like to do?
(1): Check the temperature in Celsius
(2): Change the temperature in Celsius
(3): Check the temperature in Fahrenheit
(4): Quit
--> """)
    
    if user_input == '1':
        print(temp.celsius)
    elif user_input == '2':
        new_temp = input("What is the temperature in Celsius?\n--> ")
        temp.celsius = float(new_temp)
    elif user_input == '3':
        print(temp.fahrenheit)
    elif user_input == '4':
        break
    else:
        continue
        