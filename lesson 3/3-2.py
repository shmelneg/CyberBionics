import math

x = float(input("Please enter the value of x: "))

if -math.pi <= x <= math.pi:
    print("\nFor x that is -PI <= x <= PI, y = cos(x).\nThus, for your value of x the answer is", math.cos(x))

if -math.pi < x < math.pi:
    print("\nFor x that is -PI < x < PI, y = x.\nThus, for your value of x the answer is", x)

else:
    print("Your x value is outside of the scope")
 