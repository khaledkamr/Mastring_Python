# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myfile = open("D:\khaled.txt", "a")

myfile.truncate(5) # cut the content of the file to 5 characters

print(myfile.tell()) # return the position of the cursor in the file

myfile = open("D:\khaled.txt", "r")

myfile.seek(6) # move the cursor to the entered position
print(myfile.read())

myfile.close()
os.remove("D:\khaled.txt")