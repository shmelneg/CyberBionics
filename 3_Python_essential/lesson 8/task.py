def read_file():
    with open('contact.txt', "r", encoding="UTF-8") as file:
        for line in file:
            print(line)


def write_file():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    with open('contact.txt', "w") as file:
        file.writelines(f"{first_name} {last_name}\nemail address: {email}")


while True:
    print("===================================================================================================")
    menu = input("Choose menu option:\n\t1.(re)Write your contact info\n\t2.Read your contact info\n\t0.Exit\n"
                 "Make your choice (input 1, 2, or 0): ")
    print("===================================================================================================")
    if menu == "1":
        write_file()
    elif menu == "2":
        read_file()
    elif menu == "0":
        break
    else:
        print("Invalid command. Input 1, 2, or 0")
