import requests

def getswapi(name):
    addr = 'https://swapi.co/api/people/'
    r = requests.get(addr)
    jsonData = r.json()['results']
    for i in jsonData:
        if i['name'] == name:
            return i
        else:
            text = "No Character Found"
            return text
