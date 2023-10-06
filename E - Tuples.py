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

print(TupleOne)
print(TupleTwo)

print(type(TupleOne))
print(type(TupleTwo))

# Tuple Indexing

TupleThree = (1, 2, 3, 4, 5)
print(TupleThree[0])
print(TupleThree[-1])
print(TupleThree[-3])

# Tuple Assign Values

TupleFour = (1, 2, 3, 4, 5)
# TupleFour[2] = "Three"
# print(TupleFour)  # 'tuple' object doesn't support item assignment

# Tuple Data

TupleFive = ("Khaled", "Khaled", 1, 2, 3, 100.5, True)
print(TupleFive[1])
print(TupleFive[-1])

# Tuple With One Element

myTuple1 = ("Khaled",)
myTuple2 = "Khaled",

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)

# Tuple, List, String Repeat (*)

myString = "Khaled"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# Methods => count()

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct

a = ("A", "B", 4, "C")

x, y, _, z = a

print(x)
print(y)
print(z)