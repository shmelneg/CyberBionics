def prime_numbers(limit):
    counter = 0
    prime_list = [1, ]
    current_number = 1

    def is_prime(number):
        result = True
        if number == 1 or number == 2:
            result = True
        elif number > 2:
            for i in range(2, number):
                if (number % i) == 0:
                    result = False
        return result

    while True:
        if is_prime(current_number):
            yield current_number
            counter += 1
        current_number += 1
        if counter >= limit:
            break


def main():
    upper_limit = int(input("Set the number of prime numbers tha you want to add to the generator: "))
    counter = 1
    for i in prime_numbers(upper_limit):
        if counter < upper_limit:
            print(i, end=", ")
        else:
            print(i, end=".\n")
        counter += 1


if __name__ == "__main__":
    main()
