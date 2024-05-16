# -----------------------------
# -- Lists --
# -----------
# [1] List is like array in C++ but it's not array
# [2] List Items Are Enclosed in Square Brackets
# [3] List Are Ordered, To Use Index To Access Item
# [4] List Are Mutable => Add, Delete, Edit
# [5] List Items Is Not Unique
# [6] List Can Have Different Data Types

myList = ["One", "Two", "One", 1, 100.5, True]
print(myList)          # ['One', 'Two', 'One', 1, 100.5, True]
print(myList[0])       # One
print(myList[-1])      # True
print(myList[-3])      # 1
print(myList[1:4])     # ['Two', 'One', 1]
print(myList[0:-1:2])  # ['One', 'One', 100.5]

myList[1] = 2
myList[-1] = False
print(myList)          #  ['One', 2, 'One', 1, 100.5, False]
myList[0:3] = ['A','B','C'] #this call edit not replace
print(myList)          # ['A', 'B', 'C', 1, 100.5, False]


# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Khaled", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")       
myFriends.append(100)         
myFriends.append(150.200)     
myFriends.append(True)        
myFriends.append(myOldFriends)

print(myFriends)         # ['Khaled', 'Ahmed', 'Sayed', 'Alaa', 100, 150.2, True, ['Haytham', 'Samah', 'Ali']] 
print(myFriends[2])      # Sayed
print(myFriends[6])      # True
print(myFriends[7])      # ['Haytham', 'Samah', 'Ali']
print(myFriends[7][2])   # Ali

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)
print(a)     # [1, 2, 3, 4, 'A', 'B', 'C', 'One', 'Two']

# remove()

x = [1, 2, 3, 4, 5, "Khaled", True, "Khaled", "Khaled"]
x.remove("Khaled")
print(x)     # [1, 2, 3, 4, 5, True, 'Khaled', 'Khaled']

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort() 
print(y)    # [-10, 1, 2, 17, 29, 100, 120]
# To sort the list descending :
y.sort(reverse = True) # reverse is declared to False by default
print(y)    # [120, 100, 29, 17, 2, 1, -10]

# reverse()

z = [10, 1, 9, 80, 100, "Khaled", 100]
z.reverse()
print(z)      # [100, 'Khaled', 100, 80, 9, 1, 10]

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)     # []

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # [1, 2, 3, 4]
print(c)  # [1, 2, 3, 4]

b.append(5)

print(b)  # [1, 2, 3, 4, 5]
print(c)  # [1, 2, 3, 4]

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))       # 3

# index()

e = ["Khaled", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))        # 3

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")
print(f)        # ['Test', 1, 2, 3, 4, 5, 'A', 'Test', 'B']

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))        # 5