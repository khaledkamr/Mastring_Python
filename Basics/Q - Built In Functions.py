# ------------------------
# -- Built In Functions --
# ------------------------
# all()    # sum()      # abs()    # slice()
# any()    # round()    # pow()    # enumerate()
# bin()    # range()    # min()    # help()
# id()     # print(     # max()    # reversed()
# ------------------------

# all()
x = [1, 2, 3, 4, []]

if all(x):
  print("All Elements Is True")

else:
  print("Theres At Least One Element Is False")

# any()
x = [0, 0, []]

if any(x):
  print("There's At Least One Element is True")

else:
  print("Theres No Any True Elements")

# bin()
print(bin(100))

# id()
a = 1
b = 2

print(id(a))
print(id(b))


# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a))
print(sum(a, 40))

# round(number, num of digits)
print(round(150.501))
print(round(150.554, 2))

# range(start, end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

# print()
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" @ ")

print("First Line", end=" ")
print("Second Line")
print("Third Line")


# abs()
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#" * 50)

# pow(base, exp, mod) => Power
print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10

print("#" * 50)

# min(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))
print(min("X", "Z", "Osama"))
print(min(myNumbers))

print("#" * 50)

# max(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))
print(max("X", "Z", "Osama"))
print(max(myNumbers))

print("#" * 50)

# slice(start, end, step)
a = ["A", "B", "C", "D", "E", "F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])


# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20)

print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter:
  print(f"{counter} - {skill}")

print("#" * 50)

# help()
# helps you know how the function works
print(help(print))

print("#" * 50)

# reversed(iterable)

myString = "KHALED"

print(reversed(myString))

for letter in reversed(myString):
  print(letter, end="")
  
print('\n')

for s in reversed(mySkills):
  print(s)