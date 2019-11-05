import requests

addr = 'https://swapi.co/api/people/'

requests.get(addr)

r = requests.get(addr)

for i in r.json()['results']:
    print(i['name'])