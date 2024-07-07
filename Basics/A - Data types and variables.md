# Data types
### All Data in Python is Object
```python []
print(type(10))           #int -> intger
print(type(10.5))         #float -> floating point number
print(type("khaled"))     #str -> string
print(type([1,2,3,4,5]))  #list -> array
print(type((1,2,3,4,5)))  #tuple -> tuple
print(type({"one" : 1}))  #dict -> dictionary
print(type(2 == 2))       #bool -> boolean
```
# Variables 
```
Syntax => [Variable Name] [Assignment Operator] [Value]
```

### Name Convention and Rules
- Can Start With (a-z A-Z) Or Underscore
- You Cannot start With Num Or Special Characters(!, @, #, $, % )
- Can Include (0-9) Or Underscore
- Cannot Include Special Characters(!, @, #, $, % )
- "Name" is Not Like "name" [ Case Sensitive ]
```python []
variable = "value"     #single word -> normal
myVariable = "value"   #two words -> camalCase
my_variable = "value"  #two words -> snake_case
```

### Python dynamically typed language
```python []
x = 10
x = "ten"
print(x) 
```
### output
```
ten
```
# reserved words
```python []
help("keywords")
```
### Output
```
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
```
```python []
a, b, c = 1, 2, 3

print(a) 
print(b) 
print(c) 
``` 
### Output
```
1
2
3
```



