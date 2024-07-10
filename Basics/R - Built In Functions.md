# Built In Functions 
### all()     sum()       abs()     slice()
### any()     round()     pow()     enumerate()
### bin()     range()     min()     help()
### id()      print()     max()     reversed()

# all()
```python []
x = [1, 2, 3, 4, []]

if all(x):
  print("All Elements Is True")

else:
  print("Theres At Least One Element Is False")
```
#### Output
```
Theres At Least One Element Is False
```

# any()
```python []
x = [0, 0, []]

if any(x):
  print("There's At Least One Element is True")

else:
  print("Theres No Any True Elements")
```
#### Output
```
Theres No Any True Elements
```

# bin()
```python []
print(bin(100))  
```
#### Output
```
0b1100100
```

# id()
```python []
a = 1
b = 2

print(id(a))   
print(id(b))   
```
#### Output
```
140719398642472
140719398642504
```
# sum(iterable, start)
```python []
a = [1, 10, 19, 40]
print(sum(a))       
print(sum(a, 40))   
```
#### Output
```
70
110
```
# round(number, num of digits)
```python []
print(round(150.501))    
print(round(150.554, 2)) 
```
#### Output
```
151
150.55
```
# range(start, end, step)
```python []
print(list(range(0)))          
print(list(range(10)))         
print(list(range(0, 20, 2)))   
```
#### Output
```
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```
# print()
```python []
print("Hello @ Osama @ How @ Are @ You")                 
print("Hello", "Osama", "How", "Are", "You", sep=" @ ")   

print("First Line", end=" ") # to scape new line
print("Second Line")   
print("Third Line")     
```
#### Output
```
Hello @ Osama @ How @ Are @ You
Hello @ Osama @ How @ Are @ You
First Line Second Line
Third Line
```
# abs()
```python []
print(abs(100))      
print(abs(-100))     
print(abs(10.19))    
print(abs(-10.19))   
```
#### Output
```
100
100
10.19
10.19
```

# pow(base, exp, mod) => Power
```python []
print(pow(2, 5))      
print(pow(2, 5, 10))  
```
#### Output
```
32
2
```

# min(item, item , item, or iterator)
```python []
myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))     
print(min("X", "Z", "Khaled"))      
print(min(myNumbers))              
 ```
#### Output
```
-50
Khaled
-100
```

# max(item, item , item, or iterator)
```python []
myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))   
print(max("X", "Z", "Osama"))    
print(max(myNumbers))            
```
#### Output
```
30
Z
100
```

# slice(start, end, step)
```python []
a = ["A", "B", "C", "D", "E", "F"]
print(a[:5])            
print(a[slice(5)])      
print(a[slice(2, 5)])   
```
#### Output
```
['A', 'B', 'C', 'D', 'E']
['A', 'B', 'C', 'D', 'E']
['C', 'D', 'E']
```
# enumerate(iterable, start=0)
```python []
mySkills = ["Html", "Css", "Js", "PHP"]
mySkillsWithCounter = enumerate(mySkills, 20)
print(type(mySkillsWithCounter)) 

for counter, skill in mySkillsWithCounter:
  print(f"{counter} - {skill}")
```
#### Output
```
<class 'enumerate'>
20 - Html
21 - Css
22 - Js
23 - PHP
```

# help()
### helps you know how the function works
```python []
print(help(print))
```
#### Output
```
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.     
    flush
      whether to forcibly flush the stream.

None
```

# reversed(iterable)
```python []
myString = "KHALED"
print(reversed(myString))   

for letter in reversed(myString):
  print(letter, end="")
```
#### Output
```
<reversed object at 0x000001F683365E40>  
DELAHK
```
### You can use it on any datatype except numbers
### Ex
```python []
for s in reversed(mySkills):
  print(s)
```
#### Output
```
PHP
Js
Css
Html
```