# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import random
print(random)
print(f"Print Random Float Number {random.random()}")


print(dir(random)) # Show All Functions Inside Module

# Import One Or Two Functions From Module
from random import randint, random
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")


# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

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

# Alias

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