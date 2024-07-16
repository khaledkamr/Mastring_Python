# Class Syntax and Info 
- Class is The Blueprint Or Construtor Of The Object
- Class Instantiate Means Create Instance of A Class
- Instance => Object Created From Class And Have Their Methods and Attributes
- Class Defined With Keyword class
- Class Name Written With PascalCase [UpperCamelCase] Style
- Class May Contains Methods and Attributes
- When Creating Object Python Look For The Built In __init__ Method
- __init__ Method Called Every Time You Create Object From Class
- __init__ Method Is Initialize The Data For The Object
- Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
- self Refer To The Current Instance Created From The Class And Must Be First Param
- self Can Be Named Anything
- In Python You Dont Need To Call new() Keyword To Create Object
-------------------------------------------------------------------
####  Syntax
```
class Name:
    Constructor => Do Instantiation [ Create Instance From A Class ]
    Each Instance Is Separate Object
    def __init__(self, other_data)
        Body Of Function
```
```python []
class Member:
  def __init__(self):
    print("A New Member Has Been Added") #this message will be printed every time instance created

member_one = Member()  #instance
member_two = Member()  #instance
member_three = Member()  #instance

print(member_one.__class__)
```
#### Output
```
A New Member Has Been Added
A New Member Has Been Added
A New Member Has Been Added
<class '__main__.Member'>
```