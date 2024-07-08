# If, Elif, Else 
- control flow
- make decisions
```python []
uName = "Khaled"
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
```
#### Output
```
Hello Khaled Because You Are From Kuwait
The Course "Python Course" Price Is: $50
```
## Membership Operators
- in
- not in

## String
```python []
name = "khaled"
print("k" in name)    
print("a" in name)    
print("A" in name)    
```
#### Output
```
True
True
False
```
## List
```python []
friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Khaled" in friends)              
print("Sayed" in friends)               
print("Mahmoud" not in friends)         
```
#### Output
```
False
True
False
```
## Using In and Not In With Condition
```python []
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
```
#### Output
```
Hello You Have A Discount Equal To $50
```