# Looping and Handling Multiple Objects

Thus far, we've been using the following api `https://swapi.co/api/people/{id}/` for calling data which requires an ID input to grab the character object.

We can pull all characters from the api using the following URL - `https://swapi.co/api/people`.

```python
url = 'https://swapi.co/api/people'
chars = requests.get(url)
chars.json()
```

When we return this we actually get a very different object from before. This list is paginated, and only the first set of objects is shown. We can see in our response. Maybe a good challenge exercise would be writing a function that lists all of them?

Back to the topic at hand, we can see that this JSON object is behind several objects. If we look at the keys (or plug them into a parser like https://jsoneditoronline.org/) we can see that the data we care about is behind a "results" key. Lets update our call. Note, this call will only return the first page.

```python
url = 'https://swapi.co/api/people'
chars = requests.get(url)
chars.json()['results']
```

Thats better, now we're getting our main content! What if we want to just return character names? We can handle this with a loop!

```python
url = 'https://swapi.co/api/people'
chars = requests.get(url)
for i in chars:
    print(i['name'])
```

You can see we're initiating a `for` statement, and declaring `i`. That `i` ends up being a placeholder variable that is going to change as we move through all objects in the object - in this case, the chars object.

Finally, what if we wanted to create a new JSON object that held all of these names? We can easily do that by constructing a new JSON object!

```python
names = []
url = 'https://swapi.co/api/people'
chars = requests.get(url)
for i in chars: 
    namedata = {}
    namedata['name'] =  i['name']
    names.append(namedata)
print(names)
```

Success! We can see our final returned JSON is a new object consisting of all of the characters from the first page, in a new JSON object.
