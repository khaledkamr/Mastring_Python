# -------------------------------------------------
# -- Numpy => Compare Performance And Memory Use --
# -------------------------------------------------
# - Performance
# - Memory Use
# -------------------------------------------------

import numpy as np
import time
import sys

elements = 100000000

myList1 = range(elements)
myList2 = range(elements)

arr1 = np.arange(elements)
arr2 = np.arange(elements)

list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(myList1,myList2)]
print(f"list time = {time.time() - list_start}") # 6.25

arr_start = time.time()
arr_result = arr1 + arr2
print(f"array time = {time.time() - arr_start}") # 0.14

print('=' * 50)

myArray = np.arange(100)

print(myArray)
print(myArray.itemsize) # the size of teh elements by bytes
print(myArray.size) # the number of the elements
print(f"All bytes = {myArray.itemsize * myArray.size}") # 400

print('=' * 50)

myList = range(100)
print(sys.getsizeof(1))
print(len(myList))
print(f"All bytes = {sys.getsizeof(1) * len(myList)}") # 2800