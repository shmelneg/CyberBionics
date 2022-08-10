links = {
    "wikipedia": "https://uk.wikipedia.org",
    "google": "https://www.google.com",
    "netflix": "https://www.netflix.com"}

print("We have the following sites in the database:", links.keys())
request = input("Please enter the site that link you want to get: ").lower()

if request in links.keys():
    print("Press this link", links[request])
else:
    print("Sorry, can't find it in our base")
    