# Numpy => Data Types And Control Array 
### https://numpy.org/devdocs/user/basics.types.html
### https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types
-------------------------------------------
- '?' boolean
- 'b' (signed) byte
- 'B' unsigned byte
- 'i' (signed) integer
- 'u' unsigned integer
- 'f' floating-point
- 'c' complex-floating point
- 'm' timedelta
- 'M' datetime
- 'O' (Python) objects
- 'S', 'a' zero-terminated bytes (not recommended)
- 'U' Unicode string
- 'V' raw data (void)
 ------------------------------------------------
 <br>

```python []
import numpy as np
```
## show array data type
```python []
my_array1 = np.array([1, 2, 3])
my_array2 = np.array([1.5, 20.15, 3.601])
my_array3 = np.array(["khaled_kamr", "B", "Ahmed"])

print(my_array1.dtype)   
print(my_array2.dtype)   
print(my_array3.dtype)   
```
#### Output
```
int32
float64
<U11
```

## Create Array With Specific Data Type
```python []
my_array4 = np.array([1, 2, 3], dtype=float) # float Or 'float' Or 'f'
my_array5 = np.array([1.5, 20.15, 3.601], dtype=int) # int Or 'int' Or 'i'
# my_array6 = np.array(["khaled_kamr", "B", "Ahmed"], dtype=int) # value error

print(my_array4.dtype) 
print(my_array5.dtype) 
print(my_array6.dtype) 
```
#### Output
```
float64
int32
NameError: name 'my_array6' is not defined. Did you mean: 'my_array1'?
```

## Change Data Type Of Existing Array
```python []
my_array7 = np.array([1,2,3,4,5,6,7])
print(my_array7.dtype)   
print(my_array7)         

my_array7 = my_array7.astype(float)
print(my_array7.dtype)     
print(my_array7)           
```
#### Output
```
int32
[1 2 3 4 5 6 7]
float64
[1. 2. 3. 4. 5. 6. 7.]
```
## Test Capacity
```python []
my_array8 = np.array([100,200,300,400], dtype='f')
print(my_array8.dtype)         
print(my_array8[0].itemsize)   

my_array8 = np.array([100,200,300,400], dtype=float)
print(my_array8.dtype)         
print(my_array8[0].itemsize)   
```
#### Output
```
float32
4
float64
8
```