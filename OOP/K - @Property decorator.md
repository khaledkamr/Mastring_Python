# @Property Decorator 
```python []
class member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello, {self.name}"
    
    @property
    # this now consider as a property not a method
    def ageInDays(self): 
        return self.age * 365
    
one = member("khaled", 20)
print(one.say_hello())   
print(one.ageInDays)     
```
#### Output
```
Hello, khaled
7300
```