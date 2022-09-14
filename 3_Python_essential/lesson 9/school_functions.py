def main():
    schedule()
    teachers()
    library()


def schedule():
    week = {"Monday": "09-00 - 14:30",
            "Tuesday": "09-30 - 15:00",
            "Wednesday": "09-00 - 13:30",
            "Thursday": "09-00 - 14:30",
            "Friday": "10-00 - 15:00",
            "Saturday": "Day-off",
            "Sunday": "Day-off"
            }
    for day in week:
        print(day, "->", week[day])


def teachers():
    staff = {"John Doe": "math",
             "Jane Doe": "physics",
             "Adam Smith": "economy"}
    for teacher in staff:
        print(teacher, "is a", staff[teacher], "teacher")


def library():
    books = {"Gabriel García Márquez": "One Hundred Years of Solitude",
             "Erich Maria Remarque": "All Quiet on the Western Front",
             "Stephen Hawking": "A Brief History of Time",
             "J.D. Salinger": "The Catcher in the Rye"}
    for book in books:
        print(books[book], "-by-", book)


if __name__ == "__main__":
    main()
