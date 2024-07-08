# For Nested Loops
```python []
peoples = ["Khaled", "Ahmed", "Sayed", "Ali"]
skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop
  print(f"{name} Skills Is: ")
  for skill in skills:  # Inner Loop
    print(f"- {skill}")
```
#### Output
```
Khaled Skills Is: 
- Html
- Css
- Js
Ahmed Skills Is:
- Html
- Css
- Js
Sayed Skills Is:
- Html
- Css
- Js
Ali Skills Is:
- Html
- Css
- Js
```

## Dictionary
```python []
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
```
#### Output
```
Skills and Progress For Khaled Is: 
HTML => 70%
CSS => 80%
JS => 70%

Skills and Progress For Ahmed Is:
HTML => 90%
CSS => 80%
JS => 90%

Skills and Progress For Osama Is:
HTML => 70%
CSS => 60%
JS => 90%
```
## Advanced Dictionary Loop
```python []
mySkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%"
}

for skill_key, skill_progress in mySkills.items():
  print(f"{skill_key} => {skill_progress}")
```
#### Output
```
HTML => 80%
CSS => 90%
JS => 70%
PHP => 80%
```
```python []
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
```
#### Output
```
HTML Progress Is: 
- Main => 80%
- Pugjs => 80%

CSS Progress Is:
- Main => 90%
- Sass => 70%

```