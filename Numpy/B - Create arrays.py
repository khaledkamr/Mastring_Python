# ----------------------------
# -- Numpy => Create Arrays --
# ----------------------------

import numpy as np

mylist = [1,2,3,4]
myarray = np.array(mylist)

print(type(mylist))     # <class 'list'>
print(mylist)           # [1, 2, 3, 4]
print(type(myarray))    # <class 'numpy.ndarray'>
print(myarray)          # [1 2 3 4]

print('=' * 50)

# Accessing elements

print(mylist[0])     # 1
print(myarray[0])    # 1

print('=' * 50)

a = np.array(10) # Zero dimensional array
b = np.array([10, 20]) # One dimensional array
c = np.array([[1,2], [3,4]]) # two dimensional array 
d = np.array([[[5,6], [7,9]], [[1,3], [4,8]]]) # three dimensional array

print(d[0])          # [[5 6] [7 9]]
print(d[1])          # [[1 3] [4 8]]
print(d[1][1])       # [4 8]
print(d[1][1][1])    # 8
print(d[1, 1, 1])    # 8
print(d[1, 1, -1])   # 8  (last element)

print('=' * 50)

# Number of dimensions

print(a.ndim)       # 0
print(b.ndim)       # 1
print(c.ndim)       # 2
print(d.ndim)       # 3

# Custom dimension

custom_array = np.array([1, 2, 3], ndmin=3)
print(custom_array)           # [[[1 2 3]]]
print(custom_array.ndim)      # 3

