surnames = input("Введіть декілька прізвищ, розділених пробілами: ").split()
first_letters = []
for surname in surnames:
    first_letters.append(surname[0])

print("Перші літери прізвищ: " + "".join(first_letters))
