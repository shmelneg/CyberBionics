from operator import itemgetter

people = [
    {"прізвище": "Іванов", "посада": "сторож", "стаж роботи": 2, "портфоліо": "something", "KPI": 90, "зарплата": 1000},
    {"прізвище": "Петров", "посада": "директор", "стаж роботи": 5, "портфоліо": "something", "KPI": 99, "зарплата": 5000},
    {"прізвище": "Сидоров", "посада": "бухгалтер", "стаж роботи": 4, "портфоліо": "something", "KPI": 85, "зарплата": 4000},
    {"прізвище": "Шевченко", "посада": "поет", "стаж роботи": 1, "портфоліо": "something", "KPI": 71, "зарплата": 2000},
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
