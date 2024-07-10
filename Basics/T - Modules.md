# Modules => Built In Modules 
- Module is A File Contain A Set Of Functions
- You Can Import Module in Your App To Help You
- You Can Import Multiple Modules
- You Can Create Your Own Modules
- Modules Saves Your Time

## Import Main Module
```python []
import random
print(random)
print(f"Print Random Float Number {random.random()}")
```
#### Output
```
Print Random Float Number 0.7472153052565654
```
### you can see all the functions inside any module 
```python []
print(dir(random)) 
```
#### Output
```
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```
## Import One Or Two Functions From Module
```python []
from random import randint, random
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")
```
#### Output
```
Print Random Float 0.9898184658090134
Print Random Integer 304
```
## Modules => Create Your Module 
```python []
import sys
sys.path.append(r"D:\Games")
print(sys.path)

import myModule
print(dir(myModule))

myModule.sayHello("Ahmed")
myModule.sayHello("yossif")
myModule.sayHello("ali")

myModule.sayHowAreYou("Ahmed")
myModule.sayHowAreYou("yossif")
myModule.sayHowAreYou("ali")
```

## Alias
```python []
import myModule as mm

mm.sayHello("Ahmed")
mm.sayHello("yossif")
mm.sayHello("ali")

mm.sayHowAreYou("Ahmed")
mm.sayHowAreYou("yossif")
mm.sayHowAreYou("ali")

from myModule import sayHello

sayHello("Osama")

from myModule import sayHello as ss

ss("Osama")
```