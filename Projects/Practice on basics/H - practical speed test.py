# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time

def speedTest(func):
    def wrapper():
        start = time()

        func()

        end = time()
        print(f"function running time is : {end - start} seconds")
    return wrapper

@speedTest
def bigLoop():
    for n in range(1,20000):
        print(n)

bigLoop()