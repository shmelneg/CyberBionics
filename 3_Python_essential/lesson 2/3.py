class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_for_rise(self):
        self.salary = self.salary * 1.15


class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def skillup(self):
        print(f"Your level in {self.language} has raised")


class Woman():

    def __init__(self, name):
        self.name = name

    def maternity(self):
        print("Your maternity leave has started. Your work position will be kept for you")


class Developerness(Developer, Woman):
    pass


employee1 = Developerness("Sandra", 1500, "python")

print(employee1.salary)
employee1.apply_for_rise()
print(employee1.salary)
employee1.skillup()
employee1.maternity()

print(Developerness.__mro__)
