import random


with open('numbers.txt', "w") as file:
    for _ in range(10000):
        number = random.randint(0, 10001)
        file.writelines(str(number) + "\n")
