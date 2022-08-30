class Vehicle:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
        return f"Vehilce type: {self.name}, Vehicle speed: {self.speed} km/h"

class Boat(Vehicle):

    def __str__(self):
        return f"Vehilce type: {self.name}, Vehicle speed: {self.speed / 1.852} knots"

class Wheel_vehicle(Vehicle):

    def __init__(self, name, speed, number_of_wheels):
        super().__init__(name, speed)
        self.number_of_wheels = number_of_wheels

    def __str__(self):
        return f"Vehilce type: {self.name}, Vehicle speed: {self.speed} km/h, it has {self.number_of_wheels} wheels"

class Car(Wheel_vehicle):

    def __init__(self, name, speed, number_of_wheels, model, horse_power):
        super().__init__(name, speed, number_of_wheels)
        self.model = model
        self.horse_power = horse_power

    def __str__(self):
        return f"Car model: {self.model}, Max speed: {self.speed} km/h, Engine: {self.horse_power} hps"

yacht = Boat("yacht", 20)
bicycle = Wheel_vehicle("bicycle", 20, 2)
miata = Car("car", 250, 4, "Mazda MX-5", 185)

print(yacht)
print(bicycle)
print(miata)
