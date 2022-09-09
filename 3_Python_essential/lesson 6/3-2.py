test_list = ["one", "two", "three", "four", "five", "six"]

# function to get a reverse iterator
def reverse_iterator(origin):
    reverse_list = origin[::-1]
    return iter(reverse_list)


my_iterator = reverse_iterator(test_list)

while True:
    try:
        print(next(my_iterator))
    except StopIteration:
        break
