from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color, outline=(255, 255, 255))

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 0, 0))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


s = Shape()
s.save()
c = Circle()
c.draw()
c.erase()
c.save()
sq = Square()
sq.draw()
sq.erase()
sq.save()
t = Triangle()
t.draw()
t.erase()
t.save()
