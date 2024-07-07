# All about strings and formating

### Esape sequences characters
- \b -> back space
- \ -> escape new line  + "\"
- \\ -> escape back slash
- \" -> escape double quotes
- \n -> new line feed
- \r -> carriage return
- print("123456\rabcd") -> abcd56
- \t -> horizontal tap
- \xhh -> character hex value

### Character Hex Value
```python []
print("\x4F\x73") 
```
### Output
```
Os 
``` 

### You can write the string value between single qoutes or double or even triple if the string includes new lines
```python []
string1 = 'what\'s up danger' #escape single qoute

string2 = "what's up danger" 
#single qoute have been escaped cuz it's between double qoutes

string3 = """what's
 up
danger""" 

print(string1)    
print(string2) 
print(string3)    
```
### Output
```
what's up danger
what's up danger
what's
 up
danger
```
# Concatenation 
```python []
msg = "I Love"
lang = "Python"
print(msg + " " + lang)    

full = msg + " " + lang
print(full)     

# \ -> escape new line
a = "First \
Second \
Third" 

b = "A \
B \
C"

print(a + "\n" + b)

print("Hello " + 1)  
```
### Output
```
I Love Python
I Love Python
First Second Third
A B C
Traceback (most recent call last):
  File "d:\coding\VS code\compile.py", line 19, in <module>
    print("Hello " + 1)  # TypeError: can only concatenate str (not "int") to str
          ~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
PS D:\coding\VS code>
```
# Strings Indexing & Slicing
- All Data in Python is Object
- Object Contain Elements
- Every Element Has Its Own Index
- Python Use Zero Based Indexing ( Index Start From Zero )
- Use Square Brackets To Access Element
- Enable Accessing Parts Of Strings, Tuples or Lists

### indexing (access single item)
```python []
string = "theweeknd"
print(string[1])  # h
print(string[-1]) # d (first char from the end)
```
### slicing (access multiple sequence items)
```python []
#[start:end] end not included
#[start:end:steps]

string = "theweeknd"

print(string[3:7])    
print(string[:3])     # print from index 0
print(string[3:])     # print to the end
print(string[0:9:2])  # two steps
```
### Output
```
week
the
weeknd
teekd
```

# Strings Methods 

### strip() rstrip() lstrip()
```python []
a = "    I Love Python    "
print(a.strip())   
print(a.rstrip())   
print(a.lstrip())   
```
### Output
```
I Love Python
    I Love Python
I Love Python    
```
```python []
a = "#####I Love Python####"
print(a.strip("#"))     
print(a.rstrip("#"))    
print(a.lstrip("#"))   
```
### Output
```
I Love Python
#####I Love Python
I Love Python####
```
```python []
a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))      
print(a.rstrip("@#"))     
print(a.lstrip("@#"))    
```
### Output
```
I Love Python
@#@#@#I Love Python
I Love Python@#@#@#
```
### title()
```python []
b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())
```
### Output
```
I Love 2D Graphics And 3G Technology And Python
```
### capitalize()
```python []
b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())  
```
### Output
```
I love 2d graphics and 3g technology and python
```
### zfill()
```python []
c, d, e, f = "1", "11", "111", "1111"

print(c)    
print(d)    
print(e)    
print(f)    

print(c.zfill(4))   
print(d.zfill(4))   
print(f.zfill(4))   
print(e.zfill(4))   
```
### Output
```
1
11
111
1111
0001
0011
0111
1111
```
### upper()
```python []
g = "khaled"
print(g.upper())  
```
### Output
```
KHALED
```
### lower()
```python []
h = "KHaled"
print(h.lower())   
print(len(string)) # length of the string
```
### Output
```
khaled
9
```
### split() rsplit()
```python []
a = "I Love Python and PHP and MySQL"
print(a.split())    

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))     

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))     

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))   
```
### Output
```
['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']
['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']
['I', 'Love', 'Python', 'and-PHP-and-MySQL']
['I-Love-Python-and', 'PHP', 'and', 'MySQL']
```
### center()
```python []
e = "Khaled"
print(e.center(9))         
print(e.center(9, "#"))    
print(e.center(15, "@"))  
```
### Output
```
  Khaled        
##Khaled##      
@@@@@Khaled@@@@@
```
### count()
```python []
f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))             
print(f.count("PHP", 0, 25))     
```
### Output
```
2
1
```
### swapcase()
```python []
g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())  
print(h.swapcase())
```
### Output
```
i lOVE pYTHON
I Love Python
```
### startswith()
```python []
i = "I Love Python"
print(i.startswith("I"))          
print(i.startswith("S"))          
print(i.startswith("P", 7, 12))   
```
### Output
```
True
False
True
```
### endswith()
```python []
j = "I Love Python"
print(j.endswith("n"))             
print(j.endswith("S"))             
print(j.endswith("e", 2, 6))      
```
### Output
```
True 
False
True 
```
### index(SubString, Start, End)
```python []
a = "I Love Python"
print(a.index("P"))          
print(a.index("P", 0, 10))   
print(a.index("P", 0, 5))    
```
### Output
```
7
7
ValueError: substring not found
```
### find(SubString, Start, End)
```python[]
b = "I Love Python"
print(b.find("P"))           # 7
print(b.find("P", 0, 10))    # 7
print(b.find("P", 0, 5))     # -1
```
### Output

### rjust(Width, Fill Char) ljust(Width, Fill Char)
```python []
c = "Khaled"
print(c.rjust(10))          
print(c.rjust(10, "#"))   

d = "Khaled" 
print(d.ljust(10))        
print(d.ljust(10, "#"))    
```
### Output 
```
    Khaled
####Khaled
Khaled    
Khaled####
```
### splitlines()
```python
e = """First Line
Second Line
Third Line"""

print(e.splitlines())     

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())     
```
### Output
```
['First Line', 'Second Line', 'Third Line']
['First Line', 'Second Line', 'Third Line']
```

### expandtabs()
```python []
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))     # Hello World I Love  Python

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())      # True
print(two.istitle())      # False
```
### Extra methods
```python []
three = " "
four = ""
print(three.isspace())    # True
print(four.isspace())     # False

five = 'i love python'
six = 'I Love Python'
print(five.islower())     # True
print(six.islower())      # False

seven = "Khaled_kamr"
eight = "Khaledkamr99"
nine = "Khaled--kamr99"

print(seven.isidentifier())    # True
print(eight.isidentifier())    # True
print(nine.isidentifier())     # False

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())          # True
print(y.isalpha())          # False

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())          # True
print(z.isalnum())          # True
```
### replace(Old Value, New Value, Count)
```python []
a = "Hello One Two Three One One"
print(a.replace("One", "1"))      
print(a.replace("One", "1", 1))   
print(a.replace("One", "1", 2))  
```
### Output
```
Hello 1 Two Three 1 1
Hello 1 Two Three One One
Hello 1 Two Three 1 One
```
### join(Iterable)
```python []
myList = ["Khaled", "Mohamed", "Elsayed"]
print("-".join(myList))           
print(" ".join(myList))           
print(", ".join(myList))          
print(type(", ".join(myList)))   
```
### Output
```
Khaled-Mohamed-Elsayed
Khaled Mohamed Elsayed
Khaled, Mohamed, Elsayed
<class 'str'>
```
# string formating (version 3.6+)

```python []
name = "khaled"
age = 20
gpa = 3.7

print(f"my name is {name} and my age is {age}")    
```
### Output
```
my name is khaled and my age is 20
```