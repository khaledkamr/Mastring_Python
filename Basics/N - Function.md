# -- Function And Return --
- A Function is A Reusable Block Of Code Do A Task
- A Function Run When You Call It
- A Function Accept Element To Deal With Called [Parameters]
- A Function Can Do The Task Without Returning Data
- A Function Can Return Data After Job is Finished
- A Function Create To Prevent DRY
- A Function Accept Elements When You Call It Called [Arguments]
- [8] There's A Built-In Functions and User Defined Functions
- [9] A Function Is For All Team and All Apps
```python []
def function_name():
  return "Hello Python From Inside Function"

dataFromFunction = function_name()
print(dataFromFunction)   
```
#### Output
```
Hello Python From Inside Function
```
## Function Parameters And Arguments 

- def                     => Function Keyword [Define]
- say_hello()             => Function Name
- name                    => Parameter
- print(f"Hello {name}")  => Task
- say_hello("Ahmed")      => Ahmed is The Argument
```python []
a, b, c = "Khaled", "Ahmed", "Ali"

def say_hello(n):
  print(f"Hello {n}")

say_hello(a)   
say_hello(b)   
say_hello(c)   
```
#### Output
```
Hello Khaled
Hello Ahmed
Hello Ali
```
### EX.1:
```python []
def addition(n1, n2):
  print(n1 + n2)

addition(100, 300) 
addition(-50, 100) 
```
#### Output
```
400
50
```
### EX.2:
```python []
def addition(n1, n2):
  if (type(n1) != int or type(n2) != int):
    print("Only Integers Allowed")
  else:
    print(n1 + n2)

addition(100, 500) 
```
#### Output
```
600
```
### EX.3:
```python []
def full_name(first, middle, last):

  print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("   osama   ", 'mohamed', "elsayed")   
```
#### Output
```
Hello Osama M Elsayed
```
## Function Default Parameters

### you can add a default value in case the user didn't enter value
```python []
# default parameter must be in the end 
def say_hello(name, age = "Unknown", country = "Unknown"): 
  print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

say_hello("Osama", 36, "Egypt") 
say_hello("Mahmoud", 28, "KSA") 
say_hello("Sameh", 38)          
say_hello("Ramy")               
```
#### Output
```
Hello Osama Your Age is 36 and Your Country Is Egypt
Hello Mahmoud Your Age is 28 and Your Country Is KSA
Hello Sameh Your Age is 38 and Your Country Is Unknown
Hello Ramy Your Age is Unknown and Your Country Is Unknown
```
# Function Packing, Unpacking Arguments *Args
### intro:
```python []
myList = [1, 2, 3, 5]

print(myList)   
print(*myList)  
```
#### Output
```
[1, 2, 3, 5]
1 2 3 5
```
### EX.1:
```python []
def say_hello(*peoples):  # n1, n2, n3, n4
  for name in peoples:
    print(f"Hello {name}")

# you can add infinte arguments
say_hello("Osama", "Ahmed", "Sayed", "Mahmoud") 
```
#### Output
```
Hello Osama
Hello Ahmed
Hello Sayed
Hello Mahmoud
```

### EX.2:
```python []
def show_details(name, *skills):
  print(f"Hello {name} Your Skills Is: ")
  for skill in skills:
    print(skill)

show_details("Osama", "Html", "CSS", "JS")
show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")
```
#### Output
```
Hello Osama Your Skills Is:
Html
CSS
JS
Hello Ahmed Your Skills Is:
Html
CSS
JS
Python
PHP
MySQL
```


# Function Packing, Unpacking Arguments **KWArgs 
```python []
def show_skills(*skills):
  print(type(skills)) 
  for skill in skills:
    print(f"{skill}")

show_skills("Html", "CSS", "JS") 
```
#### Output
```
<class 'tuple'>
Html
CSS
JS
```

### If you wanna add dict type arguments, put "**" before the parameter
```python []
mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def show_skills(**skills):
  print(type(skills))
  for skill, value in skills.items():
    print(f"{skill} => {value}")

show_skills(Html = "70%", Css = "80%", JS = "60%") 
show_skills(**mySkills)
```
#### Output
```
<class 'dict'>
Html => 70%
Css => 80%
JS => 60%
<class 'dict'>
Html => 80%
Css => 70%
Js => 50%
Python => 80%
Go => 40%
```

# Function Scope
```python []
x = 1  # Global Scope

def one():
  x = 2 # function scope
  print(f"Print Variable From Function Scope: {x}")

def two():
  x = 4 # function scope
  print(f"Print Variable From Function Scope: {x}")

print(f"Print Variable From Global Scope: {x}") 
one() 
two() 
```
#### Output
```
Print Variable From Global Scope: 1
Print Variable From Function Scope: 2
Print Variable From Function Scope: 4
```
### you can define the variable as global from function scope like this
```python []
def three():
  global x 
  x = 7
  print(f"Print Variable From Global Scope After One Function Is Called {x}")
```
#### Output
```
Print Variable From Global Scope After One Function Is Called 7
```
# Lambda Function 
### Anonymous Function 

- It Has No Name
- You Can Call It Inline Without Defining It
- You Can Use It In Return Data From Another Function
- Lambda Used For Simple Functions and Def Handle The Large Tasks
- Lambda is One Single Expression not Block Of Code
- Lambda Type is Function
```python []
# function
def say_hello(name, age) : return f"Hello {name} your Age Is: {age}" 

# lambda
hello = lambda name, age : f"Hello {name} your Age Is: {age}" 

print(say_hello("Ahmed", 36))  
print(hello("Ahmed", 36))      

# name of the function
print(say_hello.__name__)  
print(hello.__name__)      

print(type(hello))   
```
#### Output
```
Hello Ahmed your Age Is: 36
Hello Ahmed your Age Is: 36
say hallo 
<lamda> 
<class 'function'>
```