def main():
    step = -5.0
    while step <= 5:
        print("For", step, "pow2 =", pow2(step), "and pow3 =", pow3(step))
        step += 0.5


def pow2(number):
    return number * number

def pow3(number):
    return number ** 3

if __name__ == '__main__':
    main()
