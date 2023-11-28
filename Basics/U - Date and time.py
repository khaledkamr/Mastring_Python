# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

print(dir(datetime))
print(dir(datetime.datetime))
print("=" * 40)

# Print The Current Date and Time
print(datetime.datetime.now())
print("=" * 40)

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)
print("=" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("=" * 40)
print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())
print("=" * 40)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)
print("=" * 40)

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)
print("=" * 40)

# Print Specific Date
print(datetime.datetime(2003, 7, 3))
print(datetime.datetime(2003, 7, 3, 10, 45, 55, 150364))
print("=" * 40)

myBirthDay = datetime.datetime(2003, 7, 3)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")
print("=" * 40)

# -----------------
# -- Format Date --
# -----------------
# https://strftime.org/
# ---------------------

import datetime

myBirthday = datetime.datetime(2003, 7, 3)

print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))