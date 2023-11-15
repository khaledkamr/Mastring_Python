# -----------------------------------------------------
# -- Object Oriented Programming => Getters & Setters--
# -----------------------------------------------------
# Assuming that incapsulation does really restrict the attributes
# you can't get to the Private and Protected attributes
# so here we can use the Getter and the Setter to help us in this
 
class member:

    def __init__(self, name):

        self.__name = name #Private

    def hello(self):

        return f"Hello, {self.name}"
    
    def getName(self): #Getter

        return self.__name
    
    def setName(self, newName): #Setter

        self.__name = newName
    
one = member("Khaled")

one.setName("yossif")
print(one.getName())
