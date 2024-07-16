# Namedtuple

Python supports a type of container dictionary called “namedtuple()” present in the module “collections“. In this article, we are going to see how to Create a NameTuple and operations on NamedTuple.

## What is NamedTuple in Python?
In Python, NamedTuple is present inside the collections module. It provides a way to create simple, lightweight data structures similar to a class, but without the overhead of defining a full class. Like dictionaries, they contain keys that are hashed to a particular value. On the contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

### Python NamedTuple Syntax
```
namedtuple(typename, field_names)
- typename – The name of the namedtuple.
- field_names – The list of attributes stored in the namedtuple.
```
Example: Code implementation of NamedTuple is shown in Python.

```python []
# Python code to demonstrate namedtuple()
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
```
#### Output
```
The Student age using index is : 19
The Student name using keyname is : Nandini
```
## Operations on NamedTuple
Below are the following operations that can done by using namedtuple():

- Create a NameTuple
- Access Operations
- Conversion Operations
- Additional Operations
### Create a NameTuple in Python
This creates a new namedtuple class using the namedtuple() function from the collections module. The first argument is the name of the new class, and the second argument is a list of field names.

```python 
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p.x, p.y) 
```
#### Output
```
1 2
```
## Access Operations
Namedtuples in Python provide convenient ways to access their fields. Below are some access operations provided in Python for NamedTuple:

- Access by index
- Access by keyname
- Access Using getattr()
### Access By Index
The attribute values of namedtuple() are ordered and can be accessed using the index number unlike dictionaries which are not accessible by index. In this example, we are accessing the student’s by using index.

```python 
# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])
```
#### Output
```
The Student age using index is : 19
```
### Access by keyname
Access by keyname is also allowed as in dictionaries. In this example, we are using keyname to access the student’s name.

```python
# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
```
#### Output
```
The Student name using keyname is : Nandini
```
### Access Using getattr()
This is yet another way to access the value by giving namedtuple and key value as its argument. In this example, we are using getattr() to access the student’s id in the given namedtuple.

```python 
# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))
```
### Output
```
The Student DOB using getattr() is : 2541997
```
## Conversion Operations
Namedtuples provide a few useful conversion operations to work with other data types in Python. Below are the following conversion operations that is provided for namedtuples in Python:

- Using _make()
- Using _asdict()
- Using “**” (double star) operator
### Conversion Using _make()
This function is used to return a namedtuple() from the iterable passed as argument. In this example, we are using _make() to convert the list “li” into namedtuple.

```python
# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))
```
#### Output
```
The namedtuple instance using iterable is  : 
Student(name='Manjeet', age='19', DOB='411997')
```
### Conversion Operation Using _asdict()
This function returns the OrderedDict() as constructed from the mapped values of namedtuple(). In this example, we are using _asdict() to convert the input list into namedtuple instance.

```python
import collections
# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())
```
#### Output
```
The OrderedDict instance using namedtuple is  : 
OrderedDict([('name', 'Nandini'), ('age', '19'), ('DOB', '2541997')])
```
### Using “**” (double star) operator
This function is used to convert a dictionary into the namedtuple(). In this example, we are using “**” to convert the input list into namedtuple.

```python 
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))
```
#### Output
```
The namedtuple instance from dict is  : 
Student(name='Nikhil', age=19, DOB='1391997')
```
## Additional Operations 
There are some additional operations that are provided in Python for NamedTuples:

- _fields
- _replace()
- \_\_new__()
- \_\_getnewargs__()

### _fields
This data attribute is used to get all the keynames of the namespace declared. In this example, we are using _fields to get all the keynames of the namespace declared.

```python
import collections
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(S._fields)
```
#### Output
```
All the fields of students are : 
('name', 'age', 'DOB')
```
### _replace()
_replace() is like str.replace() but targets named fields( does not modify the original values). In this example, we are using _replace() to replace a name from “Nandini” to “Manjeet”.

```python 
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', 
                           ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# ._replace returns a new namedtuple, 
# it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='Manjeet'))
```
#### Output
```
returns a new namedtuple : 
Student(name='Manjeet', age='19', DOB='2541997')
```
### \_\_new__()
This function returns a new instance of the Student class, by taking the values that we want to assign to the keys in the named tuple. In this example, we are using __new__() to return a new instance of the Student class.

```python
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Student.__new__ returns a new instance of Student(name,age,DOB)
print(Student.__new__(Student,'Himesh','19','26082003'))
```
#### Output
```
Student(name='Himesh', age='19', DOB='26082003')
```
### \_\_getnewargs__()
This function returns the named tuple as a plain tuple. In this example, we are doing the same by using __getnewargs__().

```python
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

H=Student('Himesh','19','26082003')
# .__getnewargs__ returns the named tuple as a plain tuple
print(H.__getnewargs__())
```
#### Output
```
('Himesh', '19', '26082003')
```