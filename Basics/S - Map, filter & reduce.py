# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function

def formatText(text):
  return f"- {text.strip().capitalize()} -"

myTexts = [" khaled ", "kamr", "  ahmed  "]

myFormatedData = map(formatText, myTexts)

print(myFormatedData)

for name in myFormatedData:
  print(name)

print("=" * 50)

# Use Map With Lambda Function

def formatText(text):
  return f"- {text.strip().capitalize()} -"

myTexts = [" OSama ", "AHMED", "  sAYed  "]

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):
  print(name)



# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Ex1:

def checkNumber(num):
  return num > 10

myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)

for num in myResult:
  print(num)

print("#" * 50)

# Ex2:

def checkName(name):
  return name.startswith("O")

myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnedData = filter(checkName, myTexts)

for person in myReturnedData:
  print(person)

print("#" * 50)

# Ex3:

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

for p in filter(lambda name: name.startswith("A"), myNames):
  print(p)


# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

from functools import reduce

def sumAll(num1, num2):

  return num1 + num2

numbers = [1, 8, 2, 9, 100]

result = reduce(sumAll, numbers)

#result = reduce(lambda num1, num2: num1 + num2, numbers)

print(result)

# ((((1 + 8) + 2) + 9) + 100)