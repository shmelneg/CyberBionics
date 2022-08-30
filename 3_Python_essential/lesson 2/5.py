from datetime import date


class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    @staticmethod
    def is_adult(country, age):
        if country == "UA":
            if age >= 18:
                return True
            else:
                return False
        elif country == "US":
            if age >= 21:
                return True
            else:
                return False
        else:
            print("Can's find this country")

    def print_info(self):
        print(self.surname + self.name + "'s age is: " + str(self.age))


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
print(m_per1.is_adult("UA", m_per1.age))
