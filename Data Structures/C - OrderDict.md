# OrderDict
An `OrderedDict` is a dictionary subclass that remembers the order in which keys were first inserted. The only difference between `dict()` and OrderedDict() lies in their handling of key order in Python.

## OrderedDict vs dict in Python
`OrderedDict` maintains the sequence in which keys are added, ensuring that the order is preserved during iteration. In contrast, a standard dictionary does not guarantee any specific order when iterated, providing values in an arbitrary sequence. `OrderedDict` distinguishes itself by retaining the original insertion order of items.

Example: In this example, the below code demonstrates the difference between a regular dictionary (`dict`) and an ordered dictionary (`OrderedDict`). It first prints the items in a regular dictionary (`d`) where the order of insertion is not guaranteed.
```python []

# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)
```    
#### Output: 
```
This is a Dict:
a 1 
b 2
c 3
d 4
This is an Ordered Dict:
a 1
b 2
c 3
d 4
```
## Python Dictionary Ordered
There are various important points related to python dictionary ordereing here , we are discussing some important points related to Python dictionary ordereing those are following.

- Key value Change
- Deletion and Re-Inserting
- Equality Comparison
- OrderedDict Reversal
- OrderedDict Popitem Last
- Key Insertion at Arbitrary Position
- Collections Module
### Key value Change in Python Dictionary Order
If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict. this Python method demonstrates changing the value associated with a key in an OrderedDict.

Example : In this example the below Python code uses an OrderedDict to demonstrate changing the value associated with a specific key. Initially, it creates an OrderedDict with keys ‘a’ through ‘d’ and respective values 1 through 4.

```python []
# A Python program to demonstrate working of key
# value change in OrderedDict
from collections import OrderedDict

print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)

print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
    print(key, value)
```    
#### Output: 
```
Before:
a 1
b 2
c 3
d 4
After:
a 1
b 2
c 5
d 4
```
## Equality Comparison in Python Dictionary Order
OrderedDicts in Python can be compared for equality not only based on their content but also considering the order of insertion. This is useful when comparing two OrderedDicts for both key-value pairs and their order.

Example : In this example the code creates two OrderedDicts, `od1` and `od2`, with different orderings of key-value pairs. It then demonstrates that the order of insertion is considered when comparing them for equality using the `==` operator, resulting in `False`.

```python []
from collections import OrderedDict

# Create two ordered dictionaries with different orderings
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# Compare the ordered dictionaries for equality
print(od1 == od2)  
```
#### Output :
```
False
```
## OrderedDict Reversal in Python Dictionary Order
After initializing an `OrderedDict` named `my_dict` with specific key-value pairs, the code attempts to reverse the order of these pairs using the reverse() method. However, `OrderedDict` does not natively support a `reverse()` method. To reverse the order, the code correctly employs Python’s reversed() function combined with list() and items() to obtain a reversed list of key-value pairs. This reversed list is then used to construct a new `OrderedDict` named `reversed_dict`, demonstrating the ability to reverse the order of elements in an `OrderedDict` while preserving the original key-value associations

Example : In this example the below code Creates an OrderedDict named my_dict with elements in a specific order and uses reversed() along with list() and items() to reverse the list of key-value pairs from my_dict. Then, OrderedDict() reconstructs the dictionary in reversed order and prints each key-value pair in reversed order.

```python []
from collections import OrderedDict

my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Reverse the OrderedDict using reversed()
reversed_dict = OrderedDict(reversed(list(my_dict.items())))

# Print the reversed dictionary
for key, value in reversed_dict.items():
    print(key, value)
```  
#### Output :
```
c 3 
b 2
a 1
```
### OrderedDict Popitem() in Python Dictionary Order
The popitem() method in OrderedDict can be used with the last parameter to remove and return the last inserted key-value pair. This is useful when you want to process items in a last-in, first-out manner. Using `popitem(last=True)` on an OrderedDict would remove and return the most recently added item, providing flexibility in managing the order of elements.

