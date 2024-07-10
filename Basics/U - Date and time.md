# Date and Time => Introduction 
```python []
import datetime
```
## Print The Current Date and Time
```python []
print(datetime.datetime.now())  
```
#### Output
```
2024-07-10 11:38:31.602747
```

## Print The Current Year
```python []
print(datetime.datetime.now().year)    
```
#### Output
```
2024
```
## Print The Current Month
```python []
print(datetime.datetime.now().month)  
```
#### Output
```
7
```
## Print The Current Day
```python []
print(datetime.datetime.now().day)    
```
#### Output
```
10
```

## Print Start and End Of Date
```python []
print(datetime.datetime.min)   
print(datetime.datetime.max)   
```
#### Output
```
0001-01-01 00:00:00
9999-12-31 23:59:59.999999
```
## Print The Current Time
```python []
print(datetime.datetime.now().time()) 
```
#### Output
```
11:44:56.184371
```
## Print The Current Time Hour
```python []
print(datetime.datetime.now().time().hour)   
```
#### Output
```
11
```
## Print The Current Time Minute
```python []
print(datetime.datetime.now().time().minute) 
```
#### Output
```
45
```
## Print The Current Time Second
```python []
print(datetime.datetime.now().time().second)
```
#### Output
```
55
```
## Print Start and End Of Time
```python []
print(datetime.time.min)  
print(datetime.time.max)  
```
#### Output
```
00:00:00
23:59:59.999999
```
## Print Specific Date
```python []
print(datetime.datetime(2003, 7, 3)) 
print(datetime.datetime(2003, 7, 3, 10, 45, 55, 150364))  

myBirthDay = datetime.datetime(2003, 7, 3)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")  

print(f" I Lived For {dateNow - myBirthDay}")  
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")   
```
#### Output
```
2003-07-03 00:00:00
2003-07-03 10:45:55.150364
My Birthday is 2003-07-03 00:00:00 And Date Now Is 2024-07-10 11:49:31.385686
 I Lived For 7678 days, 11:49:31.385686
 I Lived For 7678 Days.
```
# Format Date

### https://strftime.org/
```python []
import datetime

myBirthday = datetime.datetime(2003, 7, 3)

print(myBirthday)                  # 2003-07-03 00:00:00
print(myBirthday.strftime("%a"))   # Thu
print(myBirthday.strftime("%A"))   # Thursday
print(myBirthday.strftime("%b"))   # Jul
print(myBirthday.strftime("%B"))   # July

print(myBirthday.strftime("%d %B %Y"))       # 03 July 2003
print(myBirthday.strftime("%d, %B, %Y"))     # 03, July, 2003
print(myBirthday.strftime("%d/%B/%Y"))       # 03/July/2003
print(myBirthday.strftime("%d - %B - %Y"))   # 03 - July - 2003
print(myBirthday.strftime("%B - %Y"))        # July - 2003
```