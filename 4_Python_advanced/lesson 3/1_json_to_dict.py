import json

with open("profile.json", "r") as outfile:
    data = json.load(outfile)
    print(data)
