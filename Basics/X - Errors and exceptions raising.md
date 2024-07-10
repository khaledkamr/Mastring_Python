# Errors And Exceptions Raising 
- Exceptions Is A Runtime Error Reporting Mechanism
- Exception Gives You The Message To Understand The Problem
- Traceback Gives You The Line To Look For The Code in This Line
- Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
- Exceptions List https://docs.python.org/3/library/exceptions.html
- raise Keyword Used To Raise Your Own Exceptions
## Ex
```python []
x = input("enter username : ")

if (x != "khaled"):
    raise ValueError("username invalid")
    print("this will not print because teh error")
else:
    print(f"welcome, {x}")
```
### enter uncorrect username
```
enter username : yossif
Traceback (most recent call last):
  File "d:\coding\VS code\compile.py", line 4, in <module>
    raise ValueError("username invalid")
ValueError: username invalid
```
### enter correct username
```
enter username : khaled
welcome, khaled
```
## Try | Except | Else | Finally 
- Try     => Test The Code For Errors
- Except  => Handle The Errors
- Else    => If No Errors
- Finally => Run The Code

```python []
try: # test the errors
   num = int(input("enter your age : "))

except ValueError: # handle the errors if there is any
   print("this is not intger")

except: # you can do more than one except
   print("there is no age = 0")

else: # if there in no error
   print("ok, number is integer")

finally:
   print("this comment will be printed whatever happens")
```
