list1 = []
size = int(input("Choose the size of the list 1: "))
for i in range(size):
    list1.append(int(input("Enter a number for the list 1: ")))

list2 = []
size = int(input("Choose the size of the list 2: "))
for i in range(size):
    list2.append(int(input("Enter a number for the list 2: ")))

print("Your list 1 is:", list1)
print("Your list 2 is:", list2)

set1 = set(list1)
set2 = set(list2)

print("The unique values of the list 1:", set1 - set2)
print("The unique values of the list 2:", set2 - set1)
