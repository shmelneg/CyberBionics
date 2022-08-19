def main():
    answer = input("Введіть рядок чисел, розділених пробілами: ").split()
    elements = list(map(int, answer))
    print("Середнє значення:", average(elements))


def average(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum / len(nums)


if __name__ == '__main__':
    main()
