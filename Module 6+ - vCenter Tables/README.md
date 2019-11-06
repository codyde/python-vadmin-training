# Fun With Pretty Tables

It's not always necessary to have Python return data in a programmatic fashion. Many people get started with Python for the purposes of building reporting. [PrettyTables](https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki) is great for this use case as it gives a very quick way to build tables to return data.

In this example, we can take the API data that returns and loop over it, placing it into a table.

```python
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
```

We use our functions from the previous example to authenticate to the vCenter API. We then create a new function that calls those previous functions to return the data and build our table.

In order to build a table, we need to instantiate the table as an object, and then populate the required data - namely the field names and the content of those fields.
