# Type Conversion 

## str()
```python []
a = 10
print(type(a))       
print(type(str(a)))  
```
#### Output
```
<class 'int'>
<class 'str'>
```

## tuple()
```python []
c = "Osama"  # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(tuple(c)) 
print(tuple(d)) 
print(tuple(e)) 
print(tuple(f)) 
```
#### Output
```
('O', 's', 'a', 'm', 'a')
(1, 2, 3, 4, 5)
('C', 'B', 'A')
('A', 'B')
```
## list()
```python []
c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(list(c))  
print(list(d))  
print(list(e))  
print(list(f))  
```
#### Output
```
['O', 's', 'a', 'm', 'a']
[1, 2, 3, 4, 5]
['C', 'B', 'A']
['A', 'B']
```
## set()
```python []
c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List
f = {"A": 1, "B": 2}  # Dictionary

print(set(c))   
print(set(d))   
print(set(e))   
print(set(f))   
```
#### Output
```
{'a', 'm', 's', 'O'}
{1, 2, 3, 4, 5}
{'C', 'B', 'A'}
{'B', 'A'}
```
## dict()
### string and set cannot be convert to dict
```python []
d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List

print(dict(d)) 
print(dict(e)) 
```
#### Output
```
{'A': 1, 'B': 2, 'C': 3}
{'One': 1, 'Two': 2, 'Three': 3}
```