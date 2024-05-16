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

'''
#01 Os
#02 Ah
#03 Ga
#04 Al
#05 Ra
#06 Sa
#07 Ta
#08 Ma
#09 Mo
#10 Wa
All Friends Printed To Screen.
'''

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

'''
The Number 1 Is Odd.
The Number 2 Is Even.
The Number 3 Is Odd.
The Number 4 Is Even.
The Number 5 Is Odd.
The Number 6 Is Even.
The Number 7 Is Odd.
The Number 8 Is Even.
The Number 9 Is Odd.
The Loop Is Finished
'''


myName = "Khaled"

for letter in myName:

  print(f" [ {letter.upper()} ] ")

'''
 [ K ]
 [ H ]
 [ A ]
 [ L ]
 [ E ]
 [ D ]
'''

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

'''
My Progress in Lang Html Is: 90%
My Progress in Lang Css Is: 60%
My Progress in Lang PHP Is: 70%
My Progress in Lang JS Is: 80%
My Progress in Lang Python Is: 90%
My Progress in Lang MySQL Is: 60%
'''

# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue

for number in myNumbers:

  if number == 13:

    continue

  print(number)

print("#" * 50)

# Break

for number in myNumbers:

  if number == 13:

    break

  print(number)

print("#" * 50)

# Pass

for number in myNumbers:

  if number == 13:

    pass

  print(number)