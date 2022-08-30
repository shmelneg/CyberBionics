class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def draw(self):
        for _ in range(self.length):
            print("*" * self.width)


class Mouse_input:

    def __init__(self, name=None):
        self.name = name

    def click(self):
        if self.name:
            print(f"You've clicked on {self.name}")
        else:
            print(f"You've clicked on me")


class Button(Rectangle, Mouse_input):

    def __init__(self, length, width, name):
        super().__init__(length, width)
        self.name = name


btn = Button(3, 5, "Exit button")

btn.draw()
btn.click()
