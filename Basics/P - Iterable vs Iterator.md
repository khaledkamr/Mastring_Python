# Iterable vs Iterator
## Iterable
- Object Contains Data That Can Be Iterated Upon
- Examples (String, List, Set, Tuple, Dictionary)
## Iterator
- Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
- You Can Generate Iterator From Iterable When Using iter() Method
- For Loop Already Calls iter() Method on The Iterable Behind The Scene
- Gives "StopIteration" If Theres No Next Element

```python []
String = "KHALED"
List = [1, 2, 3, 4, 5]

for l in String:
  print(l, end=" ")

for n in List:
  print(n, end=" ")
```
#### Output
```
K H A L E D 1 2 3 4 5
```

### For Loop Already Calls iter() Method
### the variables 'n' and 'l' are iterators
```python []
Iterator = iter(String)

print(next(Iterator))  
print(next(Iterator))  
print(next(Iterator))  
print(next(Iterator))  
print(next(Iterator))  
print(next(Iterator))  

for L in iter("KHALED"):
  print(L, end=" ")
```
#### Output
```
K H A L E D
```