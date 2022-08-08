int_list =[]
size = int(input("Choose the size of the list: "))
for i in range(size):
    int_list.append(int(input("Enter a number for the list: ")))
print("The list is:", int_list)

new_list = []
for i in int_list:
    if i % 2 != 0:
        new_list.append(i)
print("The new list includes only odd numbers:", new_list)

check = int(input("What number do you want to check? "))
if check not in new_list:
    print(check, "is not in the new list")
else:
    current_position = 0
    positions = []
    counter = 0
    for i in new_list:
        if i == check:
            positions.append(current_position)
            counter += 1
        current_position += 1
    print("Your number appears in the new list", counter, "times on the following positions:", positions)