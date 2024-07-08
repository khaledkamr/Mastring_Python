# Tuple
- Tuple Items Are Enclosed in Parentheses
- You Can Remove The Parentheses If You Want
- Tuple Are Ordered, To Use Index To Access Item
- Tuple Are Immutable => You Can't Add or Delete
- Tuple Items Is Not Unique
- Tuple Can Have Different Data Types
- Operators Used in Strings and Lists Available In Tuples

## Tuple Syntax & Type Test

```python []
TupleOne = ("Khaled", "Ahmed")
TupleTwo = "Khaled", "Ahmed"

print(TupleOne)        
print(TupleTwo)        

print(type(TupleOne))    
print(type(TupleTwo))    
```
#### Output
```
('Khaled', 'Ahmed')
('Khaled', 'Ahmed')
<class 'tuple'>
<class 'tuple'>
```
## Tuple Indexing

```python []
TupleThree = (1, 2, 3, 4, 5)
print(TupleThree[0])      
print(TupleThree[-1])     
print(TupleThree[-3])     
```
#### Output
```
1
5
3
```

## Tuple Assign Values

```python []
TupleFour = (1, 2, 3, 4, 5)
TupleFour[2] = "Three"   
```
#### Output
```
TypeError: 'tuple' object does not support item assignment
```

## Tuple Data
```python []
TupleFive = ("Khaled", "Khaled", 1, 2, 3, 100.5, True)
print(TupleFive[1])     
print(TupleFive[-1])    
```
#### Output
```
Khaled
True
```
## Tuple With One Element
```python []
myTuple1 = ("Khaled",)
myTuple2 = "Khaled",

print(myTuple1)    
print(myTuple2)    

print(type(myTuple1))    
print(type(myTuple2))    

print(len(myTuple1))    
print(len(myTuple2))    
```
#### Output
```
('Khaled',)
('Khaled',)
<class 'tuple'>
<class 'tuple'>
1
1
```
## Tuple Concatenation
```python []
a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)   
print(d)   
```
#### Output
```
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 'A', 'B', True, 5, 6)
```
## Tuple, List, String Repeat (*)
```python []
myString = "Khaled"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)   
print(myList * 6)     
print(myTuple * 6)    
```
#### Output
```
KhaledKhaledKhaledKhaledKhaledKhaled
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B')
```
## Methods => count()
```python []
a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))      
```
#### Output
```
2
```
## Methods => index()
```python []
b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error 
print(f"The Position of Index Is: {b.index(7)}")             
```
#### Output
```
The Position of Index Is: 2
```
## Tuple Destruct
```python []
a = ("A", "B", 4, "C")

x, y, _, z = a

print(x)   
print(y)   
print(z)   
```
#### Output
```
 A
 B
 C
```