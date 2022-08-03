while True:
    a = int(input("Please enter a: "))
    b = int(input("Please enter b which is higher than a: "))
    if a < b:
        break
    else:
        print("Try again but a < b")
result = 0

for i in range(a, b + 1):
    result += i

print("The sum of all natural numbers in the range is", result)
