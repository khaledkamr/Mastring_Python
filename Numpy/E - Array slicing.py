# ----------------------------
# -- Numpy => Array Slicing --
# ----------------------------

import numpy as np

# Slicing => [Start:End:Steps] Not Including End

a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim)    # 1
print(a[1])      # B
print(a[1:4])    # ['B' 'C' 'D']
print(a[:4])     # ['A' 'B' 'C' 'D']
print(a[2:])     # ['C' 'D' 'E' 'F']

print("#" * 50)

b = np.array([["A", "B", "X"], 
              ["C", "D", "Y"], 
              ["E", "F", "Z"], 
              ["M", "N", "O"]])

print(b.ndim)    # 2
print(b[1])      # ['C' 'D' 'Y']
print(b[2:][:2])
'''
[['E' 'F' 'Z']
 ['M' 'N' 'O']]
'''
print(b[2:, :2])
'''
[['E' 'F']
 ['M' 'N']]
'''
print(b[2:, :2:2]) # two steps
'''
[['E']
 ['M']]
'''