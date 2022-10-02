import csv
import json


def main():
    while True:
        menu = input("Please make your choice:\n\t1. Rewrite staff database\n\t2. Add new profile to the existing "
                     "database\n\t3. Show all profiles\n\t4. Convert database to XML\n\t5. Convert database to "
                     "JSON\n\t0. Exit\n>> ")
        match menu:
            case "1":
                create_database()
                add_person()
            case "2":
                add_person()
            case "3":
                read_all()
            case "4":
                csv_to_xml()
            case "5":
                csv_to_json()
            case "0":
                print("Good bye")
                break
            case _:
                print("Please choose from the menu items (1, 2, 3, 4, 5, or 0)")


def create_database():
    header = ['name', 'surname', 'birthday', 'city']
    with open('staff.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)


def add_person():
    data = []
    name = input("First Name: ")
    data.append(name)
    surname = input("Last Name: ")
    data.append(surname)
    birthday = input("Birthday: ")
    data.append(birthday)
    city = input("City: ")
    data.append(city)

    with open('staff.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


def read_all():
    with open('staff.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


def csv_to_xml():

    def convert_row(headers, row):
        s = f'<row id="{row[0]}">\n'
        for header, item in zip(headers, row):
            s += f'    <{header}>' + f'{item}' + f'</{header}>\n'
        return s + '</row>'

    with open('staff.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        xml = '<data>\n'
        for row in reader:
            xml += convert_row(headers, row) + '\n'
        xml += '</data>'
        with open("staff.xml", "w") as xmlfile:
            xmlfile.write(xml)


def csv_to_json():
    data = []

    with open('staff.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open('staff.json', 'w') as jsonfile:
        json_data = json.dumps(data, indent=4)
        jsonfile.write(json_data)


if __name__ == "__main__":
    main()
