while True:
    answer = input("Введіть декілька чисел, розділених пробілом, а ми їх відсортуємо: ")
    answ_splitted = answer.split()

    if not answer.replace(" ", "").replace("-", "").isdigit():
        print("Допускаються лише числа. Спробуйте ще раз.")
        continue
    else:
        numbers = []
        for n in answ_splitted:
            numbers.append(int(n))
        numbers.sort()
        break

print(tuple(numbers))