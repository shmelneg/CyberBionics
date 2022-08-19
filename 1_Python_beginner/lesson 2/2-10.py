import math

r = int(input("Please enter the radius: "))
h = int(input("Please enter the height: "))

volume = math.pi * (r**2) * h

print("The volume of the cylinder is", round(volume, 2))