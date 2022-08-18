warehouse = [{"item": "pen", "price": 1.49, "quantity": 15},
             {"item": "pencil", "price": 0.99, "quantity": 11},
             {"item": "paper", "price": 2.29, "quantity": 7},
             {"item": "folder", "price": 0.49, "quantity": 22},
             {"item": "ink", "price": 0.49, "quantity": 3}
             ]


def main():
    while True:
        print("Select account:")
        print("\t1.I'm a buyer and want to buy something in your store")
        print("\t2.I'm an administrator of the store and want to re-supply items")
        print("\t0.Exit")

        choice = input("Enter choice(1/2/0): ")

        if choice == "1":
            item = input("What item do you want to buy? ")
            quantity = int(input("How many of " + item + " do you want to buy? "))
            sell(item, quantity)

        elif choice == "2":
            item = input("What item do you want to supply? ")
            quantity = int(input("How many of " + item + " do you want to supply? "))
            price = float(input("What is the new price of this item? "))
            supply(item, quantity, price)

        elif choice == "0":
            break

        else:
            print("Invalid menu number")


#function for selling items to buyers
def sell(item, quantity):
    global warehouse
    missing_item = True
    for goods in warehouse:
        if goods["item"] == item:
            if goods["quantity"] < quantity:
                print("Sorry, we don't have so many items in our warehouse. We may offer you only", goods["quantity"])
                missing_item = False
            else:
                print("The price for", quantity, "pieces of", item, "is", quantity * goods["price"], "USD")
                goods["quantity"] = goods["quantity"] - quantity
                missing_item = False
    if missing_item:
        print("Sorry, we don't have such items in our warehouse")


#function for resupplying items by admins
def supply(item, quantity, price):
    global warehouse
    missing_item = True
    for goods in warehouse:
        if goods["item"] == item:
            goods["quantity"] = goods["quantity"] + quantity
            goods["price"] = price
            missing_item = False
    if missing_item:
        warehouse.append({"item": item, "price": price, "quantity": quantity})
    print("Now you have in stock:")
    for goods in warehouse:
        print(goods)


if __name__ == "__main__":
    main()
