# Dictionary 
- Dict Items Are Enclosed in Curly Braces
- Dict Items Are Contains Key : Value
- Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
- [4] Dict Value Can Have Any Data Types
- [5] Dict Key Need To Be Unique
- [6] Dict Is Not Ordered You Access Its Element With Key
```python []
user = {
  "name": "Khaled",
  "age": 36,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}

print(user)                
print(user['country'])      
print(user.get("country"))  
print(user.keys())          
print(user.values())       
```
#### Output
```
{'name': 'Khaled', 'age': 36, 'country': 'Egypt', 'skills': ['Html', 'Css', 'JS'], 'rating': 10.5}
Egypt
Egypt
dict_keys(['name', 'age', 'country', 'skills', 'rating'])
dict_values(['Khaled', 36, 'Egypt', ['Html', 'Css', 'JS'], 10.5])
```
## Two-Dimensional Dictionary
```python []
languages = {
  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages)                  
print(languages['One'])           
print(languages['Three']['name'])  
```
#### Output
```
{'One': {'name': 'Html', 'progress': '80%'}, 'Two': {'name': 'Css', 'progress': '90%'}, 'Three': {'name': 'Js', 'progress': '90%'}}
{'name': 'Html', 'progress': '80%'}
Js
```
## Dictionary Length
```python [] 
print(len(languages))         
print(len(languages["Two"]))  
```
#### Output
```
3
2
```
## Create Dictionary From Variables
```python []
frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)   
```
#### Output
```
{'one': {'name': 'Vuejs', 'progress': '80%'}, 'two': {'name': 'ReactJs', 'progress': '80%'}, 'three': {'name': 'Angular', 'progress': '80%'}}
```
# Dictionary Methods 

## clear()
```python []
user = {
  "name": "Khaled"
}
print(user)      
user.clear()
print(user)      
```
#### Output
```
{'name': 'Khaled'}
{}
```
## update()
```python []
member = {
  "name": "Khaled"
}
print(member)         # {'name': 'Khaled'}
member["age"] = 36
print(member)         # {'name': 'Khaled', 'age': 36}
member.update({"country": "Egypt"})
print(member)         # {'name': 'Khaled', 'age': 36, 'country': 'Egypt'}
```
#### Output
```
{'name': 'Khaled'}
{'name': 'Khaled', 'age': 36}
{'name': 'Khaled', 'age': 36, 'country': 'Egypt'}
```
## copy()
```python []
main = {
  "name": "Khaled"
}

b = main.copy()
print(b)       
main.update({"skills": "Fighting"})
print(main)    # 
print(b)       # 
```
#### Output
```
{'name': 'Khaled'}
{'name': 'Khaled', 'skills': 'Fighting'}
{'name': 'Khaled'}
```
## keys() + values()
```python []
print(main.keys())   
print(main.values()) 
```
#### Output
```
dict_keys(['name', 'skills'])
dict_values(['Khaled', 'Fighting'])
```
## setdefault()
```python []
user = {
  "name": "Khaled"
}
print(user)  
print(user.setdefault("age", 36))  
print(user)    
```
#### Output
```
{'name': 'Khaled'}
36
{'name': 'Khaled', 'age': 36}
```
## popitem()
```python []
member = {
  "name": "Khaled",
  "skill": "PS4"
}
print(member)   
member.update({"age": 36})
print(member.popitem())    
```
#### Output
```
{'name': 'Khaled', 'skill': 'PS4'}
('age', 36)
```
## items()
```python []
view = {
  "name": "Khaled",
  "skill": "XBox"
}

allItems = view.items()
print(view)      
view["age"] = 36

print(allItems)  
```
#### Output
```
{'name': 'Khaled', 'skill': 'XBox'}
dict_items([('name', 'Khaled'), ('skill', 'XBox'), ('age', 36)])
```
## fromkeys()
```python []
a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b)) 
```
#### Output
```
 {'MyKeyOne': 'X', 'MyKeyTwo': 'X', 'MyKeyThree': 'X'}
```