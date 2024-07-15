# Numpy => Arithmetic & Useful Operations 
- Addition
- Subtraction
- Multiplication
- Dividation
 ----------------
- min
- max
- sum
- ravel => Returns Flattened Array 1 Dimension With Same Type
----------------------------------------------
```python []
import numpy as np
```
# Arithmetic Operations
## Ex1:
```python []
arr1 = np.array([10, 20 ,30])
arr2 = np.array([5, 2, 4])

print(arr1 + arr2)     
print(arr1 - arr2)     
print(arr1 * arr2)     
print(arr1 / arr2)     

```
#### Output
```
[15 22 34]
[ 5 18 26]
[ 50  40 120]
[ 2.  10.   7.5]
```
## Ex2:
```python []
arr3 = np.array([[1,4], [5,9]])
arr4 = np.array([[2,7], [10,5]])

print(arr3 + arr4, end='\n\n') 
print(arr3 - arr4, end='\n\n') 
print(arr3 * arr4, end='\n\n')
print(arr3 / arr4) 
```
#### Output
```
[[ 3 11]
 [15 14]]

[[-1 -3]
 [-5  4]]

[[ 2 28]
 [50 45]]

[[0.5        0.57142857]
 [0.5        1.8       ]]
```
# Min, Max, Sum
## Ex1:
```python []
arr5 = np.array([10, 20, 30])
print(arr5.min())      
print(arr5.max())      
print(arr5.sum())      
```
#### Output
```
10
30
60
```
## Ex2:
```python []
arr6 = np.array([[6, 4], [3, 9]])
print(arr6.min())     
print(arr6.max())     
print(arr6.sum())     
```
#### Output
```
3
9
22
```

# Ravel
```python []
arr7 = np.array([[6, 4], [3, 9]])
print(arr7.ravel())    

arr8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr8.ndim)    
print(arr8.ravel())    
print(arr8.ravel().ndim)   
```
#### Output
```
[6 4 3 9]
3
[1 2 3 4 5 6 7 8]
1
```