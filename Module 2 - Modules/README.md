# Importing Modules

Modules expose additional functionality to the baseline python capabilities. Virtually every method and function is accessed after importing a module. Take the following script block...

```python
import json
import os
import flask
import requests
```

In this block we are importing several modules that are commonly used.

The `import json` block allows us to manipulate and create JSON (JavaScript Object Notation) objects (more on that later.

The`import os` is something we can use to read in Operating System environment variables and much more!

The `import flask` block references access a web framework known as flask. We will be covering this platform in a much later tutorial, but if you want to skip ahead, no one is stopping you :) (http://flask.pocoo.org/)

The `import requests` block is one we will be using extensively as it allows you to interact with http requests.

## Access Environment Variables

We can use the `os` module to access environment variables that have been stored in the system. This might be connection URLs or other configuration items. Usernames and credentials are discouraged to be stored as environment variables; but are sometimes used in this way for environments.

As mentioned earlier, we use the os module via `import os` to access methods that support reading environment variables (among other items).

__In Bash__
```bash
export url='http://codyslab.com'
```
__In Python__
```python
import os
url = os.environ.get('url')
print(url)
```