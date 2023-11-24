# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------

import timeit
import random

name = "khaled"
print(name * 1000)
print(timeit.timeit("name = 'khaled'; name * 1000"))

print(random.randint(0, 50))
print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

# 'repeat' meams it will repeat the whole excution 4 times and output the minimal time in the 4 times
print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))