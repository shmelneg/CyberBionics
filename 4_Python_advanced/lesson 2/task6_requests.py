import requests

response1 = requests.get('https://jsonplaceholder.typicode.com/')
response2 = requests.put('https://jsonplaceholder.typicode.com/')
response3 = requests.post('https://jsonplaceholder.typicode.com/')
response4 = requests.delete('https://jsonplaceholder.typicode.com/')
print(response1)
print(response2)
print(response3)
print(response4)
