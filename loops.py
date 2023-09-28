# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

i = 0

while (i < len(myF)):  # i < 10

  print(f"#{str(i + 1).zfill(2)} {myF[i]}")
  i += 1 

else:
  print("All Friends Printed To Screen.")

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])

# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in Numbers:

  if (num % 2 == 0):  
    print(f"The Number {num} Is Even.")

  else:
    print(f"The Number {num} Is Odd.")

else:
  print("The Loop Is Finished")


myName = "Khaled"

for letter in myName:

  print(f" [ {letter.upper()} ] ")

# Range

myRange = range(1, 101)

for number in myRange:

  print(number)

# Dictionary

mySkills = {
  "Html": "90%",
  "Css": "60%",
  "PHP": "70%",
  "JS": "80%",
  "Python": "90%",
  "MySQL": "60%"
}

for skill in mySkills:

  print(f"My Progress in Lang {skill} Is: {mySkills[skill]}") 