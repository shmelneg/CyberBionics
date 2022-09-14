import shelve


with shelve.open("shortener") as links:
    while True:
        print("===================================================================================================")
        menu = input("Choose menu option:\n\t1.Get the link\n\t2.Store your link\n\t0.Exit\n"
                     "Make your choice (input 1, 2, or 0): ")
        print("===================================================================================================")
        if menu == "1":
            print("We have the following sites in the database:", list(links.keys()))
            request = input("Please enter the site that link you want to get: ").lower()

            if request in links.keys():
                print("Press this link", links[request])
            else:
                print("Sorry, can't find it in our base")
        elif menu == "2":
            site = (input("Enter a short name for the site you want to add: ")).lower()
            link = (input("Enter the site full link (https://*****.***): ")).lower()
            links[site] = link
            print("The link has been added.")
        elif menu == "0":
            break
        else:
            print("Invalid command. Input 1, 2, or 0")
