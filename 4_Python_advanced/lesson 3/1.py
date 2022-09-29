import json

data = {'first_name': 'Andrii', 'last_name': 'Melnyk', 'age': 39}

with open('output.json', 'w') as file:
    json.dump(data, file)

with open('output.json', 'r') as file:
    output = json.load(file)
    print(output)