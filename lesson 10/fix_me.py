import math

test_value = 5
multiplier = int(input('Введите количество повторов: '))

print(test_value * multiplier)
print(math.pi * test_value * multiplier)
print(math.e * 2)

while test_value >= 0:
    test_value -= 1

my_str = 'my string'
total = 0
for elem in my_str:
    total += pow(my_str.find(elem), 2)
    print("sum=", total)


def my_func(atr=1):
    print('atr', atr)


my_func(atr=5)
