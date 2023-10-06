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
print(myList) #the whole list
print(myList[0]) #one
print(myList[-1]) #true
print(myList[-3]) #1
print(myList[1:4]) #['Two', 'One', 1]
print(myList[0:-1:2]) #['One', 'One', 100.5]

myList[1] = 2
myList[-1] = False
print(myList)
myList[0:3] = ['A','B','C'] #this call edit not replace
print(myList) 


# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)
print(a)

# remove()

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort() 
print(y)
# To sort the list descending :
y.sort(reverse = True) # reverse is declared to False by default
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")
print(f)

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))