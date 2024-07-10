# Generators 
- Generator is a Function With "yield" Keyword Instead of "return"
- It Support Iteration and Return Generator Iterator By Calling "yield"
- Generator Function Can Have one or More "yield"
- By Using next() It Resume From Where It Called "yield" Not From Begining
- When Called, Its Not Start Automatically, Its Only Give You The Control
```python []
def Gen():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5

myGen = Gen()

print(next(myGen)) 
print(next(myGen)) 
print(next(myGen)) 
print("\nnow generator iterator stoped at yeild 3")
```
#### Output
```
1
2
3

now generator iterator stoped at yeild 3
```
### and the for loop while resume from there
```python []
for num in myGen:
  print(num)
```
#### Output
```
4
5
```