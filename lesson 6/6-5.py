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

mult = int(input("How many copies of the new list do you want? "))
print("Enjoy: ", end="")
for j in range(mult):
    print(new_list, " ", end="")
print()
int_list.clear()