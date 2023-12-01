# ---------------------------------------------
# -- Numpy => Compare Data Location And Type --
# ---------------------------------------------

import numpy as np

myList = [1,2,3,3,4,5]
arr = np.array(myList)

print(myList[0])
print(myList[1])
print(arr[0])
print(arr[1])

print('=' * 50)

print(id(myList[0]))
print(id(myList[1]))
print(id(arr[0]))
print(id(arr[1]))

# Notice that the location of the elements of the array are next to each other 
# unlike the elments of the list

print('=' * 50)

dataList = [1, 2, 'A', 'B', True]
dataArray = np.array([1, 2, 'A', 'B', True])

print(dataList)
print(dataArray)

# The array manipulated the data and turned them all to 'string'
