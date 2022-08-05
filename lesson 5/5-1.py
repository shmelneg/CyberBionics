while True:
    answer = input("Введіть свої прізвище імʼя та по-батькові: ")
    pib = answer.split()

    if len(pib) != 3:
        print("Програма очікує 3 слова (ПіБ)")
        continue

    if pib[0].isalpha() and pib[1].isalpha() and pib[2].isalpha():
        print("Ви будете занесені в базу як: ", end="")
        for i in pib:
            print(i.title(), end=" ")
        print()
        break
    else:
        print("Ваші ПІБ мають містити лише літери")
