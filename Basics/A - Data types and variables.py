# ----------------------------
# Data types
# All Data in Python is Object
# ----------------------------

print(type(10))           #int -> intger
print(type(10.5))         #float -> floating point number
print(type("khaled"))     #str -> string
print(type([1,2,3,4,5]))  #list -> array
print(type((1,2,3,4,5)))  #tuple -> tuple
print(type({"one" : 1}))  #dict -> dictionary
print(type(2 == 2))       #bool -> boolean

# --------------------------------------
# -- Variables --
# ---------------
# Syntax => [Variable Name] [Assignment Operator] [Value]
#
# Name Convention and Rules
# [1] Can Start With (a-z A-Z) Or Underscore
# [2] You Cannot start With Num Or Special Characters(!, @, #, $, % )
# [3] Can Include (0-9) Or Underscore
# [4] Cannot Include Special Characters(!, @, #, $, % )
# [5] "Name" is Not Like "name" [ Case Sensitive ]
# --------------------------------------

variable = "value"     #single word -> normal
myVariable = "value"   #two words -> camalCase
my_variable = "value"  #two words -> snake_case

#Python dynamicly typed languege
x = 10
x = "ten"
print(x)  # ten

#reserved words
help("keywords")

'''Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not'''

a, b, c = 1, 2, 3

print(a)    # 1 
print(b)    # 2 
print(c)    # 3  


# ---------------
# -- Notes --
# ---------------
# Source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language
# Compilation : Translate Code Before Run Time
# Run-Time : Period App Take To Executing Commands
# Interpreted : Code Translated On The Fly During Execution



