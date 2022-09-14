def main():
    upper_limit = int(input("How many prime numbers do you need? "))
    print(f"Here are your prime numbers: {get_prime_numbers(upper_limit)}")


def is_prime(number):
    result = True
    if number == 1 or number == 2:
        result = True
    elif number > 2:
        for i in range(2, number):
            if (number % i) == 0:
                result = False
    return result


def get_prime_numbers(limit):
    counter = 0
    prime_list = []
    current_number = 1

    while True:
        if is_prime(current_number):
            prime_list.append(current_number)
            counter += 1
        current_number += 1
        if counter >= limit:
            break

    return prime_list


if __name__ == "__main__":
    main()
