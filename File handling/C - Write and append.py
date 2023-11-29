# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myfile = open("D:\khaled.txt", "w")

# the write mode overwrite the file
myfile.write("hello from python\n")
myfile.write("new line\n")

myList = ["khaled\n", "yossif\n", "ahmed\n"]

for name in myList:
    myfile.write(name)

myfile.writelines(myList)

# the append mode doesn't overwrite the file
myfile = open("D:\khaled.txt", "a")
myfile.write("hello from append")

myfile.close()