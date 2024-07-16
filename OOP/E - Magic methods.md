# Magic Methods 
### Everything in Python is An Object
### \_\_ init__ Called Automatically When Instantiating Class
### self.\_\_class__ The class to which a class instance belongs
### \_\_str__   Gives a Human-Readable Output of the Object
### \_\_len__   Returns the Length of the Container, <br> Called When We Use the Built-in len() Function on the Object
------------------------------------------------------
```python
class Skill:
  def __init__(self):
    self.skills = ["Html", "Css", "Js"]

  def __str__(self):
    return f"This is My Skills => {self.skills}"

  def __len__(self):
    return len(self.skills)

profile = Skill()
print(profile)      
print(len(profile)) 

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))  
print(profile.__class__)  

my_string = "Osama"
print(my_string.__class__)  
print(str.upper(my_string)) 
```
#### Output
```
This is My Skills => ['Html', 'Css', 'Js']
3
5
<class '__main__.Skill'>
<class 'str'>
OSAMA
```