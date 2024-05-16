# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Can't Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"Khaled", "Ahmed", 100}
print(mySetOne)      # {'Khaled', 100, 'Ahmed'}
print(mySetOne[0])   # TypeError: 'set' object is not subscriptable

# Slicing Can't Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
print(mySetTwo[0:3]) # TypeError: 'set' object is not subscriptable

# Has Only Immutable Data Types

mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]}   # TypeError: unhashable type: 'list'
mySetThree = {"Khaled", 100, 100.5, True, (1, 2, 3)}   

print(mySetThree)   # {True, 'Khaled', 100, 100.5, (1, 2, 3)}

# Items Is Unique

mySetFour = {1, 2, "Khaled", "One", "Khaled", 1}
print(mySetFour)    # {1, 2, 'Khaled', 'One'}

# clear()

a = {1, 2, 3}
a.clear()
print(a)    # set()

# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)            # {'Three', 'Two', '3', 'One', '1', '2'}
print(b.union(c, x))    # {'Three', 'Two', '3', 'Zero', 'One', '1', '2', 'Cool'}

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)   # {1, 2, 3, 4, 5, 6}

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)    # {1, 2, 3, 4}
print(f)    # {1, 2, 3, 4}

e.add(6)

print(e)     # {1, 2, 3, 4, 6}
print(f)     # {1, 2, 3, 4}

# remove()

g = {1, 2, 3, 4}
g.remove(1)
#g.remove(7)   # KeyError: 7
print(g)      # {2, 3, 4}

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)       # {2, 3, 4}

# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())     # A

# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)      # {1, 2, 3, 'B', 'Css', 'Html', 'A'}
 
# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "Khaled", "Ahmed"}
print(a)                 # {1, 2, 3, 4}
print(a.difference(b))   # {4}
print(a)                 # {1, 2, 3, 4}

print("=" * 40)  # Separator

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Khaled", "Ahmed"}
print(c)                 # {1, 2, 3, 4}
c.difference_update(d)   
print(c)                 # {3, 4}

print("=" * 40)  # Separator

# intersection()

e = {1, 2, 3, 4, "X", "Khaled"}
f = {"Khaled", "X", 2}
print(e)                    # {1, 2, 3, 4, 'X', 'Khaled'}
print(e.intersection(f))    # {2, 'X', 'Khaled'}
print(e)                    # {1, 2, 3, 4, 'X', 'Khaled'}

print("=" * 40)  # Separator

# intersection_update()

g = {1, 2, 3, 4, "X", "Khaled"}
h = {"Khaled", "X", 2}
print(g)                    # {1, 2, 3, 4, 'X', 'Khaled'}
g.intersection_update(h)    
print(g)                    # {2, 'X', 'Khaled'}

print("=" * 40)  # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"Khaled", "Zero", 1, 2, 4, "X"}
print(i)                          # {1, 2, 3, 4, 5, 'X'}
print(i.symmetric_difference(j))  # {3, 5, 'Zero', 'Khaled'}
print(i)                          # {1, 2, 3, 4, 5, 'X'}

print("=" * 40)  # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"Khaled", "Zero", 1, 2, 4, "X"}
print(k)                          # {1, 2, 3, 4, 5, 'X'}
k.symmetric_difference_update(l)  
print(k)                          # {3, 5, 'Zero', 'Khaled'}
 
# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("=" * 50)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True