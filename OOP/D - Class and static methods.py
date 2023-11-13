# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------

class Member:

  not_allowed_names = ["Hell", "Shit", "Baloot"]

  users_num = 0

  @classmethod
  def show_users_count(cls):

    print(f"We Have {cls.users_num} Users In Our System.")

  @staticmethod
  def say_hello():

    print("Hello From Static Method")

  def __init__(self, first_name, middle_name, last_name, gender):

    self.fname = first_name

    self.mname = middle_name

    self.lname = last_name

    self.gender = gender

    Member.users_num += 1 

    if self.fname in Member.not_allowed_names:
      
      raise ValueError("Name Not Allowed")

  def full_name(fullName): 

    return f"{fullName.fname} {fullName.mname} {fullName.lname}"

  def name_with_title(title):

    if title.gender == "Male":

      return f"Hello Mr {title.fname}"

    elif title.gender == "Female":

      return f"Hello Miss {title.fname}"

    else:

      return f"Hello {title.fname}"

  def get_all_info(Info):

    return f"{Info.name_with_title()}, Your Full Name Is: {Info.full_name()}"

  def delete_user(delete):

    Member.users_num -= 1  

    return f"User {delete.fname} Is Deleted."


member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
#member_four = Member("Shit", "Hell", "Metal", "DD")

Member.show_users_count()

print("=" * 50)

print(member_one.full_name())
print(Member.full_name(member_one))

Member.say_hello()