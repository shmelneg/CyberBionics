start = int(input("Start of the range: "))
end = int(input("End of the range: "))
result = 1

for i in range(start, end + 1, 5):
    result *= i
    print(i, "* ", end="")

print("\n")
print("The result is", result)
