# ---------------------------------------------
# -- Numpy => Arithmetic & Useful Operations --
# ---------------------------------------------
# - Addition
# - Subtraction
# - Multiplication
# - Dividation
# ----------------
# - min
# - max
# - sum
# - ravel => Returns Flattened Array 1 Dimension With Same Type
# ----------------------------------------------

import numpy as np

# Arithmetic Operations

arr1 = np.array([10, 20 ,30])
arr2 = np.array([5, 2, 4])

print(arr1 + arr2)     # [15 22 34]
print(arr1 - arr2)     # [ 5 18 26]
print(arr1 * arr2)     # [ 50  40 120]
print(arr1 / arr2)     # [ 2.  10.   7.5]

print('=' * 50)

arr3 = np.array([[1,4], [5,9]])
arr4 = np.array([[2,7], [10,5]])

print(arr3 + arr4) 
'''
[[ 3 11]
 [15 14]]
'''
print(arr3 - arr4) 
'''
[[-1 -3]
 [-5  4]]
'''
print(arr3 * arr4) 
'''
[[ 2 28]
 [50 45]]
'''
print(arr3 / arr4) 
'''
[[0.5        0.57142857]
 [0.5        1.8       ]]
'''
print('=' * 50)

# Min, Max, Sum

arr5 = np.array([10, 20, 30])
print(arr5.min())      # 10
print(arr5.max())      # 30
print(arr5.sum())      # 60

print('=' * 50)

arr6 = np.array([[6, 4], [3, 9]])
print(arr6.min())      # 3
print(arr6.max())      # 9
print(arr6.sum())      # 22

print('=' * 50)

# Ravel

arr7 = np.array([[6, 4], [3, 9]])
print(arr7.ravel())    # [6 4 3 9]

arr8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr8.ndim)    # 3
print(arr8.ravel())    # [1 2 3 4 5 6 7 8]
print(arr8.ravel().ndim)    # 1
