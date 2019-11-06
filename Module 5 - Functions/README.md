# Simple Functions

Functions allow us to create reusable code that can be used throughout python scripts. They also provide better capabilities around error and failure handling as well as promote reusability. Let's use the tricks we've learned so far in an example! Functions should have a couple of key components...

* A defined function name (required, for obvious reasons)
* Inputs (optional)
* Return statement

```python
import os

def examplefunction():
    a = 'Codys Function'
    url = os.environ.get('url')
    b = a + ' is at the address ' + url
    print(b)
    return b
```

We've done a few things in this example

* Imported our OS module
* Defined our examplefunction() which has no arguments
* Defined variables inside our function (both static, and from an environment variable)
* Concatenated values from other variables into a new variable
* Printed the variable
* Returned the final value

What if we wanted to include arguments? We can do this by placing the argument names within the function definition.

```python
def examplefunction(url):
    a = 'Grants Function'
    b = a + ' is at the address ' + url
    print(b)
    return b

examplefunction('http://grantslab.com')
```

In this example we feed in a value (url) which is used to construct another variable. This looks pretty ugly. Lets reintroduce an earlier concept... F STRINGS!

```python
def examplefunction(description):
    a = f'Chris has a {description} statement of work'
    print(a)
    return a

examplefunction('ugly')
```

Using F Strings we can feed our value directly into a string. In this case, we have not only simplified the code, but also made it more readable. At the end, our function executes, calling Chris's Slaters statement of work ugly. Poor Chris.