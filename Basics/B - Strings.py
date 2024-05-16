#----------------------------------
#All about strings and formating
#----------------------------------
#Esape sequences characters
#\b -> back space
#\ -> escape new line  + "\"
#\\ -> escape back slash
#\" -> escape double quotes
#\n -> new line feed
#\r -> carriage return
#print("123456\rabcd") -> abcd56
#\t -> horizontal tap
#\xhh -> character hex value

# Character Hex Value
print("\x4F\x73")  # Os  

#You can write the string value between single qoutes or double 
# or even triple if the string includes new lines
string1 = 'what\'s up danger' #escape single qoute
string2 = "what's up danger" #single qoute have been escaped cuz it's between double qoutes
string3 = """what's
 up
danger""" 

print(string1)    # what's up danger
print(string2)    # what's up danger
print(string3)    # what's
                  #  up
                  # danger

# -------------------
# -- Concatenation --
# -------------------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)    # I Love Python

full = msg + " " + lang
print(full)     # I Love Python

a = "First \
Second \
Third" # \ -> escape new line

b = "A \
B \
C"

print(a + "\n" + b)  # First Second Third
                     # A B C

# print("Hello " + 1)  # TypeError: can only concatenate str (not "int") to str

# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

#indexing (access single item)
string = "theweeknd"
print(string[1])  # h
print(string[-1]) # d (first char from the end)

#slicing (access multiple sequence items)
#[start:end] end not included
#[start:end:steps]

print(string[3:7])   # week
print(string[:3])    # the  (print from index 0)
print(string[3:])    # weeknd  (print to the end)
print(string[0:9:2]) # teekd   (two steps)


# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())    # I Love Python
print(a.rstrip())   #     I Love Python
print(a.lstrip())   # I Love Python

a = "#####I Love Python####"
print(a.strip("#"))    # I Love Python
print(a.rstrip("#"))   # #####I Love Python
print(a.lstrip("#"))   # I Love Python####

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))     # I Love Python
print(a.rstrip("@#"))    # @#@#@#I Love Python
print(a.lstrip("@#"))    # I Love Python@#@#@#

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())    # I Love 2D Graphics And 3G Technology And Python

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())   # I love 2d graphics and 3g technology and python

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)    # 1
print(d)    # 11
print(e)    # 111
print(f)    # 1111

print(c.zfill(4))   # 0001
print(d.zfill(4))   # 0011
print(e.zfill(4))   # 0111
print(f.zfill(4))   # 1111

# upper()

g = "khaled"

print(g.upper())  # KHALED

# lower()

h = "KHaled"

print(h.lower())   # khaled

print(len(string)) # 9 (length of the string)

# split() rsplit()

a = "I Love Python and PHP and MySQL"
print(a.split())    # ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))    # ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))    # ['I', 'Love', 'Python', 'and-PHP-and-MySQL']

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))    # ['I-Love-Python-and', 'PHP', 'and', 'MySQL']

# center()

e = "Khaled"
print(e.center(9))        #   Khaled
print(e.center(9, "#"))   # ##Khaled##
print(e.center(15, "@"))  # @@@@@Khaled@@@@@

# count()

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))             # 2 
print(f.count("PHP", 0, 25))      # 1

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())   # i lOVE pYTHON
print(h.swapcase())   # I Love Python

# startswith()

i = "I Love Python"
print(i.startswith("I"))          # True
print(i.startswith("S"))          # False
print(i.startswith("P", 7, 12))   # True

# endswith()

j = "I Love Python"
print(j.endswith("n"))            # True
print(j.endswith("S"))            # False
print(j.endswith("e", 2, 6))      # True

# index(SubString, Start, End)

a = "I Love Python"
print(a.index("P"))          # 7
print(a.index("P", 0, 10))   # 7
print(a.index("P", 0, 5))    # ValueError: substring not found

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))           # 7
print(b.find("P", 0, 10))    # 7
print(b.find("P", 0, 5))     # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)

c = "Khaled"
print(c.rjust(10))        #      Khaled
print(c.rjust(10, "#"))   #  ####Khaled

d = "Khaled" 
print(d.ljust(10))        # Khaled
print(d.ljust(10, "#"))   # Khaled####

# splitlines()

e = """First Line
Second Line
Third Line"""

print(e.splitlines())     # ['First Line', 'Second Line', 'Third Line']

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())     # ['First Line', 'Second Line', 'Third Line']

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))     # Hello World I Love  Python

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())      # True
print(two.istitle())      # False

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

# replace(Old Value, New Value, Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1"))      # Hello 1 Two Three 1 1
print(a.replace("One", "1", 1))   # Hello 1 Two Three One One
print(a.replace("One", "1", 2))   # Hello 1 Two Three 1 One

# join(Iterable)

myList = ["Khaled", "Mohamed", "Elsayed"]
print("-".join(myList))          # Khaled-Mohamed-Elsayed
print(" ".join(myList))          # Khaled Mohamed Elsayed
print(", ".join(myList))         # Khaled, Mohamed, Elsayed
print(type(", ".join(myList)))   # <class 'str'>

#---------------------------------------
#string formating (old way)
#---------------------------------------

name = "khaled"
age = 20
gpa = 3.7

#print("my name is " + name + " and my age is " + age) #error
print("my name is %s, my age is %d and my GPA is %.1f" % (name, age, gpa))   # my name is khaled, my age is 20 and my GPA is 3.7

# %s -> string
# %d -> number
# %f -> float

#---------------------------------------
#string foramting (new way)
#---------------------------------------

print("my name is {}, my age is {} and my GPA is {}" .format(name, age, gpa))        # my name is khaled, my age is 20 and my GPA is 3.7
print("my name is {:s}, my age is {:d} and my GPA is {:f}" .format(name, age, gpa))  # my name is khaled, my age is 20 and my GPA is 3.700000

#trucate string
longString = "i left the party with a barbie marking x on the dot"
print("once said : {:.17s}" .format(longString))    # once said : i left the party

#format money
myMoney = 2681300137
print("my money in bank is : {:d}".format(myMoney))     # my money in bank is : 2681300137
print("my money in bank is : {:,d}".format(myMoney))    # my money in bank is : 2,681,300,137
print("my money in bank is : {:&d}".format(myMoney))    # ValueError: Invalid format specifier '&d' for object of type 'int'

#rearrange items
a, b, c = "one","two","three"
print("numbers are : {} {} {}".format(a, b, c))      # numbers are : one two three
print("numbers are : {1} {2} {0}".format(a, b, c))   # numbers are : two three one

x, y, z = 10, 20, 30
print("numbers are : {} {} {}".format(x, y, z))              # numbers are : 10 20 30
print("numbers are : {1:d} {2:f} {0:.2f}".format(x, y, z))   # numbers are : 20 30.000000 10.00

#---------------------------------------
#format in version 3.6+
#---------------------------------------

print(f"my name is {name} and my age is {age}")     # my name is khaled and my age is 20