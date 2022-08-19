def main():
    while True:
        a = int(input("Please enter a number: "))
        operator = (input("Please enter a math operator (+, -, *, /, **, sqrt, cbrt): "))
        if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**":
            b = int(input("Please enter a second number: "))

        match operator:
            case "/":
                if b == 0:
                    print("Error. Can't be divided by zero.")
                else:
                    print(a, operator, b, "=", divide(a, b))
            case "*":
                print(a, operator, b, "=", mult(a, b))
            case "-":
                print(a, operator, b, "=", minus(a, b))
            case "+":
                print(a, operator, b, "=", plus(a, b))
            case "**":
                print(a, operator, b, "=", power(a, b))
            case "cbrt":
                print(operator + "(" + str(a) + ")", "=", cbrt(a))
            case "sqrt":
                print(operator + "(" + str(a) + ")", "=", sqrt(a))
        repeat = input("Do you want to calculate more? (type 'no' to stop) \n?> ").lower()
        if repeat == "no" or repeat == "n":
            break
        else:
            continue

def divide(x, y):
    return x / y

def mult(x, y):
    return x * y

def minus(x, y):
    return x - y

def plus(x, y):
    return x + y

def power(x, y):
    return x ** y

def sqrt(x):
    return x ** (1/2)

def cbrt(x):
    return x ** (1/3)


if __name__ == '__main__':
    main()
