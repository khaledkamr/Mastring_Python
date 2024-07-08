# Set 
- Set Items Are Enclosed in Curly Braces
- Set Items Are Not Ordered And Not Indexed
- Set Indexing and Slicing Can't Be Done
- Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
- Set Items Is Unique

## Not Ordered And Not Indexed
```python []
mySetOne = {"Khaled", "Ahmed", 100}
print(mySetOne)   
print(mySetOne[0])
```
#### Output
```
{'Khaled', 100, 'Ahmed'}
TypeError: 'set' object is not subscriptable
```
## Slicing Can't Be Done
```python []
mySetTwo = {1, 2, 3, 4, 5, 6}
print(mySetTwo[0:3]) 
```
#### Output
```
TypeError: 'set' object is not subscriptable
```
## Has Only Immutable Data Types
```python []
mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} 
```
#### Output
```
TypeError: unhashable type: 'list'
```
```python []
mySetThree = {"Khaled", 100, 100.5, True, (1, 2, 3)}   
print(mySetThree)   
```
#### Output
```
{True, 'Khaled', 100, 100.5, (1, 2, 3)}
```
## Items Is Unique
```python []
mySetFour = {1, 2, "Khaled", "One", "Khaled", 1}
print(mySetFour)   
```
#### Output
```
 {1, 2, 'Khaled', 'One'}
```
## clear()
```python []
a = {1, 2, 3}
a.clear()
print(a)    
```
#### Output
```
set()
```
## union()
```python
b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)            # 
print(b.union(c, x))    #
```
#### Output
```
{'Three', 'Two', '3', 'One', '1', '2'}
{'Three', 'Two', '3', 'Zero', 'One', '1', '2', 'Cool'}
```
## add()
```python []
d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)   
```
#### Output
```
{1, 2, 3, 4, 5, 6}
```
## copy()
```python []
e = {1, 2, 3, 4}
f = e.copy()

print(e)  
print(f)  

e.add(6)

print(e)    
print(f)    
```
#### Output
```
{1, 2, 3, 4}
{1, 2, 3, 4}
{1, 2, 3, 4, 6}
{1, 2, 3, 4}
```
## remove()
```python []
g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)   # KeyError: 7
print(g)      
```
#### output
```
{2, 3, 4}
```
## discard()
```python []
h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)       
```
#### output
```
{2, 3, 4}
```
## pop()
```python []
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())     
```
#### output
```
 A
```
## update()
```python []
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)      
 ```
#### output
```
{1, 2, 3, 'B', 'Css', 'Html', 'A'}
```

## difference()
```python []
a = {1, 2, 3, 4}
b = {1, 2, 3, "Khaled", "Ahmed"}
print(a)                 
print(a.difference(b))   
print(a)                 

```
#### output
```
{1, 2, 3, 4}
{4}
{1, 2, 3, 4}
```

## difference_update()
```python []
c = {1, 2, 3, 4}
d = {1, 2, "Khaled", "Ahmed"}
print(c)                 
c.difference_update(d)   
print(c)               
```
#### output
```
{1, 2, 3, 4}
{3, 4}
```
## intersection()
```python []
e = {1, 2, 3, 4, "X", "Khaled"}
f = {"Khaled", "X", 2}
print(e)                   
print(e.intersection(f))   
print(e)                   
```
#### output
```
{1, 2, 3, 4, 'X', 'Khaled'}
{2, 'X', 'Khaled'}
{1, 2, 3, 4, 'X', 'Khaled'}
```
## intersection_update()
```python []
g = {1, 2, 3, 4, "X", "Khaled"}
h = {"Khaled", "X", 2}
print(g)                    # {1, 2, 3, 4, 'X', 'Khaled'}
g.intersection_update(h)    
print(g)                    # {2, 'X', 'Khaled'}
```
#### output
```
{1, 2, 3, 4, 'X', 'Khaled'}
{2, 'X', 'Khaled'}
```
## symmetric_difference()
```python []
i = {1, 2, 3, 4, 5, "X"}
j = {"Khaled", "Zero", 1, 2, 4, "X"}
print(i)                          
print(i.symmetric_difference(j))  
print(i)                          
```
#### output
```
{1, 2, 3, 4, 5, 'X'}
{3, 5, 'Zero', 'Khaled'}
{1, 2, 3, 4, 5, 'X'}
```
## symmetric_difference_update()
```python []
k = {1, 2, 3, 4, 5, "X"}
l = {"Khaled", "Zero", 1, 2, 4, "X"}
print(k)                          
k.symmetric_difference_update(l)  
print(k)                         
 ```
#### output
```
{1, 2, 3, 4, 5, 'X'}
{3, 5, 'Zero', 'Khaled'}
```
## issuperset()
```python []
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b)) 
print(a.issuperset(c)) 
```
#### output
```
True
False
```
## issubset()
```python []
d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e)) 
print(d.issubset(f)) 
```
#### output
```
False
True
```
## isdisjoint()
```python []
g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h)) 
print(g.isdisjoint(i)) 
```
#### output
```
False
True
```