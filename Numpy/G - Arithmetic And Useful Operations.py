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

print(arr1 + arr2) # result [15, 22, 34]
print(arr1 - arr2) # result [5, 18, 26]
print(arr1 * arr2) # result [50, 40, 120]
print(arr1 / arr2) # result [2, 10, 7.5]

print('=' * 50)

arr3 = np.array([[1,4], [5,9]])
arr4 = np.array([[2,7], [10,5]])

print(arr3 + arr4) # result [[3, 11], [15, 14]]
print(arr3 - arr4) # result [[-1, -3], [-5, 4]]
print(arr3 * arr4) # result [[2, 28], [50, 45]]
print(arr3 / arr4) # result [[0.5, 0.571], [0.5, 1.8]]

print('=' * 50)

# Min, Max, Sum

arr5 = np.array([10, 20, 30])
print(arr5.min())
print(arr5.max())
print(arr5.sum())

print('=' * 50)

arr6 = np.array([[6, 4], [3, 9]])
print(arr6.min())
print(arr6.max())
print(arr6.sum())

print('=' * 50)

# Ravel

arr7 = np.array([[6, 4], [3, 9]])
print(arr7.ravel())

arr8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr8.ndim)
print(arr8.ravel())
print(arr8.ravel().ndim)
