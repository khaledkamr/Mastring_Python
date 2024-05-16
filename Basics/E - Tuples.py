# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Can't Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple Syntax & Type Test

TupleOne = ("Khaled", "Ahmed")
TupleTwo = "Khaled", "Ahmed"

print(TupleOne)         # ('Khaled', 'Ahmed')
print(TupleTwo)         # ('Khaled', 'Ahmed')

print(type(TupleOne))    # <class 'tuple'>
print(type(TupleTwo))    # <class 'tuple'>

# Tuple Indexing

TupleThree = (1, 2, 3, 4, 5)
print(TupleThree[0])       # 1
print(TupleThree[-1])      # 5
print(TupleThree[-3])      # 3

# Tuple Assign Values

TupleFour = (1, 2, 3, 4, 5)
TupleFour[2] = "Three"    # TypeError: 'tuple' object does not support item assignment

# Tuple Data

TupleFive = ("Khaled", "Khaled", 1, 2, 3, 100.5, True)
print(TupleFive[1])     # Khaled
print(TupleFive[-1])    # True

# Tuple With One Element

myTuple1 = ("Khaled",)
myTuple2 = "Khaled",

print(myTuple1)     # ('Khaled',)
print(myTuple2)     # ('Khaled',)

print(type(myTuple1))    # <class 'tuple'>
print(type(myTuple2))    # <class 'tuple'>

print(len(myTuple1))    # 1
print(len(myTuple2))    # 1

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)     # (1, 2, 3, 4, 5, 6)
print(d)     # (1, 2, 3, 4, 'A', 'B', True, 5, 6)

# Tuple, List, String Repeat (*)

myString = "Khaled"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)    # KhaledKhaledKhaledKhaledKhaledKhaled
print(myList * 6)      # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(myTuple * 6)     # ('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B')

# Methods => count()

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))      # 2

# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
print("The Position of Index Is: {:d}".format(b.index(7)))    # The Position of Index Is: 2
print(f"The Position of Index Is: {b.index(7)}")              # The Position of Index Is: 2

# Tuple Destruct

a = ("A", "B", 4, "C")

x, y, _, z = a

print(x)    # A
print(y)    # B
print(z)    # C