# Numpy => Array Slicing 

### Slicing => [Start:End:Steps] Not Including End

## Ex1:
```python []
import numpy as np

a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim)   
print(a[1])     
print(a[1:4])   
print(a[:4])    
print(a[2:])    
```
#### Output
```
1
B
['B' 'C' 'D']
['A' 'B' 'C' 'D']
['C' 'D' 'E' 'F']
```
## Ex2:
```python []
b = np.array([["A", "B", "X"], 
              ["C", "D", "Y"], 
              ["E", "F", "Z"], 
              ["M", "N", "O"]])

print(b.ndim)   
print(b[1])     
print(b[2:][:2])

print(b[2:, :2])

print(b[2:, :2:2]) # two steps
```
#### Output
```
2

['C' 'D' 'Y']

[['E' 'F' 'Z']
 ['M' 'N' 'O']]

[['E' 'F']
 ['M' 'N']]

[['E']
 ['M']]
```