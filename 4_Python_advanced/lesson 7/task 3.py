import sqlite3
from datetime import date


class User:

    def __init__(self, full_name: str, short_name: str, birthday: 'date', email: str):
        self.full_name = full_name
        self.short_name = short_name
        self.birthday = birthday
        self.age = date.today().year - birthday.year - ((date.today().month, date.today().day) < (birthday.month,
                                                                                                  birthday.day))
        self.email = email

    def __str__(self):
        return f'Name: {self.full_name}, birthday: {self.birthday}'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.short_name

    def get_age(self):
        return self.age


def main():

    users = []

    while True:
        print("==========================================")
        menu = input("Please, choose an operation:\n\t"
                     "1. Create new or re-write existing database (!Existing db will be lost)\n\t"
                     "2. Add new person to the database\n\t"
                     "3. Find someone in the database\n\t"
                     "4. Show entire database\n\t"
                     "0. Exit\n>> ")
        print("==========================================")
        match menu:
            case "1":
                create_db()
            case "2":
                print('Please indicate data of the person')

                # getting info from user
                first_name = input("First name: ").title()
                last_name = input("Last name: ").title()
                father_name = input("Last name (if None just hit ENTER): ").title()
                birthday = input("Birthday (YYYY,m,d): ")
                email = input("Email: ")

                # preparing data
                birthday_year, birthday_month, birthday_day = map(int, birthday.split(','))
                birth_date = date(birthday_year, birthday_month, birthday_day)

                # adding person to the database
                if father_name:
                    add_person(first_name, last_name, birthday, email, father_name)
                    full_name = last_name + " " + first_name + " " + father_name
                    short_name = last_name + " " + first_name[0] + ". " + father_name[0] + "."
                else:
                    add_person(first_name, last_name, birthday, email)
                    full_name = last_name + " " + first_name
                    short_name = last_name + " " + first_name[0] + "."

                # not necessary but just to check and print - creating an instance of User
                new_user = User(full_name, short_name, birth_date, email)
                print('The following person has been added to the database:')
                print(new_user)
                print(f'{new_user.get_short_name()} is {new_user.get_age()} years old')

            case "3":
                finder = input("How do you want to search?\n\t"
                             "1. By name\n\t"
                             "2. By surname\n\t"
                             "3. By email\n")
                if finder == '1':
                    first_name = input("Enter name to search: ").title()
                    find_user(name=first_name)
                elif finder == '2':
                    last_name = input("Enter surname to search: ").title()
                    find_user(surname=last_name)
                elif finder == '3':
                    email = input("Enter email to search: ")
                    find_user(email=email)
                else:
                    print('No search parameters')

            case "4":
                show_db()

            case "0":
                print("Good bye")
                break
            case _:
                print("Please choose from the menu items (1, 2, 3, 4, or 0)")


def create_db():
    connection = sqlite3.connect('People.db')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS People")

    table = """
    CREATE TABLE People (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        father_name TEXT,
        birthday DATE,
        email TEXT NOT NULL
    );
    """

    cursor.execute(table)
    print("People table is created")
    cursor.close()
    connection.close()


def show_db():
    connection = sqlite3.connect('People.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * from People")
    names = [description[0] for description in cursor.description]
    print(names)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()


def add_person(first_name, last_name, birthday, email, father_name='None'):
    try:
        connection = sqlite3.connect('People.db')
        cursor = connection.cursor()
    except:
        print("Database hasn't created yet")
        return None

    request = """INSERT INTO People(first_name, last_name, father_name, birthday, email)
              VALUES('""" + first_name + "','" + last_name + "','" + father_name + "','" + birthday + "','" + email + "')"

    cursor.execute(request)
    connection.commit()
    print("People table has been updated")
    cursor.close()
    connection.close()


def find_user(name=None, surname=None, email=None):
    try:
        connection = sqlite3.connect('People.db')
        cursor = connection.cursor()
    except:
        print("Database hasn't created yet")
        return None

    if name:
        request = "SELECT * FROM People WHERE first_name = " + "'" + name + "'"
        cursor.execute(request)
        result = cursor.fetchall()
        names = [description[0] for description in cursor.description]
        print(names)
        print(result)
    elif surname:
        request = "SELECT * FROM People WHERE last_name = " + "'" + surname + "'"
        cursor.execute(request)
        result = cursor.fetchall()
        names = [description[0] for description in cursor.description]
        print(names)
        print(result)
    elif email:
        request = "SELECT * FROM People WHERE email = " + "'" + email + "'"
        cursor.execute(request)
        result = cursor.fetchall()
        names = [description[0] for description in cursor.description]
        print(names)
        print(result)
    else:
        print('Search parameters should not be empty')


def greeting_email(self):
    pass


if __name__ == "__main__":
    main()
