# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Osama"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "Kuwait":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

print("=" * 50)

# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "khaled"
print("k" in name)    # True
print("a" in name)    # True
print("A" in name)    # False

print("=" * 50)

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Khaled" in friends)                # False
print("Sayed" in friends)                # True
print("Mahmoud" not in friends)          # False

print("=" * 50)

# Using In and Not In With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Italy"

if (myCountry in countriesOne):
  print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

elif (myCountry in countriesTwo):
  print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")

else:
  print("You Have No Discount")