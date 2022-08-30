from datetime import date


class MyClass1:

    people_ages = []

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
        MyClass1.people_ages.append(self.age)

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    @classmethod
    def how_many_adults(cls):
        us = 0
        ua = 0
        for age in cls.people_ages:
            if age >= 21:
                us += 1
                ua += 1
            elif age >= 18:
                ua += 1
        return f"Among the people we have {us} adults in US and {ua} adults in UA"

    def print_info(self):
        print(self.surname + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000)
m_per2.print_info()

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))

print(MyClass1.how_many_adults())
