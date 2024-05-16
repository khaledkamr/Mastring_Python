# -------------------------
# -- Function And Return --
# -------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# ----------------------------------------

def function_name():

  return "Hello Python From Inside Function"

dataFromFunction = function_name()

print(dataFromFunction)  # Hello Python From Inside Function

# Function Parameters And Arguments 

a, b, c = "Khaled", "Ahmed", "Ali"

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Ahmed is The Argument

def say_hello(n):

  print(f"Hello {n}")

say_hello(a)    # Hello Khaled
say_hello(b)    # Hello Ahmed
say_hello(c)    # Hello Ali

#EX.1:

def addition(n1, n2):

  print(n1 + n2)

addition(100, 300)   # 400
addition(-50, 100)   # 50

#EX.2:

def addition(n1, n2):

  if (type(n1) != int or type(n2) != int):

    print("Only Integers Allowed")

  else:

    print(n1 + n2)

addition(100, 500) # 600

#EX.3:

def full_name(first, middle, last):

  print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("   osama   ", 'mohamed', "elsayed")   # Hello Osama M Elsayed


# Function Default Parameters

# you can add a default value in case the user didn't enter value

def say_hello(name, age = "Unknown", country = "Unknown"): # default parameter must be in the end 

  print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

say_hello("Osama", 36, "Egypt")  # Hello Osama Your Age is 36 and Your Country Is Egypt
say_hello("Mahmoud", 28, "KSA")  # Hello Mahmoud Your Age is 28 and Your Country Is KSA
say_hello("Sameh", 38)           # Hello Sameh Your Age is 38 and Your Country Is Unknown
say_hello("Ramy")                # Hello Ramy Your Age is Unknown and Your Country Is Unknown


# ----------------------------------------------------
# Function Packing, Unpacking Arguments *Args
# ----------------------------------------------------
#intro:

myList = [1, 2, 3, 5]

print(myList)    # [1, 2, 3, 5]
print(*myList)   # 1 2 3 5

#EX.1:

def say_hello(*peoples):  # n1, n2, n3, n4

  for name in peoples:

    print(f"Hello {name}")

say_hello("Osama", "Ahmed", "Sayed", "Mahmoud") # you can add infinte arguments
'''
Hello Osama
Hello Ahmed
Hello Sayed
Hello Mahmoud
'''

#EX.2:

def show_details(name, *skills):

  print(f"Hello {name} Your Skills Is: ")

  for skill in skills:

    print(skill)

show_details("Osama", "Html", "CSS", "JS")
show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")
'''
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
'''


# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

def show_skills(*skills):

  print(type(skills)) # tuple

  for skill in skills:

    print(f"{skill}")

show_skills("Html", "CSS", "JS") 
'''
<class 'tuple'>
Html
CSS
JS
'''

# If you wanna add dict type arguments, put "**" before the parameter

mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def show_skills(**skills):

  print(type(skills)) # dict

  for skill, value in skills.items():

    print(f"{skill} => {value}")

show_skills(Html = "70%", Css = "80%", JS = "60%") 
show_skills(**mySkills)



# Function Scope

x = 1  # Global Scope

def one():

  x = 2 # function scope

  print(f"Print Variable From Function Scope {x}")

def two():

  x = 4 # function scope

  print(f"Print Variable From Function Scope {x}")

print(f"Print Variable From Global Scope {x}") #  Print Variable From Global Scope 1
one() #  Print Variable From Function Scope 2
two() #  Print Variable From Function Scope 4

# you can define the variable as global from function scope like this

def three():

  global x 
  x = 7

  print(f"Print Variable From Global Scope After One Function Is Called {x}")


# Lambda Function 
# Anonymous Function 

# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

def say_hello(name, age) : return f"Hello {name} your Age Is: {age}" # function

hello = lambda name, age : f"Hello {name} your Age Is: {age}" # lambda

print(say_hello("Ahmed", 36))   # Hello Ahmed your Age Is: 36
print(hello("Ahmed", 36))       # Hello Ahmed your Age Is: 36

# name of the function
print(say_hello.__name__)  # say hallo 
print(hello.__name__)      # <lamda> 

# there is no difference between lambda and function in the type 
print(type(hello))    # <class 'function'>