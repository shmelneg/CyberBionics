a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

disr = (b**2)-(4*a*c)

x1 = (-b-disr**0.5) / (2*a)
x2 = (-b+disr**0.5) / (2*a)

print ("x1={0}, x2={1}".format(x1,x2))