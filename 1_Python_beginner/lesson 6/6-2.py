"""
Замість цього завдання буде наступне:
Є два списки, які наповнюються користувачем з клавіатури.
Сформувати список, в якому будуть міститися унікальні значення першого відносно другого списку
та навпаки без повторень. Роздрукувати підсумковий об'єкт на екран в прямій послідовності,
зворотній, а також виконати сортування за зростанням та спаданням.
"""

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

list3 = []
for i in list1:
    if (i not in list2) and (i not in list3):
        list3.append(i)
for j in list2:
    if (j not in list1) and (j not in list3):
        list3.append(j)

print("The unique values of the lists are:", list3)
print("The same but reversed:", list3[::- 1])
list3.sort()
print("The sorted final list is:", list3)
print("The reverse-sorted final list is:", list3[::- 1])