class Employee:

    def __init__(self):
        # getting first name
        while True:
            self.name = input("Employee's first name: ")
            if self.name.isalpha():
                break
            else:
                print("You should use only alphabetical symbols for the name. Let's try again.")
        # getting second name
        while True:
            self.surname = input("Employee's second name: ")
            if self.surname.isalpha():
                break
            else:
                print("You should use only alphabetical symbols for the name. Let's try again.")
        # getting the hiring year
        while True:
            try:
                self.start_year = int(input("The year when this employee was hired (YYYY): "))
            except ValueError:
                print("Please enter the year by 4 digits")
            if 2010 <= self.start_year <= 2022:
                break
            else:
                print("You cannot put a year before our company was incorporated (2010) of after the current year")
        # getting the department
        while True:
            answer = input("Choose the employee's department code: 1 for Management, 2 for HR, 3 for Sales\n>> ")
            if answer == "1":
                self.department = "Management"
                break
            elif answer == "2":
                self.department = "HR"
                break
            elif answer == "3":
                self.department = "Sales"
                break
            else:
                print("You need to indicate code 1, 2 or 3")

    def __str__(self):
        return f"{self.name} {self.surname} (works in {self.department})"

    def __repr__(self):
        return f"{self.name} {self.surname} (works in {self.department})"


def main():
    employees = []
    while True:
        try:
            number_of_employees = int(input("How many employees are in your company? "))
            break
        except ValueError:
            print("You can put only numbers here")

    # creating a list of employees
    print("=Let's add your employees to the database=")
    for counter in range(number_of_employees):
        print(f">>adding employee number {counter + 1}>>")
        employee = Employee()
        employees.append(employee)

    # picking the employees hired since 2022
    print("=List of the employees hired this year=")
    for employee in employees:
        if employee.start_year == 2022:
            print(employee)


if __name__ == "__main__":
    main()
