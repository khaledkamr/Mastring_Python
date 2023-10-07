# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop

  print(f"{name} Skills Is: ")

  for skill in skills:  # Inner Loop

    print(f"- {skill}")


# Dictionary

peoples = {
  "Khaled": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Osama": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

for name in peoples:

  print(f"Skills and Progress For {name} Is: ")

  for skill in peoples[name]: # "Html" "Css" "Js"

    print(f"{skill.upper()} => {peoples[name][skill]}")

  else : print(" ")


# Advanced Dictionary Loop

mySkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%"
}

for skill_key, skill_progress in mySkills.items():

  print(f"{skill_key} => {skill_progress}")

#######################

myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key, main_value in myUltimateSkills.items():

  print(f"{main_key} Progress Is: ")

  for child_key, child_value in main_value.items():

    print(f"- {child_key} => {child_value}")

  else: print(" ")
