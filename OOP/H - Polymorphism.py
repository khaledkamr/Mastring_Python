# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------
#when you have two functions with the same name but every function do a different task

class A:

    def do(self):

        print("from class A")

        raise NotImplementedError("derived class must implement this method")
        #this will make any derived class to implement this method and make the required changes

class B(A):
    
     def do(self):

        print("from class B")

class C(A):

    def do(self):

        print("from class C")

ins = A()
#ins.do()
ins = B()
ins.do()
ins = C()
ins.do()