# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------

class member:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def say_hello(self):

        return f"Hello, {self.name}"
    
    @property
    def ageInDays(self): # this now consder as a property not a method

        return self.age * 365
    
one = member("khaled", 20)
print(one.say_hello())   # Hello, khaled
print(one.ageInDays)     # 7300