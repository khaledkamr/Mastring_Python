# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------

class Member:
  
  #attributes specific to the class only

  not_allowed_names = ["Hell", "Shit", "fuck"]

  users_num = 0

  def __init__(self, first_name, middle_name, last_name, gender):

    self.fname = first_name

    self.mname = middle_name

    self.lname = last_name

    self.gender = gender

    Member.users_num += 1  #user counter

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

    Member.users_num -= 1  # Member.users_num = Member.users_num -1

    return f"User {delete.fname} Is Deleted."


print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

print(Member.users_num)

print(member_four.delete_user())

print(Member.users_num)

#print(dir(member_one))

print(member_two.full_name())
print(member_two.name_with_title())

print(member_three.get_all_info())

#print(dir(Member))