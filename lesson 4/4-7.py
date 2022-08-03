amount = 0

while True:
    new_price = int(input("Please enter the price of the next item: "))
    if not new_price:
        print("The total amount due:", amount)
        break
    amount += new_price
