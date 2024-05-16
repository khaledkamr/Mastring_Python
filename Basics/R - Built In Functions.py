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

'''
Theres At Least One Element Is False
'''

# any()
x = [0, 0, []]

if any(x):
  print("There's At Least One Element is True")

else:
  print("Theres No Any True Elements")

'''
Theres No Any True Elements
'''

# bin()
print(bin(100))   # 0b1100100

# id()
a = 1
b = 2

print(id(a))    # 140719398642472
print(id(b))    # 140719398642504


# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a))        # 70
print(sum(a, 40))    # 110

# round(number, num of digits)
print(round(150.501))     # 151
print(round(150.554, 2))  # 150.55

# range(start, end, step)
print(list(range(0)))           # []
print(list(range(10)))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 20, 2)))    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# print()
print("Hello @ Osama @ How @ Are @ You")                  # Hello @ Osama @ How @ Are @ You
print("Hello", "Osama", "How", "Are", "You", sep=" @ ")   # Hello @ Osama @ How @ Are @ You

print("First Line", end=" ")
print("Second Line")    # First Line Second Line
print("Third Line")     # Third Line


# abs()
print(abs(100))       # 100
print(abs(-100))      # 100
print(abs(10.19))     # 10.19
print(abs(-10.19))    # 10.19

print("=" * 50)

# pow(base, exp, mod) => Power
print(pow(2, 5))      # 32
print(pow(2, 5, 10))  # 2

print("=" * 50)

# min(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))     # -50
print(min("X", "Z", "Osama"))      # Osama
print(min(myNumbers))              # -100
 
print("=" * 50)

# max(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))   # 30
print(max("X", "Z", "Osama"))    # Z
print(max(myNumbers))            # 100

print("=" * 50)

# slice(start, end, step)
a = ["A", "B", "C", "D", "E", "F"]
print(a[:5])             # ['A', 'B', 'C', 'D', 'E']
print(a[slice(5)])       # ['A', 'B', 'C', 'D', 'E']
print(a[slice(2, 5)])    # ['C', 'D', 'E']


# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20)

print(type(mySkillsWithCounter))  # <class 'enumerate'>

for counter, skill in mySkillsWithCounter:
  print(f"{counter} - {skill}")

'''
20 - Html
21 - Css
22 - Js
23 - PHP
'''

print("=" * 50)

# help()
# helps you know how the function works
print(help(print))

'''
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.     
    flush
      whether to forcibly flush the stream.

None
'''

print("=" * 50)

# reversed(iterable)

myString = "KHALED"

print(reversed(myString))    # <reversed object at 0x000001F683365E40>  

for letter in reversed(myString):
  print(letter, end="")

# DELAHK

print('\n')

for s in reversed(mySkills):
  print(s)

'''
PHP
Js
Css
Html
'''