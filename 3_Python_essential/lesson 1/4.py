class Dealership:

    def __init__(self, balance=0):
        self.balance = balance
        self.cars = []

    def __str__(self):
        if self.cars:
            return f"We have {self.balance} USD in the bank account and the following cars for sale: {self.cars}"
        else:
            return f"We have {self.balance} USD in the bank account but don't have any cars for sale now"

    def supply(self, car):
        self.cars.append(car)
        self.balance -= car.supply_price

    def sell(self, car):
        if car in self.cars:
            self.cars.remove(car)
            self.balance += car.sale_price
            print(f"Congratulations! You are the lucky owner of {car}")
        else:
            print("Sorry, we don't have such model in stock")


class Car:

    def __init__(self, maker, model, supply_price, sale_price):
        self.maker = maker
        self.model = model
        self.supply_price = supply_price
        self.sale_price = sale_price

    def __str__(self):
        return f"{self.maker} {self.model}"

    def __repr__(self):
        return f"{self.maker} {self.model}"


miata = Car("Mazda", "MX-5", 15000, 24999)
cx5 = Car("Mazda", "CX-5", 25000, 33999)
model3 = Car("Mazda", "3", 21000, 26999)
model6 = Car("Mazda", "6", 24000, 31999)

mazda_center = Dealership(100000)
print(mazda_center)
mazda_center.supply(model6)
mazda_center.supply(cx5)
mazda_center.supply(miata)
mazda_center.supply(miata)
print(mazda_center)

mazda_center.sell(miata)
mazda_center.sell(model6)
mazda_center.sell(model6)
print(mazda_center)
