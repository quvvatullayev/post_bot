import requests

url = 'http://localhost:5000'

data = requests.post(url)

print(data.json())