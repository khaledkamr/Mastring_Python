# -- Numpy => Array Shape & ReShape --
 Shape Returns A Tuple Contains The Number Of Elements in Each Dimension
 ----------------------------------------------
```python []
import numpy as np
```
# Shape
## Ex1:
```python []
arr1 = np.array([1,2,3,4])
print(arr1.shape)   
```
#### Output
```
(4,)
```
## Ex2:
```python []
arr2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(arr2.shape)   
```
#### Output
```
(3, 4)
```
## Ex3:

```python []
arr3 = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])
print(arr3.shape)    
```
#### Output
```
(2, 2, 3)
```

# Reshape
## Ex1:
```python []
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr4.shape)   

reshaped_arr4 = arr4.reshape(3, 4)
print(reshaped_arr4.shape) 
print(reshaped_arr4)

```
#### Output
```
(12,)
(3, 4)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```
## Ex2:
```python []
arr5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(arr5.shape) 
```
#### Output
```
(2, 10)
```
## Ex3:
```python []
# reshaped_arr5 = arr5.reshape(-1) # equivalent to ravel
# reshaped_arr5 = arr5.reshape(5, 4)
reshaped_arr5 = arr5.reshape(2, 5, 2) 
print(reshaped_arr5.shape)   
print(reshaped_arr5)
```
#### Output
```
(2, 5, 2)
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
```