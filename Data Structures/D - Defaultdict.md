# Defaultdict
Dictionary in Python is an unordered collection of data values that are used to store data values like a map. Unlike other Data Types that hold only single value as an element, the Dictionary holds key-value pair. In Dictionary, the key must be unique and immutable. This means that a Python Tuple can be a key whereas a Python List can not. A Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’.


### Example:

```python []
# Python program to demonstrate
# dictionary

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("Dictionary:") 
print(Dict)
print(Dict[1])

# Uncommenting this print(Dict[4])
# will raise a KeyError as the
# 4 is not present in the dictionary
```
### Output:
```
Dictionary:
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
Geeks
```
```
Traceback (most recent call last):
  File "/home/1ca83108cc81344dc7137900693ced08.py", line 11, in 
    print(Dict[4])
KeyError: 4
```
Sometimes, when the KeyError is raised, it might become a problem. To overcome this Python introduces another dictionary like container known as Defaultdict which is present inside the collections module.
Note: For more information, refer to Python Dictionary.
 

## DefaultDict

Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
```
Syntax: defaultdict(default_factory)
Parameters:  

- default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
```
### Example:

```python []
# Python program to demonstrate
# defaultdict

from collections import defaultdict

# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"
    
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
```
#### Output:
```
1
2
Not Present 
```
## Inner Working of defaultdict
Defaultdict adds one writable instance variable and one method in addition to the standard dictionary operations. The instance variable is the default_factory parameter and the method provided is __missing__.

- Default_factory: It is a function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
Example:
```python []
# Python program to demonstrate
# default_factory argument of 
# defaultdict

from collections import defaultdict

# Defining the dict and passing 
# lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
```
#### Output:
```
1
2
Not Present
```
- \_\_missing__(): This function is used to provide the default value for the dictionary. This function takes default_factory as an argument and if this argument is None, a KeyError is raised otherwise it provides a default value for the given key. This method is basically called by the \_\_getitem__() method of the dict class when the requested key is not found. \_\_getitem__() raises or return the value returned by the \_\_missing__(). method.

### Example:
```python []
# Python program to demonstrate
# defaultdict

from collections import defaultdict

# Defining the dict
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

# Provides the default value 
# for the key
print(d.__missing__('a'))
print(d.__missing__('d'))
```
#### Output:
```
Not Present
Not Present
```
## Using List as default_factory
When the list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.

### Example:

```python []
# Python program to demonstrate
# defaultdict

from collections import defaultdict

# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)
    
print("Dictionary with values as list:")
print(d)
```
#### Output:
```
Dictionary with values as list:
defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})
```
## Using int as default_factory
When the int class is passed as the default_factory argument, then a defaultdict is created with default value as zero.
### Example:

```python []
# Python program to demonstrate
# defaultdict 
 
from collections import defaultdict
 
# Defining the dict
d = defaultdict(int)
 
L = [1, 2, 3, 4, 2, 4, 1, 2]
 
# Iterate through the list
# for keeping the count
for i in L:
     
    # The default value is 0
    # so there is no need to 
    # enter the key first
    d[i] += 1
     
print(d)
```
### Output:
```
defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})
```

## Defaultdict in Python – FAQs
### What is Defaultdict in Python Keyerror?
```
Defaultdict is a subclass of Python’s built-in dict class. It overrides the __missing__ method to provide a default value for missing keys, preventing KeyError. If a key is not found in the dictionary, defaultdict automatically inserts it with a default value.
```
### What is Defaultdict subclass in Python?
```
defaultdict is a subclass of the dict class in Python, found in the collections module. It allows you to specify a default factory function that provides default values for missing keys.
```
```python
from collections import defaultdict
# Example with list as the default factory
dd = defaultdict(list)
dd['missing_key'].append(1)
print(dd)  # Output: defaultdict(<class 'list'>, {'missing_key': [1]})
```
### What is the difference between Setdefault and Defaultdict in Python?
```
setdefault is a method of the dict class. It inserts a key with a specified default value if the key is not already present.
```
```python
d = {}
d.setdefault('key', []).append(1)
print(d)  # Output: {'key': [1]}
defaultdict is a subclass of dict that provides a default value for a missing key without explicitly checking for its presence.
from collections import defaultdict
dd = defaultdict(list)
dd['key'].append(1)
print(dd)  # Output: defaultdict(<class 'list'>, {'key': [1]})\
```
### What is the difference between Defaultdict and dict in Python typing?
```
Dict: A standard dictionary without automatic default values for missing keys.
```
```python 
d = {}
# Accessing a missing key will raise KeyError
defaultdict: A dictionary with a default factory function that automatically creates values for missing keys.
from collections import defaultdict
dd = defaultdict(int)
# Accessing a missing key will return 0 (default value provided by int())
Why we use Setdefault in Python?
setdefault is used to insert a key with a default value if the key is not already in the dictionary. This is useful for avoiding repeated key existence checks and manual insertion.

d = {}
d.setdefault('key', []).append(1)
d.setdefault('key', []).append(2)
print(d)  # Output: {'key': [1, 2]}
```