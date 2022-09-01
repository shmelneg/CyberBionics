class Base:

    def __init__(self):
        self.name = "Base"

    def method(self):
        print(f"Hello from {self.name}")


class Child(Base):

    def __init__(self):
        self.name = "Child"


base = Base()
child = Child()

base.method()
child.method()
