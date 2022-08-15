def main():
    lower_level = int(input("Enter the lower level for the calculation of the sum: "))
    upper_level = int(input("Enter the upper level for the calculation of the sum: "))
    print("The sum of all elements in the range is", my_sum(lower_level, upper_level))



def my_sum(start, finish):
    """This function calculates the sum of all elements in the range provided by user"""
    if finish == start:
        return start
    else:
        return finish + my_sum(start, finish - 1)


if __name__ == '__main__':
    main()
