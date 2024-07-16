# Frozen set
Frozen sets in Python are immutable objects that only support 
methods and operators that produce a result without affecting 
the frozen set or sets to which they are applied. While elements 
of a set can be modified at any time, but elements of the frozen set 
remain the same after creation.
If no parameters are passed, it returns an empty frozenset.

# frozenset()
Python Method creates an immutable Set object from an iterable. 
It is a built-in Python function. As it is a set object, therefore, 
we cannot have duplicate values in the frozenset.

### frozenset() Syntax
```
Syntax : frozenset(iterable_object_name)
Parameter : iterable_object_name

This function accepts iterable object as input parameter.
Return :  Returns an equivalent frozenset object.
```
### Example
In this example, we are creating a frozen set with the list in Python.

```python []
animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals) 
print("elephant" in animals)  
```
#### Output
```
True
False
```
### Example
In this example, we are showing how that frozen set objects are immutable and can not be modified after the creation.
```python []
fruits = frozenset(["apple", "banana", "orange"])
print(fruits) 
fruits.append("peach")
print(fruits) 
```
#### Output
```
frozenset({'banana', 'orange', 'apple'})

AttributeError: 'frozenset' object has no attribute 'append'
```
If by mistake we want to change the frozen set object, then it throws a TypeError
```python []
# creating a list 
favourite_subject = ["OS", "DBMS", "Algo"]

# creating a frozenset
f_subject = frozenset(favourite_subject)

# below line will generate error
f_subject[1] = "Networking"
```
#### Output 
```
TypeError: 'frozenset' object does not support item assignment
```
### Frozenset operations
Frozen sets are immutable sets that allow you to perform various set operations such as union, intersection, difference, and symmetric difference.

```python []
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()
print(C)  

# union
union_set = A.union(B)
print(union_set) 

# intersection
intersection_set = A.intersection(B)
print(intersection_set)  

difference_set = A.difference(B)
print(difference_set) 

# symmetric_difference
symmetric_difference_set = A.symmetric_difference(B)
print(symmetric_difference_set)  
```
#### Output 
```
frozenset({1, 2, 3, 4})
frozenset({1, 2, 3, 4, 5, 6})
frozenset({3, 4})
frozenset({1, 2})
frozenset({1, 2, 5, 6})
```
### Can we convert a frozenset back to a set?
Yes, you can convert a frozenset back to a regular set using the set() constructor.

Example of Converting a frozenset to a Set:
```python []
# frozenset to set
frozen_set = frozenset([1, 2, 3, 4, 5])
my_set = set(frozen_set)  # Convert frozenset back to a set
print(my_set) 
```
#### Output
```
{1, 2, 3, 4, 5}
```
