def main():
    upper_level = int(input("Enter the upper border of the range: "))
    prime_numbers = []
    for i in range(upper_level + 1):
        if is_prime(i):
            prime_numbers.append(i)
    print("The prime numbers in your range are:", prime_numbers)
    menu = input("Select (1 or 2) what you want to do with those prime numbers:\n"
                 "1. Find a sum of the numbers\n2. Find a product of the numbers\n?> ")
    if menu == "1":
        print("The sum of the numbers is:", sum(prime_numbers))
    elif menu == "2":
        product = 1
        for j in prime_numbers:
            product *= j
        print("The product of the numbers is:", product)
    else:
        print("Sorry, I can't help you")


def is_prime(number):
    answer = True
    if number < 2:
        answer = False
    elif number == 2:
        answer = True
    else:
        for x in range(2, number):
            if number % x == 0:
                answer = False
    return answer

main()