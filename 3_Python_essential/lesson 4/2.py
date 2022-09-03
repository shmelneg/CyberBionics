def main():
    calculator()


def calculator():
    #getting first number
    while True:
        a = input("Enter the first number: ")
        try:
            a = int(a)
            break
        except ValueError:
            print("Enter a number")

    # getting operator
    while True:
        operator = input("Enter math operator (+, -, *, /, or **): ")
        if operator in ["+", "-", "*", "/", "**"]:
            break

    #getting second number
    while True:
        b = input("Enter the second number: ")
        try:
            b = int(b)
            break
        except ValueError:
            print("Enter a number")

    #calculations
    match operator:
        case "+":
            result = a + b
            print(f"a + b = {result}")
        case "-":
            result = a - b
            print(f"a - b = {result}")
        case "*":
            result = a * b
            print(f"a * b = {result}")
        case "/":
            try:
                result = a + b
                print(f"a + b = {result}")
            except ZeroDivisionError:
                print("Numbers cannot be divided by zero")
        case "**":
            try:
                result = a**b
                print(f"a**b = {result}")
            except ZeroDivisionError:
                print("Zero cannot be raised to a negative power")

if __name__ == "__main__":
    main()
