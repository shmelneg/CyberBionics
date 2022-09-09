iterable = iter((input("Input a phrase to iterate by words\n>> ").split()))

while True:
    try:
        print(next(iterable))
    except StopIteration:
        break
    