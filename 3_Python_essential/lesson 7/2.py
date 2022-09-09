while True:
    try:
        upper_limit = int(input("Set the upper limit of the list: "))
        break
    except ValueError:
        print("It must be an integer. Try again.")

num_list = list(range(1, upper_limit + 1))

# using generator
my_gen = (x**2 for x in num_list if x % 2 == 0)
while True:
    try:
        print(next(my_gen))
    except StopIteration:
        break

# using loop
sqr_list = []
for i in num_list:
    if i % 2 == 0:
        sqr_list.append(i**2)
print(sqr_list)
