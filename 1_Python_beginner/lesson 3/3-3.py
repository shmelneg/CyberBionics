a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

disr = (b**2)-(4*a*c)

if disr < 0:
    print("Відсутні дійсні корені.")
elif disr == 0:
    print("x =", -b / (2*a))
else:
    x1 = (-b-disr**0.5) / (2*a)
    x2 = (-b+disr**0.5) / (2*a)
    print ("x1 =", x1, "\nx2 =", x2)