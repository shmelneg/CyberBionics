import school_functions as school


def main():
    while True:
        print("===================================================================================================")
        menu = input("Choose menu option:\n\t1. Lessons schedule\n\t2. List of the teachers\n\t3. Library\n\t4. Exit\n"
                     "Make your choice (input 1, 2, 3 or 4): ")
        print("===================================================================================================")
        if menu == "1":
            school.schedule()
        elif menu == "2":
            school.teachers()
        elif menu == "3":
            school.library()
        elif menu == "4":
            break
        else:
            print("Invalid command. Input 1, 2, 3, or 4")


if __name__ == "__main__":
    main()
