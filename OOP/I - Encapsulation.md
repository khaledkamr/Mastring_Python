# Encapsulation

- Restrict Access To The Data Stored in Attirbutes and Methods
### Public
- Every Attribute and Method That We Used So Far Is Public
- Attributes and Methods Can Be Modified and Run From Everywhere
- Inside And Outside The Class
### Protected
- Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
- Attributes and Methods Prefixed With One Underscore _
### Private
- Attributes and Methods Can Be Accessed From Within The Class Or Object Only
- Attributes Cannot Be Modified From Outside The Class
- Attributes and Methods Prefixed With Two Underscores __
---------------------------------------------------------
### Attributes = Variables = Properties

## public
```python []
class member:
    def __init__(self, name):
        self.name = name 

one = member("Khaled")
print(one.name)    
one.name = "yossif"
print(one.name)    
```
#### Output
```
Khaled
yossif
```
## protected
```python []
class member:
    def __init__(self, name):
        self._name = name 

one = member("Khaled")

# it supposed that we can't access the property cuz it's protected
# but unfortunately we can
# Python use "_" just as a note for the coder to not use it out the class

print(one._name)     
one._name = "yossif" 
print(one._name)     
```
#### Output
```
Khaled
and you can change it to
yossif
```
## private
```python []
class member:
    def __init__(self, name):
        self.__name = name 

    def hello(self):
        print(f"Hello, {self.__name}")

one = member("Khaled")
one.hello()  
# print(one.__name) # AttributeError: 'member' object has no attribute '__name'

# But unfortunately you still can access the private attribute
# Python use "__" just as a note for the coder to not use it out the class

print(one._member__name)  
```
#### Output
```
Hello, Khaled
Khaled
```

