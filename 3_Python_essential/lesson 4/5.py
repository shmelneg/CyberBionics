class CoachError(Exception):
    pass


def main():
    gym = [{"name": "Ivan", "surname": "Ivanov", "sport": "swimming", "time": "13:00-14:00", "price": 150},
           {"name": "Petro", "surname": "Petrov", "sport": "boxing", "time": "14:00-15:00", "price": 150},
           {"name": "Natasha", "surname": "Romanova", "sport": "ballet", "time": "17:00-18:30", "price": 300},
           {"name": "Stepan", "surname": "Bandera", "sport": "shooting", "time": "18:00-21:00", "price": 500}
           ]

    while True:
        menu = input("Please select menu item:\n\t1.Sports to choose\n\t2.Our Coaches\n\t3.Gym schedule\n\t"
                     "4.Training cost\n\t5.Find coach by their last name\n\t0.Exit\n>>")
        if menu not in ("1", "2", "3", "4", "5", "0"):
            print("Wrong number of the menu. Please choose some correct menu item")
            continue
        match menu:
            case "1":
                for coach in gym:
                    print(coach["sport"])
            case "2":
                for coach in gym:
                    print(f"{coach['name']} {coach['surname']}")
            case "3":
                for coach in gym:
                    print(f"{coach['time']} - {coach['sport']}")
            case "4":
                for coach in gym:
                    print(f"{coach['sport']} - {coach['price']} UAH per lesson")
            case "5":
                lastname = input("Input surname to search: ")
                try:
                    find_coach(gym, lastname)
                except CoachError:
                    print("Sorry, we couldn't find such such person among our coaches")
            case "0":
                break


def find_coach(gym, person):
    absent = True
    for coach in gym:
        if coach["surname"] == person:
            absent = False
            print(f"We've found your coach\n{coach['name']} {coach['surname']} trains {coach['sport']}"
                  f" at {coach['time']}. Lesson price is {coach['price']} UAH.")
            return None
    if absent:
        raise CoachError


if __name__ == "__main__":
    main()
