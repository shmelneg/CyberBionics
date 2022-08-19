height = int(input("Please enter the height of the triangle: "))

length = 1
for i in range(height):
    for j in range(length):
        print("*", end="")
    length += 1
    print(" ")
