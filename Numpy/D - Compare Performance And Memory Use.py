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
print(f"list time = {time.time() - list_start}")    # list time = 17.051422357559204

arr_start = time.time()
arr_result = arr1 + arr2
print(f"array time = {time.time() - arr_start}")    # array time = 21.044347763061523

print('=' * 50)

myArray = np.arange(100)

print(myArray)

'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99]
'''

print(myArray.itemsize)      # 4
print(myArray.size)       # 100
print(f"All bytes = {myArray.itemsize * myArray.size}")    # All bytes = 400

print('=' * 50)

myList = range(100)
print(sys.getsizeof(1))      # 28
print(len(myList))      # 100
print(f"All bytes = {sys.getsizeof(1) * len(myList)}")    # All bytes = 2800