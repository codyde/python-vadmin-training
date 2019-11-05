import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from prettytable import PrettyTable
    
def authvc(api_url,user,password):
    r = requests.post(f'{api_url}/rest/com/vmware/cis/session', auth=(user,password), verify=False)
    if r.status_code == 200:
        print("Authentication Success")
        return r.json()['value']
    else:
        print("You didn't say the magic word")
        return print("Fail")

def getapidata(path):
    sid = authvc('https://hlcorevc01.humblelab.com',os.environ['user'],os.environ['password'])
    r = requests.get(f'https://hlcorevc01.humblelab.com/rest{path}', headers={'vmware-api-session-id':sid}, verify=False)
    if r.status_code == 200:
        return r.json()
    else: 
        return print("Failure with Status Code "+r.status_code)


def gettable():
    x = PrettyTable()
    x.field_names = ['Name','Memory','CPU','Power']
    for i in getapidata('/vcenter/vm')['value']:
        x.add_row([i['name'],i['memory_size_MiB'],i['cpu_count'],i['power_state']])
    print(x)    
    return
