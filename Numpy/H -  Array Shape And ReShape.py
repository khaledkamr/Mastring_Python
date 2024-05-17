# ------------------------------------
# -- Numpy => Array Shape & ReShape --
# ------------------------------------
# Shape Returns A Tuple Contains The Number Of Elements in Each Dimension
# ----------------------------------------------

import numpy as np

# Shape

arr1 = np.array([1,2,3,4])
print(arr1.shape)   # (4,)

print('=' * 50)

arr2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(arr2.shape)    # (3, 4)

print('=' * 50)

arr3 = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])
print(arr3.shape)    # (2, 2, 3)

print('=' * 50)

# Reshape

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr4.shape)   # (12,)

reshaped_arr4 = arr4.reshape(3, 4)
print(reshaped_arr4.shape)   # (3, 4)
print(reshaped_arr4)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
print('=' * 50)

arr5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(arr5.shape) # (2, 10)

# reshaped_arr5 = arr5.reshape(-1) # equivalent to ravel
# reshaped_arr5 = arr5.reshape(5, 4)
reshaped_arr5 = arr5.reshape(2, 5, 2) 
print(reshaped_arr5.shape)    # (2, 5, 2)
print(reshaped_arr5)
'''
[[[ 1  2]
  [ 3  4]
  [ 5  6]
  [ 7  8]
  [ 9 10]]

 [[ 1  2]
  [ 3  4]
  [ 5  6]
  [ 7  8]
  [ 9 10]]]
'''