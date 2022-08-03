answer = int(input("Please enter 1, 2 or 3: "))

if answer == 1:
    print("-=Volume of a cube calculation=-")
    a = int(input("Please enter the side of the cube: "))
    print("The volume of the cube is", a ** 3)
elif answer == 2:
    print("-=Perimeter of a triangle calculation=-")
    a = int(input("Please enter side 1 of the triangle: "))
    b = int(input("Please enter side 2 of the triangle: "))
    c = int(input("Please enter side 3 of the triangle: "))
    print("The perimeter of the triangle is", a + b + c)
elif answer == 3:
    print("Exit")
else:
    print("You have entered incorrect value")
