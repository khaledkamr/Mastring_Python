# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------

x = input("enter positive number : ")

if (type(x) == str):
    raise ValueError("only numbers allowed")

elif(x < 0):
    raise Exception(f"the number {x} is less than zero")
    print("this will not print because teh error")

else:
    print(f"{x} is a positive number")


# -----------------------------------
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

try: # test the errors
   num = int(input("enter your age : "))

except ValueError: # handle the errors if there is any
   print("there is no age = 0")

except: # you can do than one except
   print("this is not intger")

else: # if there in no error
   print("ok, number is integer")

finally:
   print("this comment will be printed whatever happens")
