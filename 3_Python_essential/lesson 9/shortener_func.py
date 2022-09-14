def main():
    links = {"test1": "https://uk.test1.org",
             "test2": "https://www.test2.com",
             "test3": "https://www.test3.com"
             }
    get_link(links)
    add_link(links)
    print(links)


def get_link(database):
    print("We have the following sites in the database:", database.keys())
    request = input("Please enter the site that link you want to get: ").lower()
    if request in database.keys():
        print("Press this link", database[request])
    else:
        print("Sorry, can't find it in our base")


def add_link(database):
    site = (input("Enter a short name for the site you want to add: ")).lower()
    link = (input("Enter the site full link (https://*****.***): ")).lower()
    database[site] = link
    print("The link has been added.")


if __name__ == "__main__":
    main()
