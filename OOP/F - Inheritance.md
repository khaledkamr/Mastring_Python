# Inheritance 
```python []
class Food: # base class
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is created from main class")

    def eat(self):
        print("eat method from base class")


class apple(Food): # derived class
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is created from derived class")

food1 = Food("pizza")
food2 = apple("pizza")     
food2.eat()    
```
#### Output
```
pizza is created from main class
pizza is created from derived class
eat method from base class
```
### when you add a constructor to the driven class, you over write on the constructor of the base class
### how you can fix that:
```python []
class Food: # base class
  def __init__(self, name, price):
    self.name = name
    self.price = price
    print(f"{self.name} is created from main class")

  def eat(self):
    print("eat method from base class")

class apple(Food): # derived class
  def __init__(self, name, price, amount):
    # create instance from base class
    Food.__init__(self, name, price) 
    
    # or you can use super() so you don't have yo write the class name and the self param:
    # super().__init__(name, price)

    self.amount = amount
    print(f"{self.name} is created from derived class")
    print(f"Price is {self.price}")
    print(f"Amount is {self.amount}")

food2 = apple("pizza", 150, 500)
food2.eat() 
```
#### Output
```
pizza is created from main class
pizza is created from derived class
Price is 150
Amount is 500
eat method from base class
```