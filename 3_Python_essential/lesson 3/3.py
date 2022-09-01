class Temperature:

    def __int__(self):
        self._celsius = 0
        self._fahrenheit = 0

    def __str__(self):
        return f"The current temperature is {self._celsius}°C which is {self._fahrenheit}°F"

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, degrees):
        self._celsius = degrees
        self._fahrenheit = degrees * 1.8 + 32

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, degrees):
        self._fahrenheit = degrees
        self._celsius = (degrees - 32) * 0.5556


thermometer = Temperature()

thermometer.celsius = 30
print(f"In Celsius: {thermometer.celsius}")
print(f"In Fahrenheit: {thermometer.fahrenheit}")
print(thermometer)

thermometer.fahrenheit = 100
print(f"In Celsius: {thermometer.celsius}")
print(f"In Fahrenheit: {thermometer.fahrenheit}")
print(thermometer)
