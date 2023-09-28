# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = input("Enter your name : ").strip().capitalize()
uCountry = input("Enter your country and make sure the firsr letter is capital : ").strip()
isStudent = input("student or professional ? ").strip()
course = "Mastring Python"
cPrice = 100

if (uCountry == "Egypt" or uCountry == "KSA"):
  if (isStudent == "student"):
    print(f"Hello {uName} Because You Are From {uCountry} and {isStudent}")
    print(f"The Course \"{course}\" Price Is: {cPrice - 80}$")
    
  elif (isStudent == "professional"):
     print(f"Hello {uName} Because You Are From {uCountry} and {isStudent}")
     print(f"The Course \"{course}\" Price Is: {cPrice - 30}$")

elif (uCountry == "Kuwait"): 
  if (isStudent == "student"): 
    print(f"Hello {uName} Because You Are From {uCountry} and {isStudent}")
    print(f"The Course \"{course}\" Price Is: {cPrice - 50}$")

  elif (isStudent == "professional"):
     print(f"Hello {uName} Because You Are From {uCountry} and {isStudent}")
     print(f"The Course \"{course}\" Price Is: {cPrice - 30}$")

elif (uCountry == "USA"):
   if (isStudent == "student"):  
     print(f"Hello {uName} Because you are from {uCountry} and {isStudent}")
     print(f"The course \"{course}\" Prise is : {cPrice - 20}$") 

   elif (isStudent == "professional"):  
     print(f"Hello {uName} Because you are from {uCountry} and {isStudent}")
     print(f"The course \"{course}\" Prise is : {cPrice}$") 

else:
  if (isStudent == "student"):  
     print(f"Hello {uName} Because you are from {uCountry} and {isStudent}")
     print(f"The course \"{course}\" Prise is : {cPrice - 30}$") 

  elif (isStudent == "professional"):  
    print(f"Hello {uName} Because you are from {uCountry} and {isStudent}")
    print(f"The course \"{course}\" Prise is : {cPrice}$")   



print("good luck :)" if isStudent == "student" else "Enjoy your course")