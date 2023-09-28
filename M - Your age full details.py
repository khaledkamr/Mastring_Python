#second project

# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

print("tip : write only the first letter of the time unit")
age = int(input("enter your age : ").strip())
unit = input("Choose time unit:(months, weeks, days, hours, mintes, seconds)? ").lower()

# get in all time units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
mintes = hours * 60
seconds = mintes * 60

if (unit == "m"):
    print("you chose the unit months")
    print(f"you lived for {months:,} months.")

elif (unit == "w"):
    print("you chose the unit weeks")
    print(f"you lived for {weeks:,} weeks")

elif (unit == "d"):
    print("you chose the unit days")
    print(f"you lived for {days:,} days")

elif (unit == "h"):
    print("you chose the unit hours")
    print(f"you lived for {hours:,} hours")

elif (unit == "mi"):
    print("you chose the unit mintes")
    print(f"you lived for {mintes:,} mintes")

elif (unit == "s"):
    print("you chose the unit seconds")
    print(f"you lived for {seconds:,} seconds")