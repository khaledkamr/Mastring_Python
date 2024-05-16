# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

String = "KHALED"
List = [1, 2, 3, 4, 5]

for l in String:
  print(l, end=" ")

for n in List:
  print(n, end=" ")

'''
K H A L E D 1 2 3 4 5
'''

# For Loop Already Calls iter() Method
# the variables 'n' and 'l' are iterators
#------------------------------------------

Iterator = iter(String)

print(next(Iterator))   # K
print(next(Iterator))   # H
print(next(Iterator))   # A
print(next(Iterator))   # L
print(next(Iterator))   # E
print(next(Iterator))   # D

for L in iter("KHALED"):
  print(L, end=" ")

'''
K H A L E D
'''