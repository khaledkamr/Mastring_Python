# Lists 
- List is like array in C++ but it's not array
- List Items Are Enclosed in Square Brackets
- List Are Ordered, To Use Index To Access Item
- List Are Mutable => Add, Delete, Edit
- List Items Is Not Unique
- List Can Have Different Data Types
```python []
myList = ["One", "Two", "One", 1, 100.5, True]
print(myList)          
print(myList[0])       
print(myList[-1])      
print(myList[-3])      
print(myList[1:4])     
print(myList[0:-1:2])  

myList[1] = 2
myList[-1] = False
print(myList)          
myList[0:3] = ['A','B','C']
print(myList)          
```
### Output
```
['One', 'Two', 'One', 1, 100.5, True]
One
True
1
['Two', 'One', 1]
['One', 'One', 100.5]
['One', 2, 'One', 1, 100.5, False]
['A', 'B', 'C', 1, 100.5, False]
```

# Lists Methods 

### append()
```python []
myFriends = ["Khaled", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")       
myFriends.append(100)         
myFriends.append(150.200)     
myFriends.append(True)        
myFriends.append(myOldFriends)

print(myFriends)         
print(myFriends[2])      
print(myFriends[6])     
print(myFriends[7])      
print(myFriends[7][2])   
```
#### Output
```
['Khaled', 'Ahmed', 'Sayed', 'Alaa', 100, 150.2, True, ['Haytham', 'Samah', 'Ali']]
Sayed
True
['Haytham', 'Samah', 'Ali']
Ali
```
### extend()
```python []
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)
print(a)     
```
#### Output
```
[1, 2, 3, 4, 'A', 'B', 'C', 'One', 'Two']
```
### remove()
```python []
x = [1, 2, 3, 4, 5, "Khaled", True, "Khaled", "Khaled"]
x.remove("Khaled")
print(x)     
```
#### Output
```
[1, 2, 3, 4, 5, True, 'Khaled', 'Khaled']
```
### sort()
```python []
y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort() 
print(y)   

# To sort the list descending :
# reverse is declared to False by default
y.sort(reverse = True) 
print(y)   
```
#### Output
```
[-10, 1, 2, 17, 29, 100, 120]
[120, 100, 29, 17, 2, 1, -10]
```
### reverse()
```python []
z = [10, 1, 9, 80, 100, "Khaled", 100]
z.reverse()
print(z)      
```
#### Output
```
[100, 'Khaled', 100, 80, 9, 1, 10]
```
### clear()
```python []
a = [1, 2, 3, 4]
a.clear()
print(a)     
```
#### Output
```
[]
```
### copy()
```python []
b = [1, 2, 3, 4]
c = b.copy()
print(b)  
print(c)  

b.append(5)
print(b)  
print(c)  
```
#### Output
```
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4]
```
### count()
```python []
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))       
```
#### Output
```
3
```
### index()
```python []
e = ["Khaled", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))        
```
#### Output
```
3
```
### insert()
```python []
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")
print(f)        
```
#### Output
```
['Test', 1, 2, 3, 4, 5, 'A', 'Test', 'B']
```
### pop()
```python []
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))        
```
#### Output
```
5
```