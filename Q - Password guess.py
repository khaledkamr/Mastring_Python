# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4
mainPassword = "Khaled@123"
inputPassword = input("Enter Your Password : ")

while (inputPassword != mainPassword):
  
  tries -= 1 
  print(f"Wrong Password, {'Last' if tries == 0 else tries} Chance Left")
  
  inputPassword = input("Write Your Password: ")

  if (tries == 0):
    print("All Tries Is Finished.")
    break
    print("Will Not Print")

else:
  print("Correct Password")