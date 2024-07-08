# Boolean 
- In Programming You Need to Known Your If Your Code Output is True Or False
- Boolean Values Are The Two Constant Objects False + True.
```python []
name = " "
print(name.isspace())
print(100 > 200)     
print(100 > 100)     
print(100 > 90)      
```
#### output
```
True
False
False
True
```
## True Values
```python []
print(bool("Osama"))
print(bool(100))    
print(bool(100.95)) 
print(bool(True))   
print(bool([1, 2, 3, 4, 5]))  
```
#### output
```
True
False
False
True
```

## False Values
```python []
print(bool(0))       
print(bool(""))      
print(bool(''))      
print(bool([]))      
print(bool(False))   
print(bool(()))      
print(bool({}))      
print(bool(None))    
```
#### output
```
False
False
False
False
False
False
False
False
```
# Boolean Operators
- and
- or
- not
```python []
age = 36
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 0)
print(age > 16 and country == "KSA" and rank > 0)  

print(age > 40 or country == "KSA" or rank > 20)  
print(age > 40 or country == "Egypt" or rank > 20) 

print(age > 16)  
print(not age > 16) 
```
#### output
```
True
False
False
True
True
False
```

# Comparison Operators 
- [ == ] Equal
- [ != ] Not Equal
- [ > ] Greater Than
- [ < ] Less Than
- [ >= ] Greater Than Or Equal
- [ <= ] Less Than Or Equal

## Equal + Not Equal
```python []
print(100 == 100)    
print(100 == 100.00) 

print(100 != 100)    
print(100 != 100.00) 
```
#### Output
```
True
True
False
False
```
## Greater Than + Less Than
```python
print(100 > 100)      
print(100 > 40)       

print(100 < 100)      
print(100 < 200)      
```
#### Output
```
False
True
False
True
```
## Greater Than Or Equal + Less Than Or Equal
```python []
print(100 >= 100)      
print(100 >= 40)       

print(100 <= 100)      
print(100 <= 200)      
print(100 <= 40)       
```
#### Output
```
True
True
True
True
False
```