# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------

name = " "
print(name.isspace())  # True

print("=" * 50)

print(100 > 200)     # False
print(100 > 100)     # False
print(100 > 90)      # True

print("=" * 50)

# True Values

print(bool("Osama"))    # True
print(bool(100))    # True
print(bool(100.95))    # True
print(bool(True))    # True
print(bool([1, 2, 3, 4, 5]))    # True

print("=" * 50)

# False Values

print(bool(0))        # False
print(bool(""))       # False
print(bool(''))       # False
print(bool([]))       # False
print(bool(False))    # False
print(bool(()))       # False
print(bool({}))       # False
print(bool(None))     # False

print("=" * 50)

# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # False

# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# --------------------------

# Equal + Not Equal

print(100 == 100)       # True
print(100 == 100.00)    # True

print("=" * 50)

print(100 != 100)      # False
print(100 != 100.00)   # False

print("=" * 50)

# Greater Than + Less Than

print(100 > 100)       # False
print(100 > 200)       # False
print(100 > 100.00)    # False
print(100 > 40)        # True

print("=" * 50)

print(100 < 100)       # False
print(100 < 200)       # True
print(100 < 100.00)    # False
print(100 < 40)        # False

print("=" * 50)

# Greater Than Or Equal + Less Than Or Equal

print(100 >= 100)      # True
print(100 >= 200)      # False
print(100 >= 100.00)   # True
print(100 >= 40)       # True

print("=" * 50)

print(100 <= 100)      # True
print(100 <= 200)      # True
print(100 <= 100.00)   # True
print(100 <= 40)       # False

print("=" * 50)