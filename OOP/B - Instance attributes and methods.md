# Instance Attributes and Methods 
- Self: Point To Instance Created From Class
- Instance Attributes: Instance Attributes Defined Inside The Constructor
- Instance Methods: Take Self Parameter Which Point To Instance Created From Class
- Instance Methods Can Have More Than One Parameter Like Any Function
- Instance Methods Can Freely Access Attributes And Methods On The Same Object
- Instance Methods Can Access The Class Itself

```python []
class Member:
  def __init__(self, first_name, middle_name, last_name, gender):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name
    self.gender = gender

  def full_name(self):  #method
    return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):  #method
    if self.gender == "Male":
      return f"Hello Mr {self.fname}"
    elif self.gender == "Female":
      return f"Hello Miss {self.fname}"
    else:
      return f"Hello {self.fname}"

  def get_all_info(self):  #method
    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"


member_one = Member("khaled", "kamr", "rashad", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname) 
print(member_two.fname)   
print(member_three.fname) 

print(member_two.full_name())  
print(member_two.name_with_title())  

print(member_one.get_all_info())  
```
#### Output
```
khaled kamr rashad
Ahmed
Mona
Ahmed Ali Mahmoud
Hello Mr Ahmed
Hello Mr khaled, Your Full Name Is: khaled kamr rashad
```