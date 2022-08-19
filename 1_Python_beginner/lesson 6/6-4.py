list =[]
size = int(input("Choose the size of the list: "))
for i in range(size):
    list.append(int(input("Enter a number for the list: ")))

print("Your list is:", list)
print()
list1 = list.copy()

while True:
    menu = input("Select (1 or 2) what you want to do with the list:\n"
                 "1. Reverse the list\n2. Sort the list\n"
                 "Select 0 to restore your original list or any other symbol to exit\n?> ")
    if menu == "0":
        list1 = list.copy()
        print("Your original list is", list1)
        print()
    elif menu == "1":
        print("The reversed list is the following:", list1[::-1])
        print()
    elif menu == "2":
        list1.sort()
        print("The sorted list is the following:", list1)
        print()
    else:
        print("Good Bye")
        break