while True:
    a = int(input("Please enter a: "))
    b = int(input("Please enter b which is higher than a: "))
    if a < b:
        break
    else:
        print("Try again but a < b")

sum = 0
for i in range(a, b + 1):
    sum += i

arithmetic_mean = sum / (b - a)

final_answer = 0
for i in range(a, b + 1):
    if i % arithmetic_mean == 0:
        final_answer += i

print("The sum of all natural numbers which are multiples of the arithmetic mean is", final_answer)
