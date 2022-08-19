def main():
    print("Let's solve the quadratic equation ax^2+bx+c=0")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    answer1, answer2 = quadratic_equation(a, b, c)

    if answer1 and answer2:
        print("The first root is", answer1, "and the second root is", answer2)
    else:
        print("The equation has no roots")


def quadratic_equation(a, b, c):
    x1 = None
    x2 = None

    #function to find a discriminant
    def calc_rezult(a, b, c):
        discriminant = b**2 - 4 * a * c
        return discriminant

    if calc_rezult(a, b, c) < 0:
        return x1, x2
    else:
        x1 = (-b + calc_rezult(a, b, c)**0.5) / (2 * a)
        x2 = (-b - calc_rezult(a, b, c)**0.5) / (2 * a)
        return (x1, x2)


if __name__ == '__main__':
    main()
