"""This script Requests to one of the URL of of our Django App and
shows the Respose.
"""
'''
"""For sending a Request with a string data to the server"""
import requests

# URL to the Django inbuilt server.
# url = 'http://127.0.0.1:8000/test_app/'
# URL to the Apache server.
url = 'http://127.0.0.1:80/test_app/'

data = {
    'first_number': 1,
    'second_number': 2
}

response = requests.post(url, data=data)

print(response)

print(response.content)
'''


"""For seding a Request with a file attached to it to server and getting 
a file as Response."""
import requests

# You must specify 'rb' parameter while opening the file.
f = open('hornet.jpeg', 'rb')

# url = 'http://127.0.0.1:8000/test_app/'
url = 'http://127.0.0.1:80/test_app/'

files = {
    'test_file': f,
}

# Pass the file dictionary as 'files' argument.
response = requests.post(url, files=files)

f.close()

# Getting the response code.
print(response)

# Getting the respose content.
print(response.content)

# Saving the returned file in Local Mahcine.
# f = open('returned_file.{}'.format('jpeg'), 'wb')
# f.write(response.content)
# f.close()
