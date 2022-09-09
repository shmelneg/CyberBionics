while True:
    try:
        start = int(input("Input start of the range value: "))
        upper = int(input("Input end of the range value: "))
        my_pow = int(input("Input power value: "))
        break
    except ValueError:
        print("Both base and power values must be integers. Try again.")

my_list = [i ** my_pow for i in range(start, upper + 1)]
my_gen = (i ** my_pow for i in range(start, upper + 1))

print(my_list)

while True:
    try:
        print(next(my_gen))
    except StopIteration:
        break
