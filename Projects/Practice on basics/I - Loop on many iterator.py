# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ----------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C']
tuple1 = ("man", "woman", "girl", "boy")
dict1 = {"name" : "khaled", "age" : 36, "country" : "egypt"}


for i1, i2, i3, i4 in zip(list1, list2, tuple1, dict1):
    print("list 1 item => ", i1)
    print("list 2 item => ", i2)
    print("tuple 3 item => ", i3)
    print("Dict 1 key => ", i4, "value => ", dict1[i4])

