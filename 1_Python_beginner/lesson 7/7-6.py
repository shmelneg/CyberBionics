from collections import OrderedDict

library = {"J. K. Rowling": "Harry Potter",
           "Jane Austen": "Pride and Prejudice",
           "Harper Lee": "To Kill a Mockingbird",
           "Scott Fitzgerald": "Great Gatsby",
           "Miguel De Cervantes": "Don Quixote"
            }
print("The books in the library:", library)

while True:
    choice = input("Choose what you want to do:\n\t1. Add or edit book\n\t2. Sort by author\n\t3. Sort by title\n\t"
                   "or enter any other key to exit\n?> ")
    if choice == "1":
        author = input("Enter the author: ")
        title = input("Enter the title: ")
        library[author] = title
        print("The updated library:", library)
    elif choice == "2":
        new_a = OrderedDict(sorted(library.items()))
        print(new_a)
    elif choice == "3":
        new_t = OrderedDict(sorted(library.items(), key = lambda t: t[1]))
        print(new_t)
    else:
        break
