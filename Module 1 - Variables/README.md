# Creating Variables

Variables are values stored within memory behind an identifier. Python is an object oriented programming language, which means we will be frequently creating variables that represent objects, and then interacting with that object. As an example, we will call the Star Wars API and store the connection as a variable (later in this training). The connection itself is an OBJECT, and using the variable, we are able to execute functions and methods against the object.

Creating variables is easy!

```python
a = "Cody's Variable"
b = "Grant's Variable"
c = "Chris Slater doesn't get a variable"
```

Theses variables are all "string" variables, meaning simple words. Objects are another matter, but often created in the same way, we will come back to those later! 

## Printing Data

In Python3 the syntax for printing (returning data to the screen) has changed. We can print data back by either referencing a variable, or directly calling a string or number. For example...

```python
print('hello world!')
a = 'hello VMware'
print(a)
```

## Concatenation and F Strings

### Concatenation

We can build strings in multiple ways using Python. Common paths are concatenating strings and using F Strings.

An example of concatenation is a statement like the below...

```python
a = 'My name is Cody'
b = 'His name is Kyle'
finalString = a + ' ' + b
print(finalString)
```

Notice that I concatenate a space in. The strings will join immediately after one and other. This can create some strangely structured sentences in some cases :)

### F Strings

F Strings can help you keep your code clean, but can also help when you are bringing in strings that have complicated characters in them.

We can use F Strings like the below...

```python
a = 'My name is Cody'
b = 'His name is Kyle'
finalString = f'{a} {b}'
print(finalString)
```

Or in a more practical example...

```python
vmid = 'vm-1123'
addr = f'https://vcenteraddress.domain.local/api/vcenter/vm/{vmid}'
print(addr)
```
