def main():
    answer = input("Введіть рядок чисел, розділених пробілами: ").split()
    elements = [int(i) for i in answer]
    print("The result is: ", mult(elements))

def mult(nums):
    result = 1
    for n in nums:
        result *= n
    return result


if __name__ == '__main__':
    main()