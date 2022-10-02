import sqlite3
from datetime import datetime

def main():
    while True:
        print("==========================================")
        menu = input("Please, choose an operation:\n\t"
                     "1. Add new expense transaction\n\t"
                     "2. Add new income transaction\n\t"
                     "3. View the Accounting table\n\t"
                     "4. Calculate all your expenses\n\t"
                     "0. Exit\n>> ")
        print("==========================================")
        match menu:
            case "1":
                inp_description = input("Set a description of the transaction: ")
                inp_amount = input("Enter the amount of the transaction: ")
                now = datetime.now()
                inp_time = now.strftime("%m-%d-%Y %H:%M")

                request = """
                INSERT INTO Accounting (description, expenses, transaction_time) 
                VALUES ('""" + inp_description + "'," + inp_amount + ", '" + inp_time + "')"

                insert(request)
            case "2":
                inp_description = input("Set a description of the transaction: ")
                inp_amount = input("Enter the amount of the transaction: ")
                now = datetime.now()
                inp_time = now.strftime("%m-%d-%Y, %H:%M")

                request = """
                INSERT INTO Accounting (description, income, transaction_time) 
                VALUES ('""" + inp_description + "'," + inp_amount + ", '" + inp_time + "')"

                insert(request)
            case "3":
                view()
            case "4":
                calculate_expenses()
            case "0":
                print("Good bye")
                break
            case _:
                print("Please choose from the menu items (1, 2, 3, 4, or 0)")


def insert(request):
    connection = sqlite3.connect('Accounting.db')
    cursor = connection.cursor()

    cursor.execute(request)
    connection.commit()
    print("The transaction has been added to the Expenses table")

    cursor.close()
    connection.close()


def view():
    connection = sqlite3.connect('Accounting.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Accounting;')
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    connection.close()


def calculate_expenses():
    connection = sqlite3.connect('Accounting.db')
    cursor = connection.cursor()

    cursor.execute('SELECT expenses FROM Accounting;')
    result = cursor.fetchall()

    summary = 0.0
    for cell in result:
        if cell[0]:
            summary += cell[0]

    print(f"Your total expenses are: {summary}")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
