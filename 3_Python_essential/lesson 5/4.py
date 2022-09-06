class Contact:

    def __init__(self, surname="Doe", name="John", age=33, mob_phone="095-555-55-55", email="test@test.com"):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"{self.name} {self.surname} - {self.mob_phone}"

    def send_message(self):
        print(f"Sending message to {self.name} {self.surname} at {self.email}")


class UpdateContact(Contact):

    def __init__(self, surname="Doe", name="Jane", age=25, mob_phone="095-111-11-11", email="test2@test.com", job=None):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        print(f"{self.name}, you've got an email at {self.email}. Do you want to open it?")

contact1 = Contact()
contact2 = UpdateContact()

print(isinstance(contact1, Contact))
print(isinstance(contact2, Contact))
print(isinstance(contact1, UpdateContact))
print(isinstance(contact2, UpdateContact))
print()
print(issubclass(Contact, UpdateContact))
print(issubclass(UpdateContact, Contact))
