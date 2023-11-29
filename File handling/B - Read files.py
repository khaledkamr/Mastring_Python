# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myfile = open("D:\khaled.txt", "r")

# print(myfile) # data object
# print(myfile.name)
# print(myfile.mode)
# print(myfile.encoding)

# print(myfile.read()) # read all the content of the file
# print(myfile.read(5)) # read 5 characters from the file 

# print(myfile.readline()) # read one line
# print(myfile.readline(5)) # read 5 characters from the line

# print(myfile.readlines()) # read all the lines

for line in myfile:

    print(line)

    if line.startswith("4"): break

myfile.colse()
