# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class programmig(metaclass = ABCMeta):

    @abstractmethod
    def hasOOP(self):

        pass

# the drived classes must follow the pattern of the base class:

class python(programmig):

    def hasOOP(self):

        return "yes"
    
class Pascal(programmig):

    def hasOOP(self):

        return "no"
    
one = python()
print(one.hasOOP())   # yes
two = Pascal()
print(two.hasOOP())   # no