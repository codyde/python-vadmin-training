# Bringing It All Together

We've learned the basic building blogs of Python scripts at this point. In this lesson we'll work on connecting to a REST endpoint using Python.

The example functions within this folder perform a few useful items. 

## Function for Authenticating to vCenter

```python
def authvc(api_url,user,password):
    r = requests.post(f'{api_url}/rest/com/vmware/cis/session', auth=(user,password), verify=False)
    if r.status_code == 200:
        print("Authentication Success")
        return r.json()['value']
    else:
        print("You didn't say the magic word")
        return print("Fail")
```

We create a function named `authvc()` that takes in the API url, user, and password as required components. We use the `requests` module, with some of its built in methods to handle creating the authentication. We use if/then statements to determine if the authentication was successful and tell the user one way or another.

The pattern of using if/then statements to determine if a call is successful is a very common pattern that you should keep note of!

## Function For Calling vCenter API's

```python
def getapidata(path):
    sid = authvc('https://hlcorevc01.humblelab.com',os.environ['user'],os.environ['password'])
    r = requests.get(f'https://hlcorevc01.humblelab.com/rest{path}', headers={'vmware-api-session-id':sid}, verify=False)
    print(r.json())
    if r.status_code == 200:
        return r.json()
    else: 
        return print("Failure with Status Code "+r.status_code)
```

In this function, we use our previous function to obtain our authentication SID. This function takes an input of the API's path we want to call (for example, `/vcenter/vm`). We use if/then statements to handle if the call was successful - and return the results of the API call.
