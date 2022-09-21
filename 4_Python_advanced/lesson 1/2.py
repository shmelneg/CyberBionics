answer = input("Enter start and finish values (separated by space) of the future integers list: ")
start, finish = map(int, answer.split())
first_list = list(range(start, finish + 1))
print(f"The list of integers if the following: {first_list}")

# solution via list generator
second_list = [x**2 for x in first_list if x % 2 != 0]
print(f"The list of squared values of the odd numbers if the following: {second_list}")

# solution via lambda, map and filter

# filter odd numbers to a new list
odd_list = list(filter(lambda x: x % 2 != 0, first_list))

# creating short-name function for squared values
sqr = lambda x: x**2

# applying sqr to the odd list
third_list = list(map(sqr, odd_list))
print(f"The the same as the 2nd list but with lambda, map and filter: {third_list}")
