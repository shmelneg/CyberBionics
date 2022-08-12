def main():
    while True:
        try:
            a = int(input("Please enter the first number: "))
            b = int(input("Please enter the second number: "))
            c = int(input("Please enter the third number: "))
        except:
            print("Let's try again but with NUMBERS only")
        elements = [a, b, c]
        print("The average of your numbers is", mean(elements))

        repeat = input("Do you want to calculate more? (type 'no' to stop) \n?> ").lower()
        if repeat == "no" or repeat == "n":
            break
        else:
            continue

def mean(nums):
    total = 0
    for i in nums:
        total += i
    return total / len(nums)

if __name__ == '__main__':
    main()
