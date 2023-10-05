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

print("\x4F\x73") # Character Hex Value

#You can write the string value between single qoutes or double 
# or even triple if the string includes new lines
string1 = 'what\'s up danger' #escape single qoute
string2 = "what's up danger"
string3 = """what's
 up
danger""" 

print(string1)
print(string2)
print(string3)

#indexing (access single item)
string = "theweeknd"
print(string[1])  #index -> h
print(string[-1]) #index -> first char from the end -> d

#slicing (access multiple sequence items)
#[start:end] end not included
#[start:end:steps]

print(string[3:7])   #week
print(string[:3])    #print from index 0 -> the
print(string[3:])    #print to the end -> weeknd
print(string[0:9:2]) #teekd

#methods

# strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

g = "osama"

print(g.upper())

# lower()

h = "OSama"

print(h.lower())

print(len(string)) #length of the string

# split() rsplit()

a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))

# center()

e = "Osama"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @

# count()

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()

j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))

# index(SubString, Start, End)

a = "I Love Python"
# print(a.index("P"))  # Index Number 7
# print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # Through Error

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)

c = "Osama"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Osama"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())
# replace(Old Value, New Value, Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join(Iterable)

myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))

#string formating (old way)
name = "khaled"
age = 20
gpa = 3.7

#print("my name is " + name + " and my age is " + age) #error
print("my name is %s, my age is %d and my GPA is %.1f" % (name, age, gpa))

# %s -> string
# %d -> number
# %f -> float

#string foramting (new way)
print("my name is {}, my age is {} and my GPA is {}" .format(name, age, gpa))
print("my name is {:s}, my age is {:d} and my GPA is {:f}" .format(name, age, gpa))

#trucate string
longString = "i left the party with a barbie marking x on the dot"
print("once said : {:.17s}" .format(longString))

#format money
myMoney = 2681300137
print("my money in bank is : {:d}".format(myMoney))
print("my money in bank is : {:,d}".format(myMoney))
#print("my money in bank is : {:&d}".format(myMoney)) #error

#rearrange items
a, b, c = "one","two","three"
print("numbers are : {} {} {}".format(a, b, c))
print("numbers are : {1} {2} {0}".format(a, b, c))

x, y, z = 10, 20, 30
print("numbers are : {} {} {}".format(x, y, z))
print("numbers are : {1:d} {2:f} {0:.2f}".format(x, y, z))

#format in version 3.6+
print(f"my name is {name} and my age is {age}")