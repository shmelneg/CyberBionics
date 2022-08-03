while True:
    n = int(input("Please enter non-negative n: "))
    if n >= 0:
        break
    else:
        print("Try again but NON-NEGATIVE n")

result = 1

for i in range(1, n + 1):
    result *= i

print("The factorial of your n is", result)