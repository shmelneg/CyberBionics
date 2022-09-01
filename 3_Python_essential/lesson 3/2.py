class English:

    def greeting(self, name):
        print("Hello", name)


class Spanish:

    def greeting(self, name):
        print("Hola", name)


language1 = English()
language2 = Spanish()

def hello_friend():
    name = input("What's your name? ")
    language1.greeting(name)
    language2.greeting(name)


hello_friend()
