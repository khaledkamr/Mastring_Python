# Counter
The counter is a container included in the `collections module`. Now you all must be wondering what is a container. Don’t worry first let’s discuss the container.

## What is Container?
Containers are objects that hold objects. They provide a way to access the contained objects and iterate over them. Examples of built-in containers are Tuples, lists, and dictionaries. Others are included in the Collections module.
A Counter is a subclass of dict. Therefore it is an unordered collection where elements and their respective count are stored as a dictionary. This is equivalent to a bag or multiset of other languages.

## Syntax 
```
class collections.Counter([iterable-or-mapping])
```
### Initialization: 

The constructor of the counter can be called in any one of the following ways:

- With a sequence of items
- With a dictionary containing keys and counts
- With keyword arguments mapping string names to counts

## Initializing a Counter
```python []
# A Python program to show different ways to create
# Counter
from collections import Counter
 
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
 
# with dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
 
# with keyword arguments
print(Counter(A=3, B=5, C=2))
```
#### Output:
```
Counter({'B': 5, 'A': 3, 'C': 2})
Counter({'B': 5, 'A': 3, 'C': 2})
Counter({'B': 5, 'A': 3, 'C': 2})
```
## Updation in counters

### We can also create an empty counter in the following manner : 
```
coun = collections.Counter()
```
### And can be updated via the update() method. The syntax for the same : 
```
coun.update(Data)
```
``` python []
# A Python program to demonstrate update()
from collections import Counter
coun = Counter()
 
coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)
 
coun.update([1, 2, 4])
print(coun)
```
#### Output:
```
Counter({1: 4, 2: 3, 3: 1})
Counter({1: 5, 2: 4, 3: 1, 4: 1}
```
## Subtract two Counters
### Data can be provided in any of the three ways as mentioned in initialization and the counter’s data will be increased not replaced.Counts can be zero or negative also.
```python []
# Python program to demonstrate that counts in 
# Counter can be 0 and negative
from collections import Counter
 
c1 = Counter(A=4,  B=3, C=10)
c2 = Counter(A=10, B=3, C=4)
 
c1.subtract(c2)
print(c1)
```
#### Output:
```
Counter({'c': 6, 'B': 0, 'A': -6})
```
## Distinct Count in the list
### We can use Counter to count distinct elements of a list or other collections. 
```python []
# An example program where different list items are
# counted using counter
from collections import Counter
 
# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
 
# Count distinct elements and print Counter aobject
print(Counter(z))
```
#### Output:
```
Counter({'blue': 3, 'red': 2, 'yellow': 1})
```
## Printing Counter Values
### We can also access all the keys and values of a counter using the keys(), values(), and items() methods. These methods return views of the keys, values, and key-value pairs in the counter, respectively. 
```python []
from collections import Counter
my_counter = Counter('abracadabra')
print(my_counter.keys()) 
print(my_counter.values()) 
print(my_counter.items()) 
```
#### Output:
```
dict_keys(['a', 'b', 'r', 'c', 'd'])
dict_values([5, 2, 2, 1, 1])
dict_items([('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])
```
If you want to learn more about accessing counters in Python, the article  [(Accessing Counters)](https://www.geeksforgeeks.org/counters-in-python-set-2-accessing-counters) is a great resource.

