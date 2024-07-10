# Decorators => Intro
- Sometimes Called Meta Programming
- Everything in Python is Object Even Functions
- Decorator Take A Function and Add Some Functionality and Return It
- Decorator Wrap Other Function and Enhance Their Behaviour
- Decorator is Higher Order Function (Function Accept Function As Parameter)
```python []
def myDecorator(func):  # Decorator
  def nestedFunc():  # Any Name Its Just For Decoration
    print("Before")  # Message From Decorator
    func()   # Execute Function
    print("After")  # Message From Decorator

  return nestedFunc  # Return All Data

@myDecorator
def sayHello():
  print("Hello From Say Hello Function")

def sayHowAreYou():
  print("Hello From Say How Are You Function")

sayHello()
```
#### Output
```
Before
Hello From Say Hello Function
After
```
### Another way for decoration
```python []
afterDecoration = myDecorator(sayHowAreYou)
afterDecoration()
sayHowAreYou()
```
#### Output
```
Before
Hello From Say How Are You Function
After
Hello From Say How Are You Function
```

## Function With Parameters 
```python []
def myDecorator(func):  
  def nestedFunc(n1, n2):  
    print("Before") 
    func(n1, n2)  
    print("After")  

  return nestedFunc 

def myDecorator2(func): 
  def nestedFunc(num1, num2):  
    print("Coming From Decorator Two")
    func(num1, num2)  

  return nestedFunc  

@myDecorator
@myDecorator2
def calc(n1, n2):
  print(n1 + n2)

calc(10, 90)
```
#### Output
```
Before
Coming From Decorator Two
100
After
```

## Function With Unlimited Parameters

```python []
def dec(func):
    def fun(*nums):
        print("before")
        for n in nums:
             if n < 0:
                 print("one of the elements is negative")
        func(*nums)
        print("after")

    return fun

@dec
def calc(n1, n2, n3):
    print(n1 + n2 + n3)

calc(10, 10, 10)
```
#### Output
```
before
30
after
```