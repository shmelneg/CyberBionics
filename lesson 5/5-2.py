import statistics

while True:
    answer = input("Введіть як мінімум 5 чисел, розділених пробілами: ")
    answ_splitted = answer.split()

    if not answer.replace(" ", "").isdigit():
        print("Допускаються лише числа. Спробуйте ще раз.")
        continue
    elif len(answ_splitted) < 5:
        print("Потрібно не менше 5 чисел. Спробуйте ще раз.")
        continue
    else:
        numbers = []
        for n in answ_splitted:
            numbers.append(int(n))
        break

print("Cумa другого, передостаннього та середнього арифметичного вашої послідовності =",
      numbers[1] + numbers[-2] + statistics.mean(numbers))
