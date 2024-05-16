# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

print(dir(datetime))
print(dir(datetime.datetime))
print("=" * 40)

# Print The Current Date and Time
print(datetime.datetime.now())  # 2024-05-16 23:07:44.144474
print("=" * 40)

# Print The Current Year
print(datetime.datetime.now().year)   # 2024

# Print The Current Month
print(datetime.datetime.now().month)  # 5

# Print The Current Day
print(datetime.datetime.now().day)    # 16
print("=" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)   # 0001-01-01 00:00:00
print(datetime.datetime.max)   # 9999-12-31 23:59:59.999999

print("=" * 40)
print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())  # 23:07:44.146067
print("=" * 40)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)   # 23

# Print The Current Time Minute
print(datetime.datetime.now().time().minute) # 7

# Print The Current Time Second
print(datetime.datetime.now().time().second) # 44
print("=" * 40)

# Print Start and End Of Time
print(datetime.time.min)    # 00:00:00
print(datetime.time.max)    # 23:59:59.999999
print("=" * 40)

# Print Specific Date
print(datetime.datetime(2003, 7, 3))  # 2003-07-03 00:00:00
print(datetime.datetime(2003, 7, 3, 10, 45, 55, 150364))  # 2003-07-03 10:45:55.150364
print("=" * 40)

myBirthDay = datetime.datetime(2003, 7, 3)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")   # My Birthday is 2003-07-03 00:00:00 And Date Now Is 2024-05-16 23:07:44.146067    

print(f" I Lived For {dateNow - myBirthDay}")   #  I Lived For 7623 days, 23:07:44.146067
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")   #  I Lived For 7623 Days.
print("=" * 40)

# -----------------
# -- Format Date --
# -----------------
# https://strftime.org/
# ---------------------

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