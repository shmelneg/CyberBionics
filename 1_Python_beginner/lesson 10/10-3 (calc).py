import math


def main():
    while True:
        print("Select operation:")
        print("\t1.Factorial")
        print("\t2.Square root")
        print("\t3.Cosine")
        print("\t4.Sine")
        print("\t5.Tangent")
        print("\t0.Exit")

        choice = input("Enter choice(1/2/3/4/5/0): ")

        if choice in ("1", "2", "3", "4", "5"):
            number = float(input("Enter a number for the operation: "))
            match choice:
                case "1":
                    print("The factorial of", number, "is", factorial(number))
                case "2":
                    print("The square root of", number, "is", square_root(number))
                case "3":
                    print("The cosine of", number, "is", cosine(number))
                case "4":
                    print("The sine of", number, "is", sine(number))
                case "5":
                    print("The tangent of", number, "is", tangent(number))
        elif choice == "0":
            break
        else:
            print("Invalid menu number")


def factorial(x):
    return math.factorial(x)


def square_root(x):
    return math.sqrt(x)


def cosine(x):
    return math.cos(x)


def sine(x):
    return math.sin(x)


def tangent(x):
    return math.tan(x)


if __name__ == "__main__":
    main()
