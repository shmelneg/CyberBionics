from prime_functions import get_prime_numbers, is_prime


print("=============================================")
answer = input("Enter some number separated by spaces to check whether they are prime numbers: ").split()
test_list = map(int, answer)

for number in test_list:
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
print("=============================================")
upper_limit = int(input("I can generate prime numbers for you. How many do you want? "))
print(f"Here are your prime numbers: {get_prime_numbers(upper_limit)}")
