class NegativeNumberError(Exception):
    pass


def main():
    square()


def square():
    while True:
        a = input("Enter a: ")
        try:
            a = int(a)
            break
        except ValueError:
            print("Enter a number")
    while True:
        b = input("Enter b: ")
        try:
            b = int(b)
            break
        except ValueError:
            print("Enter b number")
    try:
        if a < 0 or b < 0:
            raise NegativeNumberError("Length or height can't be a negative number")
    except NegativeNumberError:
        print("We can't calculate square due to the incorrect input")
        return None
    print(f"The square is {a * b}")


if __name__ == "__main__":
    main()
