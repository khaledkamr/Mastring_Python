# Deque in Python
Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.

![deque](https://media.geeksforgeeks.org/wp-content/uploads/anod.png)

## Types of Restricted Deque Input
- Input Restricted Deque:  Input is limited at one end while deletion is permitted at both ends.
- Output Restricted Deque: output is limited at one end but insertion is permitted at both ends.
Example: Python code to demonstrate deque 
```python 
from collections import deque 
    
# Declaring deque 
queue = deque(['name','age','DOB'])  
    
print(queue)
```
#### Output
```
deque(['name', 'age', 'DOB'])
```

## Operations on deque 
### Example 1: Appending Items Efficiently
- append():- This function is used to insert the value in its argument to the right end of the deque.
- appendleft():- This function is used to insert the value in its argument to the left end of the deque.
```python
from collections import deque

de = deque([1, 2, 3])
print("deque: ", de)

# inserts 4 at the end of deque
de.append(4)

print("\nThe deque after appending at right is : ")
print(de)

# inserts 6 at the beginning of deque
de.appendleft(6)

print("\nThe deque after appending at left is : ")
print(de)
```
#### Output
```
deque:  deque([1, 2, 3])

The deque after appending at right is : 
deque([1, 2, 3, 4])

The deque after appending at left is : 
deque([6, 1, 2, 3, 4])
```

### Example 2: Popping Items Efficiently
- pop():- This function is used to delete an argument from the right end of the deque.
- popleft():- This function is used to delete an argument from the left end of the deque.
```python
from collections import deque

de = collections.deque([6, 1, 2, 3, 4])
print("deque: ", de)

# deletes 4 from the right end of deque
de.pop()

print("\nThe deque after deleting from right is : ")
print(de)

# deletes 6 from the left end of deque
de.popleft()

print("\nThe deque after deleting from left is : ")
print(de)
```
#### Output
```
deque:  deque([6, 1, 2, 3, 4])

The deque after deleting from right is : 
deque([6, 1, 2, 3])

The deque after deleting from left is : 
deque([1, 2, 3])
```
### Example 3: Accessing Items in a deque
- index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
- insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
- remove():- This function removes the first occurrence of the value mentioned in arguments.
- count():- This function counts the number of occurrences of value mentioned in arguments.
```python 
# insert(), index(), remove(), count()

from collections import deque

de = deque([1, 2, 3, 3, 4, 2, 4])

print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5))

de.insert(4,3)

print ("The deque after inserting 3 at 5th position is : ")
print (de)

print ("The count of 3 in deque is : ")
print (de.count(3))

de.remove(3)

print ("The deque after deleting first occurrence of 3 is : ")
print (de)
```
#### Output
```
The number 4 first occurs at a position : 
4
The deque after inserting 3 at 5th position is : 
deque([1, 2, 3, 3, 3, 4, 2, 4])
The count of 3 in deque is : 
3
The deque after deleting first occurrence of 3 is : 
deque([1, 2, 3, 3, 4, 2, 4])
```

### Example 5: Front and Back of a deque
- Deque[0] :- We can access the front element of the deque using indexing with de[0].
- Deque[-1] :- We can access the back element of the deque using indexing with de[-1].
```python 
from collections import deque

de = deque([1, 2, 3, 4, 5, 6])
print("Current Deque: ", de)

print("Front element of the deque:", de[0])

print("Back element of the deque:", de[-1])
```
#### Output
```
Current Deque:  deque([1, 2, 3, 4, 5, 6])
Front element of the deque: 1
Back element of the deque: 6
```

### Example 6: Different operations on deque
- extend(iterable):- This function is used to add multiple values at the right end of the deque. The argument passed is iterable.
- extendleft(iterable):- This function is used to add multiple values at the left end of the deque. The argument passed is iterable. Order is reversed as a result of left appends.
- reverse():- This function is used to reverse the order of deque elements.
- rotate():- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to the left. Else rotation is to right.
```python 
# extend(), extendleft(), rotate(), reverse()

from collections import deque

de = collections.deque([1, 2, 3,])

de.extend([4,5,6])

print ("The deque after extending deque at end is : ")
print (de)

de.extendleft([7,8,9])

print ("The deque after extending deque at beginning is : ")
print (de)

de.rotate(-3)

print ("The deque after rotating deque is : ")
print (de)

de.reverse()

print ("The deque after reversing deque is : ")
print (de)
```
#### Output
```
The deque after extending deque at end is : 
deque([1, 2, 3, 4, 5, 6])
The deque after extending deque at beginning is : 
deque([9, 8, 7, 1, 2, 3, 4, 5, 6])
The deque after rotating deque is : 
deque([1, 2, 3, 4, 5, 6, 9, 8, 7])
The deque after reversing deque is : 
deque([7, 8, 9, 6, 5, 4, 3, 2, 1])
```

## Complexity Analysis:

| Methods            | Time Complexity | Auxiliary Space |
---------------------|-----------------|------------------
append()             | O(1)            | O(1)
appendleft()         | O(1)            | O(1)
pop()                | O(1)            | O(1)
popleft()            | O(1)            | O(1)
index(ele, beg, end) | O(N)            | O(1)
insert(i, a)         | O(N)            | O(1)
remove()             | O(N)            | O(1)
count()              | O(N)            | O(1)
len(dequeue)         | O(1)            | O(1)
Deque[0]             | O(1)            | O(1)
Deque[-1]            | O(1)            | O(1)
extend(iterable)     | O(K)            | O(1)
extendleft(iterable) | O(K)            | O(1)
reverse()            | O(N)            | O(1)
rotate()             | O(K)            | O(1)

 
## Deque in Python – FAQs
### Why use deque instead of list in Python?
```
deque (double-ended queue) in Python, from the collections module, provides optimized operations for appending and popping elements from both ends of the sequence. Compared to list, which provides constant time complexity for append operations (amortized O(1)), deque offers consistent O(1) time complexity for append and pop operations from both ends. This makes deque suitable for scenarios where efficient appends and pops are required from both ends of the sequence, such as implementing queues and stacks.
```
### Is deque better than queue in Python?
```
In Python, queue is a module that provides different types of queues like Queue, LifoQueue, and PriorityQueue, built on top of deque or list. deque itself is not better or worse than queue, but rather serves as a fundamental component that can be used to implement efficient queues (Queue), stacks (LifoQueue), and double-ended queues (deque).
```
### Why is deque faster than queue?
```
deque itself is not faster than queue because deque is often used as the underlying data structure to implement queues (Queue), stacks (LifoQueue), and double-ended queues (deque) in Python. The efficiency of operations (such as append and pop) depends on the specific implementation and usage context rather than deque being inherently faster than queue.
```
### Why is deque faster than stack?
```
deque is not necessarily faster than a stack (LifoQueue) because both can be implemented using deque as the underlying data structure. However, if comparing deque to a straightforward list-based stack implementation (list used as a stack), deque may offer faster performance for pop and append operations due to its optimized internals for these operations.
```
### What are the two types of deque?
```
In Python’s collections module, there are two primary types of deque:

- deque: A general-purpose double-ended queue.
- deque(maxlen=N): A bounded deque that restricts the maximum number of elements (N) it can hold. When new items are added and the deque is full, the oldest items are automatically removed to accommodate the new items.
```
### What is the difference between a simple queue and deque?
```
A simple queue, such as those implemented using queue.Queue in Python, typically refers to a FIFO (First-In-First-Out) data structure where elements are inserted at the rear and removed from the front. deque, on the other hand, supports efficient insertion and deletion operations from both ends (front and rear) of the queue. It can function as a double-ended queue (collections.deque) or as a general-purpose data structure that can mimic a FIFO queue (queue.Queue) or LIFO stack (queue.LifoQueue) depending on how it’s used.
```