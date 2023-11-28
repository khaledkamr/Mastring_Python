# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------

def checkPass(password):
    '''
    check password function
         it says welcome poss
    parameter:
         password -> the password of the user
    return:
         return hello poss if the password correct, and password uncorrect otherwise
    '''
    if(password == 12345):
         print(f"hello poss")
    else : 
         print("password uncorrect!")
   

key = int(input("Enter your password : "))
checkPass(key)

print(dir(checkPass))

print(checkPass.__doc__)

help(checkPass)