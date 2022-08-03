import math

a = int(input("Please enter a number: "))
operator = (input("Please enter a math operator (+, -, *, /, **, sqrt, cbrt, sin, cos, tan): "))
if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**":
    b = int(input("Please enter a second number: "))

match operator:
    case "/":
        print(a, operator, b, "=", a / b)
    case "*":
        print(a, operator, b, "=", a * b)
    case "-":
        print(a, operator, b, "=", a - b)
    case "+":
        print(a, operator, b, "=", a + b)
    case "**":
        print(a, operator, b, "=", a ** b)
    case "cbrt":
        print(operator + "(" + str(a) + ")", "=", a ** (1 / 3))
    case "sqrt":
        print(operator + "(" + str(a) + ")", "=", math.sqrt(a))
    case "sin":
        print(operator + "(" + str(a) + ")", "=", math.sin(a))
    case "cos":
        print(operator + "(" + str(a) + ")", "=", math.cos(a))
    case "tan":
        print(operator + "(" + str(a) + ")", "=", math.tan(a))
