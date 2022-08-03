import math

r = int(input("Please enter the radius: "))
h = int(input("Please enter the height: "))

volume = (math.pi * (r**2) * h) / 3

print("The volume of the cone is", round(volume, 2))