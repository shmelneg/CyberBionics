from operator import itemgetter

people = [
    {"прізвище": "Іванов", "посада": "сторож", "стаж": 2, "портфоліо": "something", "KPI": 90, "зарплата": 1000},
    {"прізвище": "Петров", "посада": "директор", "стаж": 5, "портфоліо": "something", "KPI": 99, "зарплата": 5000},
    {"прізвище": "Сидоров", "посада": "бухгалтер", "стаж": 4, "портфоліо": "something", "KPI": 85, "зарплата": 4000},
    {"прізвище": "Шевченко", "посада": "поет", "стаж": 1, "портфоліо": "something", "KPI": 71, "зарплата": 2000},
]

#sort by surname
people.sort(key=itemgetter("прізвище"))
for person in people:
    print(person)

print()

#sort by KPI
people.sort(key=itemgetter("KPI"), reverse=True)
for person in people:
    print(person)

#change occupation of Ivanov to "driver"
people[1]["посада"] = input("Enter new role of the employee: ")
print(people[1])