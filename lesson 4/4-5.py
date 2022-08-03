height = int(input("Please enter the height of the rectangle: "))
length = int(input("Please enter the length of the rectangle: "))
print()

for i in range(height):
    for j in range(length):
        print("*", end="")
    print(" ")
