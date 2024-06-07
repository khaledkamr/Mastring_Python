# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------

file = None
tries = 5

while tries > 0:
    try:
       if (tries == 5):
           print("enter the file with absolute path")
           print(f"you have {tries} tries")

       else:
           print(f"try again, you have {tries} tries left")
        
       file_path = input("file name : ").strip()
       file = open(file_path, 'r')
       print(file.read())
       break
    
    except FileNotFoundError:
        print("the file you entered not found")
        tries -= 1

    except:
        print("something wrong happened")
        tries -= 1

    finally:
        if (file != None):
             file.close()
             print("file closed")

    tries -= 1 


else: print("you wasted your tries, try agian after an hour")