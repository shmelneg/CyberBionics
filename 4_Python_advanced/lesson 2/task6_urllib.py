from urllib import request

response = request.urlopen('https://jsonplaceholder.typicode.com/')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
print(response.headers)
print(response.getheaders())
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))
print(response.headers.get('Expires'))
print(response.getheader('Expires'))
