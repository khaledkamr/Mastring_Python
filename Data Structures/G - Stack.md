# Stack

A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.

![Stack in python](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230726165552/Stack-Data-Structure.png)

### The functions associated with stack are:

- empty() – Returns whether the stack is empty – Time Complexity: O(1)
- size() – Returns the size of the stack – Time Complexity: O(1)
- top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
- push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
- pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

## Python Stack Implementation
### Stack in Python can be implemented using the following ways:

- list
- Collections.deque
- queue.LifoQueue

## Implementation using List

Python’s built-in data structure list can be used as a stack. Instead of push(), append() is used to add elements to the top of the stack while pop() removes the element in LIFO order. 

```python 
stack = []
 
# append() function to push element in the stack
stack.append('g')
stack.append('f')
stack.append('g')
 
print('Initial stack')
print(stack)
 
# pop() function to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 
print(stack.pop())
# this will cause an IndexError as the stack is now empty
```
#### Output
```
Initial stack
['g', 'f', 'g']

Elements popped from stack:
g
f
g

Stack after elements are popped:
[]
Traceback (most recent call last):
  File "d:\coding\VS code\compile.py", line 20, in <module>
    print(stack.pop())
          ^^^^^^^^^^^
IndexError: pop from empty list
```
## Implementation using collections.deque:

Python stack can be implemented using the deque class from the collections module. Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 

```python 
from collections import deque
 
stack = deque()
 
# append() function to push element in the stack
stack.append('g')
stack.append('f')
stack.append('g')
 
print('Initial stack:')
print(stack)
 
# pop() function to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 
print(stack.pop())
# this will cause an IndexError as the stack is now empty
```
#### Output
```
Initial stack:
deque(['g', 'f', 'g'])

Elements popped from stack:
g
f
g

Stack after elements are popped:
deque([])
Traceback (most recent call last):
  File "d:\coding\VS code\compile.py", line 22, in <module>
    print(stack.pop())
          ^^^^^^^^^^^
IndexError: pop from an empty deque
```
## Implementation using queue module

The queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 

```python 
from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize = 3)
 
# qsize() show the number of elements in the stack
print(stack.qsize())
 
# put() function to push element in the stack
stack.put('g')
stack.put('f')
stack.put('g')
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() function to pop element from stack in LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())
```
### Output
```
0
Full:  True
Size:  3

Elements popped from the stack
g
f
g

Empty:  True
```