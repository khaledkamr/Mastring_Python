# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------

class Skill:

  def __init__(self):

    self.skills = ["Html", "Css", "Js"]

  def __str__(self):

    return f"This is My Skills => {self.skills}"

  def __len__(self):

    return len(self.skills)

profile = Skill()
print(profile)       # This is My Skills => ['Html', 'Css', 'Js']
print(len(profile))  # 3

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))  # 5

print(profile.__class__)  # <class '__main__.Skill'>

my_string = "Osama"
print(type(my_string))     # <class 'str'>
print(my_string.__class__) # <class 'str'>
print(dir(str))
print(str.upper(my_string)) # OSAMA