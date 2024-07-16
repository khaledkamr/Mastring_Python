# Multiple Inheritance 
```python []
class base1:
    def __init__(self):
        print("base1")

    def fun1(self):
        print("one")

class base2:
    def __init__(self):
        print("base2")

    def fun2(self):
        print("two")

class derived(base1, base2):
    pass

var = derived()      
var.fun1()           
var.fun2()           
```
#### Output
```
base1
one
two
```






