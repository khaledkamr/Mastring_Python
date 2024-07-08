# User Input
```python []
fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middle Name?')
lName = input('What\'s Is Your Last Name?')
```
### if there are spaces in the string you can delete them by strip() function

### if you want to make the first letter of the string capital and the others small
### you can use capitalize() function
```python []
fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s}. {lName} Happy To See You.")
```
#### Input
```
khaled
kamr
rashad
```
#### output
```
Hello Khaled K. Rashad Happy To See You.
```