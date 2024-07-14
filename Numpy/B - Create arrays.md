# Numpy => Create Arrays
```python []
import numpy as np

mylist = [1,2,3,4]
myarray = np.array(mylist)

print(type(mylist))     
print(mylist)           
print(type(myarray))    
print(myarray)          
```
#### Output
```
<class 'list'>
[1, 2, 3, 4]
<class 'numpy.ndarray'>
[1 2 3 4]
```
## Accessing elements
```python []
print(mylist[0])    
print(myarray[0])   

a = np.array(10) 
b = np.array([10, 20]) 
c = np.array([[1,2], [3,4]]) 
d = np.array([[[5,6], [7,9]], [[1,3], [4,8]]]) 

print('=' * 50)

print(d[0])         
print(d[1])         
print(d[1][1])      
print(d[1][1][1])   
print(d[1, 1, 1])   
print(d[1, 1, -1])  
```
#### Output
```
1
1
Zero dimensional array
One dimensional array
two dimensional array 
three dimensional array
==================================================
[[5 6] [7 9]]
[[1 3] [4 8]]
[4 8]
8
8
8  (last element)
```
## Number of dimensions
```python []
print(a.ndim)      
print(b.ndim)      
print(c.ndim)      
print(d.ndim)      
```
#### Output
```
0
1
2
3
```
## Custom dimension
```python []
custom_array = np.array([1, 2, 3], ndmin=3)
print(custom_array)           
print(custom_array.ndim)      
```
#### Output
```
[[[1 2 3]]]
3
```