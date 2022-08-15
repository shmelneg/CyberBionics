def main():
    stairs = int(input("Enter the number of steps of a stair: "))
    print("You can reach the highest step by", steps(stairs), "different ways")


def steps(level):
    one, two = 1, 1
    for i in range(level - 1):
        temp = one
        one = one + two
        two = temp
    return one

if __name__ == '__main__':
    main()
