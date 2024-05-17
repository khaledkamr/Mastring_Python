# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

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


#food1 = Food("pizza")
food2 = apple("pizza")    # pizza is created from derived class
food2.eat()    # eat method from base class
print("=" * 50)

# when you add a constructor to the dreiven class, you over write on the constructor of thebase class
# how you can fix that:

class Food: # base class

    def __init__(self, name, price):

        self.name = name
        self.price = price

        print(f"{self.name} is created from main class")

    def eat(self):

        print("eat method from base class")


class apple(Food): # derived class

    def __init__(self, name, price, amount):

        Food.__init__(self, name, price) #create instance from base class

        # or you can use super() so you don't have yo write the class name and the self param:

        #super().__init__(name, price)

        self.amount = amount

        print(f"{self.name} is created from derived class")
        print(f"Price is {self.price}")
        print(f"Amount is {self.amount}")


#food1 = Food("pizza")
food2 = apple("pizza", 150, 500)  # pizza is created from main class
food2.eat() 
'''
pizza is created from derived class
Price is 150
Amount is 500
eat method from base class
'''