Example : In this example the below code uses an OrderedDict and applies the `popitem` method with `last=True` to remove and store the last inserted key-value pair. It then prints the removed item, resulting in the output: `(‘c’, 3)`.

```python []
from collections import OrderedDict

my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
last_item = my_dict.popitem(last=True)

print(last_item)
```  
#### Output :
```
('c', 3)
```
## Key Insertion at Arbitrary Position in Python Dictionary Ordered
OrderedDict allows inserting a new key at a specific position using the move_to_end and move_to_start methods. This flexibility allows dynamic reordering of keys based on usage or priority.

Example : In this example the below Python code uses an OrderedDict to create a dictionary with ordered key-value pairs. It then employs the `move_to_end` method to reposition key ‘a’ to the end and key ‘b’ to the beginning.

```python []
from collections import OrderedDict

my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move key 'a' to the end
my_dict.move_to_end('a')

# Move key 'b' to the beginning
my_dict.move_to_end('b', last=False)

for key, value in my_dict.items():
    print(key, value)
```
#### Output :
```
b 2, c 3, a 1
```
## Deletion and Re-Inserting in Python Dictionary Ordered
Deleting and re-inserting the same key will push it to the back as OrderedDict, however, maintains the order of insertion. This method showcases deletion and re-insertion operations in a Python OrderedDict. Initially, it populates the OrderedDict with key-value pairs, deletes an entry, prints the updated OrderedDict, and subsequently re-inserts the deleted entry, demonstrating the ordered nature of the dictionary.

Example :In this example the below python code demonstrates deletion, re-insertion, and printing of items in an OrderedDict. It first prints the OrderedDict items, then deletes the entry with key ‘c’, prints the updated OrderedDict, and finally re-inserts ‘c’ with its value, printing the OrderedDict again.

```python []
# A Python program to demonstrate working of deletion
# re-insertion in OrderedDict
from collections import OrderedDict

print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)
```

#### Output: 
```
Before deleting:
a 1
b 2
c 3
d 4
After deleting:
a 1
b 2
d 4
After re-inserting:
a 1
b 2
d 4
c 3
```
## Collections Module in Python Dictionary Order
OrderedDict is part of the collections module in Python. It provides all the methods and functionality of a regular dictionary, as well as some additional methods that take advantage of the ordering of the items. Here are some examples of using OrderedDict in Python:

Example :In this example the below code uses an OrderedDict to create a dictionary with ordered key-value pairs. It adds a new item ‘d’ to the end and inserts items ‘e’ and ‘f’ at the beginning, with ‘e’ being moved to the front. The final loop prints the dictionary items in the order they were added.

```python []
from collections import OrderedDict

# Create an ordered dictionary of key-value pairs
my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Add a new item to the end of the dictionary
my_dict['d'] = 4

# Add a new item at a specific position in the dictionary
# my_dict.update({'e': 5, 'f': 6}) or below
my_dict.update([('e', 5), ('f', 6)])
my_dict.move_to_end('e', last=False)

# Iterate over the dictionary in the order in which items were added
for key, value in my_dict.items():
    print(key, value)
```
#### Output:
```
e 5
a 1
b 2
c 3
d 4
f 6
```
### Time Complexity:

- Get item(Key): O(1)
- Set item(key, value): O(1)
- Delete item(key): O(n)
- Iteration: O(n)
### Space Complexity: O(n)

OrderedDict is a dictionary subclass in Python that remembers the order in which items were added. In a regular Python dictionary, the order of the items is not guaranteed, and it may change between different runs of the program or different versions of Python. However, an OrderedDict preserves the order of the items as they were added, even if new items are later added or existing items are changed.

### Other Considerations
- Ordered dict in Python version 2.7 consumes more memory than normal dict. This is due to the underlying Doubly Linked List implementation for keeping the order. In Python 2.7 Ordered Dict is not dict subclass, it’s a specialized container from collections module.
- Starting from Python 3.7, insertion order of Python dictionaries is guaranteed.
- Ordered Dict can be used as a stack with the help of popitem function. Try implementing LRU cache with Ordered Dict.
