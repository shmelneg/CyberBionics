import json

my_dict = {
    "name": "Andrii",
    "surname": "Melnyk",
    "age": 39,
    "course": "Python"
}

with open("profile.json", "w") as outfile:
    json.dump(my_dict, outfile)
