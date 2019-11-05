import requests

addr = 'https://swapi.co/api/people/'

requests.get(url = addr)

r = requests.get(addr)

r.json()

r.json()['results']

jsonData = r.json()['results']

len(jsonData)