with open('numbers.txt', 'r') as file:
    result = sum(map(int, file))
print(f"The sum of all numbers in the file is {result}")
