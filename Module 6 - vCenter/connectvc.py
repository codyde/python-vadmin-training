import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    print(r.json())
    if r.status_code == 200:
        return r.json()
    else: 
        return print("Failure with Status Code "+r.status_code)

def lightswitch(vmname):
    data = getapidata('/vcenter/vm')
    sid = authvc('vcenterhere',os.environ['user'],os.environ['password'])
    for i in data['value']:
        if i['name'] == vmname:
            id = i['vm']
            print("The ID for this VM is "+id)
            pstate = requests.get(f'https://hlcorevc01.humblelab.com/rest/vcenter/vm/{id}/power', headers={'vmware-api-session-id':sid}, verify=False)
            print("Power State Data is as follows "+pstate.json()['value']['state'])
            if pstate.json()['value']['state'] == 'POWERED_OFF':
                state = requests.post(f'https://hlcorevc01.humblelab.com/rest/vcenter/vm/{id}/power/start', headers={'vmware-api-session-id':sid}, verify=False)
                print("Starting VM")
                return state.status_code
            else:
                state = requests.post(f'https://hlcorevc01.humblelab.com/rest/vcenter/vm/{id}/power/stop', headers={'vmware-api-session-id':sid}, verify=False)
                print("Stopping VM")
                return state.status_code