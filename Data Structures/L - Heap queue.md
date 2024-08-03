# Heap queue (or heapq)
heapq module in Python provides the heap data structure that is mainly used to represent a priority queue. The property of this data structure in Python is that each time the smallest heap element is popped(min-heap). Whenever elements are pushed or popped, heap structure is maintained. The heap[0] element also returns the smallest element each time. 

It supports the extraction and insertion of the smallest element in the O(log n) times.

```python
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ", end="")
print (list(li))

# using heappush() to push elements into heap
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ", end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ", end="")
print (heapq.heappop(li))
```
#### Output
```
The created heap is : [1, 3, 9, 7, 5]
The modified heap after push is : [1, 3, 4, 7, 5, 9]
The popped and smallest element is : 1
```