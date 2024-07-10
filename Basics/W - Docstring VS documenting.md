# DocString & Commenting vs Documenting 
- Documentation String For Class, Module or Function
- Can Be Accessed From The Help and Doc Attributes
- Made For Understanding The Functionality of The Complex Code
- Theres One Line and Multiple Line Doc Strings
```python []
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
```
#### Output
```
Enter your password : 12345
hello poss

    check password function
         it says welcome poss
    parameter:
         password -> the password of the user
    return:
         return hello poss if the password correct, and password uncorrect otherwise

Help on function checkPass in module __main__:

checkPass(password)
    check password function
         it says welcome poss
    parameter:
         password -> the password of the user
    return:
         return hello poss if the password correct, and password uncorrect otherwise

```