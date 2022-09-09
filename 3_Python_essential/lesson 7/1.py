def main():
    original_list = ['one', 'two', 'three', 'four', 'five', 'six']

    my_gen = backward(original_list)

    while True:
        try:
            print(next(my_gen))
        except StopIteration:
            break


def backward(original):
    return (i for i in original[::-1])


if __name__ == "__main__":
    main()
    