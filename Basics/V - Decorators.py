# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------

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

'''
Before
Hello From Say Hello Function
After
'''

print("=" * 40)

afterDecoration = myDecorator(sayHowAreYou)
afterDecoration()

'''
Before
Hello From Say How Are You Function
After
'''

print("=" * 40)  

sayHowAreYou()

'''
Hello From Say How Are You Function
'''

print("=" * 40)

# ------------------------------
# -- Function With Parameters --
# ------------------------------

def myDecorator(func):  # Decorator

  def nestedFunc(n1, n2):  # Any Name Its Just For Decoration

    print("Before")  # Message From Decorator

    func(n1, n2)  # Execute Function

    print("After")  # Message From Decorator

  return nestedFunc  # Return All Data

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

'''
Before
Coming From Decorator Two
100
After
'''

# ----------------------------------------
# -- Function With Unlimited Parameters --
# ----------------------------------------


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

'''
before
30
after
'''