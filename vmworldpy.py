import requests
import os

def authvc(api_url,user,password):
    r = requests.post(f'{api_url}/rest/com/vmware/cis/session', auth=(user,password), verify=False)
    if r.status_code == 200:
        print("Authentication Success")
        return r.json()['value']
    else:
        print("You didn't say the magic word")
        return print("Fail")

def getapidata(path):
    sid = authvc('https://vcenter.sddc-34-218-57-180.vmc.vmware.com',os.environ['user'],os.environ['password'])
    r = requests.get(f'https://vcenter.sddc-34-218-57-180.vmc.vmware.com/rest{path}', headers={'vmware-api-session-id':sid}, verify=False)
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
            pstate = requests.get(f'vcenterhere/rest/vcenter/vm/{id}/power', headers={'vmware-api-session-id':sid}, verify=False)
            print("Power State Data is as follows "+pstate.json()['value']['state'])
            if pstate.json()['value']['state'] == 'POWERED_OFF':
                state = requests.post(f'vcenterhere/rest/vcenter/vm/{id}/power/start', headers={'vmware-api-session-id':sid}, verify=False)
                print("Starting VM")
                return state.status_code
            else:
                state = requests.post(f'vcenterhere/rest/vcenter/vm/{id}/power/stop', headers={'vmware-api-session-id':sid}, verify=False)
                print("Stopping VM")
                return state.status_code

def deletevm(vmname):
    data = getapidata('/vcenter/vm')
    sid = authvc('vcenterhere',os.environ['user'],os.environ['password'])
    for i in data['value']:
        if i['name'] == vmname:
            id = i['vm']
            print("The ID for this VM is "+id)
            pstate = requests.get(f'vcenterhere/rest/vcenter/vm/{id}/power', headers={'vmware-api-session-id':sid}, verify=False)
            print("Power State Data is as follows "+pstate.json()['value']['state'])
            if pstate.json()['value']['state'] == 'POWERED_OFF':
                state = requests.delete(f'vcenterhere/rest/vcenter/vm/{id}', headers={'vmware-api-session-id':sid}, verify=False)
                print("Deleting VM")
                return state.status_code
            else:
                state = requests.post(f'vcenterhere/rest/vcenter/vm/{id}/power/stop', headers={'vmware-api-session-id':sid}, verify=False)
                delete = requests.delete(f'vcenterhere/rest/vcenter/vm/{id}', headers={'vmware-api-session-id':sid}, verify=False)
                print("Stopping VM")
                return state.status_code
