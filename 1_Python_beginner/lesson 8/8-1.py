def hello(name="Andrii"):
    print("Hello, " + name + "!")


answer = input("What's your name? ")

if answer == "":
    hello()
else:
    hello(answer)
