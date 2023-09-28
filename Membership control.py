# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Yassen", "Khaled", "Yossif", "Shahd", "Yomna", "Ziad", "Anas"]

name = input("Please Type Your Name ").strip().capitalize()

if (name in admins):
  print(f"Hello {name}, Welcome Back")

  option = input("Delete Or Update Your Name ?").strip().lower()

  # Update option
  if (option == 'update'):
    theNewName = input("Your New Name Please ").strip().capitalize()

    admins[admins.index(name)] = theNewName

    print("Name Updated.")
    print(admins)

  # Delete Option
  elif  (option == 'delete'):
    admins.remove(name)

    print("Name Deleted")
    print(admins)

  # Wrong Option
  else:
    print("Wrong Option choose again")

else:
  status = input("Not Admin, Wanna be Added ? (Yes or No) ").strip().lower()

  if  (status == "yes"):
    print("You Have Been Added")

    admins.append(name)
    print(admins)

  else:
    print("You Are Not Added.")