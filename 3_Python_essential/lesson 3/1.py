class Car:

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine
        self._max_speed = 200
        self.started = False
        self.speed = 0
        self.__service_interval = 5000

    def __str__(self):
        if self.started and self.speed:
            return f"You're driving {self.model} at {self.speed} km/h"
        else:
            return f"Car: {self.model}, engine: {self.engine} hsp, max.speed: {self._max_speed} km/h\n" \
                   f"Now the car isn't moving"

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed <= 230:
            self._max_speed = max_speed
        else:
            self._max_speed = 230

    def start(self):
        self.started = True
        print('The engine has been started')

    def stop(self):
        self.started = False
        print('The engine has been turned off')

    def set_speed(self, speed):
        if self.started:
            if speed > 230:
                self.speed = 230
            elif speed < 0:
                self.speed = 0
            else:
                self.speed = speed
        else:
            print('Start the engine first')

    def __stage1(self):
        self.engine *= 1.2
        self._max_speed *= 1.2
        self.__service_interval = 10000

    def service(self, center):
        if center == "official":
            self.__service_interval = 10000
        elif center == "custom":
            self.__stage1()
        else:
            pass


miata = Car("Mazda MX-5", 185)
print(miata)
miata.max_speed = 250
print(miata)
miata.set_speed(300)
print(miata)
miata.start()
miata.set_speed(300)
print(miata)

brz = Car("Subaru BRZ", 240)
print(brz)
brz.service("custom")
print(brz)
