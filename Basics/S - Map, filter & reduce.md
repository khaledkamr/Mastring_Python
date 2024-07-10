# Built In Functions => Map
- Map Take A Function + Iterator
- Map Called Map Because It Map The Function On Every Element
- The Function Can Be Pre-Defined Function or Lambda Function

## Use Map With Predefined Function
```python []
def formatText(text):
  return f"- {text.strip().capitalize()} -"

myTexts = [" khaled ", "kamr", "  ahmed  "]
myFormatedData = map(formatText, myTexts)
print(myFormatedData)   

for name in myFormatedData:
  print(name)
```
#### Output
```
<map object at 0x0000021CC7C4BEE0>
- Khaled -
- Kamr -
- Ahmed -
```

## Use Map With Lambda Function
```python []
def formatText(text):
  return f"- {text.strip().capitalize()} -"

myTexts = [" KHaled ", "AHMED", "  sAYed  "]

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):
  print(name)
```
#### Output
```
- Khaled -
- Ahmed -
- Sayed -
```

# Built In Functions => Filter - 
- Filter Take A Function + Iterator
- Filter Run A Function On Every Element
- The Function Can Be Pre-Defined Function or Lambda Function
- Filter Out All Elements For Which The Function Return True
- The Function Need To Return Boolean Value

## Ex1:
```python []
def checkNumber(num):
  return num > 10

myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]
myResult = filter(checkNumber, myNumbers)

for num in myResult:
  print(num)
```
#### Output
```
19
20
100
```

## Ex2:
```python []
def checkName(name):
  return name.startswith("O")

myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]
myReturnedData = filter(checkName, myTexts)

for person in myReturnedData:
  print(person)
```
#### Output
```
Osama
Omer
Omar
Othman
```

## Ex3:
```python []
myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

for p in filter(lambda name: name.startswith("A"), myNames):
  print(p)
```
#### Output
```
Ahmed
Ameer
```

# Built In Functions => Reduce 
- Reduce Take A Function + Iterator
- Reduce Run A Function On FIrst and Second Element And Give Result
- Then Run Function On Result And Third Element
- Then Run Function On Rsult And Fourth Element And So On
- Till One ELement is Left And This is The Result of The Reduce
- The Function Can Be Pre-Defined Function or Lambda Function

## Ex:
```python []
from functools import reduce

def sumAll(num1, num2):
  return num1 + num2

numbers = [1, 8, 2, 9, 100]
result = reduce(sumAll, numbers)

# Using lambda
# result = reduce(lambda num1, num2: num1 + num2, numbers)
 
print(result)  

# ((((1 + 8) + 2) + 9) + 100)
```
#### Output
```
120
```