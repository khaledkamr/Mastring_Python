# -------------------
# -- File Handling --
# -------------------
# Modes:
# "a" Append   Open File For Appending Values, Create File If Not Exists
# "r" Read     [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write    Open File For Writing, Create File If Not Exists
# "x" Create   Create File, Give Error If File Exists
# "rb" Binary  return contents as bytes objects without any decoding
# --------------------------------------------------

# open() -> take two parameter, first one the file name, second is the mode,
# the mode is 'r' by default if no mode entered
file = open("D:\khaled.txt")

import os

# get the current working directory
print(os.getcwd()) 

# get the absolute path of the opening file
abspath = os.path.abspath(__file__)
print(abspath) 

# get the directory for the opening file
dir = os.path.dirname(abspath)
print(dir) 

# change current working directory
os.chdir(dir)































