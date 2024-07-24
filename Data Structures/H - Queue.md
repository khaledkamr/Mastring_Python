# Queue
As a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed first. A good example of the queue is any queue of consumers for a resource where the consumer that came first is served first.

![Queue](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230726165642/Queue-Data-structure1.png)

### Operations associated with queue are:

- Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity: O(1)
- Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity: O(1)
- Front: Get the front item from queue – Time Complexity: O(1)
- Rear: Get the last item from queue – Time Complexity: O(1)

## Python queue Implementation

### Queue in Python can be implemented in the following ways:

- list
- collections.deque
- queue.Queue

## Implementation using list

Instead of enqueue() and dequeue(), append() and pop() function is used.

```python
queue = []
 
# Adding elements to the queue
queue.append('g')
queue.append('f')
queue.append('g')
 
print("Initial queue")
print(queue)
 
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
 
print("\nQueue after removing elements")
print(queue)
 
print(queue.pop(0))
# this will raise and IndexError as the queue is now empty
```
#### Output
```
Initial queue
['g', 'f', 'g']

Elements dequeued from queue
g
f
g

Queue after removing elements
[]
Traceback (most recent call last):
  File "d:\coding\VS code\compile.py", line 20, in <module>
    print(queue.pop(0))
          ^^^^^^^^^^^^
IndexError: pop from empty list
```
## Implementation using collections.deque

Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

```python
from collections import deque
 
# Initializing a queue
q = deque()
 
# Adding elements to a queue
q.append('g')
q.append('f')
q.append('g')
 
print("Initial queue")
print(q)
 
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)
 
q.popleft()
# will raise an IndexError as queue is now empty
```
#### Output
```
Initial queue
deque(['g', 'f', 'g'])

Elements dequeued from the queue
g
f
g

Queue after removing elements
deque([])
Traceback (most recent call last):
  File "d:\coding\VS code\compile.py", line 23, in <module>
    q.popleft()
IndexError: pop from an empty deque
```
## Implementation using the queue.Queue

queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means an infinite queue. This Queue follows the FIFO rule. 

```python
from queue import Queue
 
q = Queue(maxsize = 3)
 
# qsize() give the maxsize of the Queue
print(q.qsize())
 
# Adding of element to queue
q.put('g')
q.put('f')
q.put('g')
 
# Return Boolean for Full Queue
print("\nFull: ", q.full())
 
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
 
# Return Boolean for Empty Queue
print("\nEmpty: ", q.empty())
 
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
 
# This would result into Infinite Loop as the Queue is empty.
# print(q.get())
```
#### Output
```
0

Full:  True

Elements dequeued from the queue
g
f
g

Empty:  True

Empty:  False
Full:  False
```
