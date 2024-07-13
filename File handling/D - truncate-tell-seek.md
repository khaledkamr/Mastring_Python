# File Handling => Important Info 
```python []
import os
```
## truncate()
```python []
myfile = open("D:\khaled.txt", "a")

myfile.truncate(5) # cut the content of the file to 5 characters and remove the rest
```
## tell()
```python []
print(myfile.tell()) # return the position of the cursor in the file

myfile = open("D:\khaled.txt", "r")
```
## seek()
### The method seek takes two parameters: (offset, startpoint)
### The parameter offset specifies how many positions the cursor will be moved
### This cursor is specified by the second parameter startpoint
### It can have the follwoing values:
- 0: reference point is the beginning of the file
- 1: reference point is the current file position
- 2: reference point is the end of the file
### if the startpoint parameter is not given, it defaults to 0
```python []
myfile.seek(6) # move the cursor to the entered position
print(myfile.read())
```
### when using the startpoint 1 or 2 you should set the binary mode
```python []
myfile = open("D:\khaled.txt", "rb")

myfile.seek(6,1) 
print(myfile.read())

myfile.seek(-10,2) 
print(myfile.read())

myfile.close()
os.remove("D:\khaled.txt")
```