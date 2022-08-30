class Editor:

    def view_document(self, document):
        print(document)

    def edit_document(self, document):
        print("This function is unavailable in free version")


class ProEditor(Editor):

    def edit_document(self, document):
        print("Let's edit this:\n", document)


document = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip " \
           "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore " \
           "eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia " \
           "deserunt mollit anim id est laborum."

license_key = "QRG7T-8RHQY-B4CVX-R8MWM-W43BT"

user_key = input("Please enter the license key: ")
if user_key == license_key:
    my_app = ProEditor()
    print("You have a pro version")
else:
    my_app = Editor()
    print("You have a free version")

my_app.view_document(document)
my_app.edit_document(document)
