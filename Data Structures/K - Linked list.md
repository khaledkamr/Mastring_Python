# Linked List
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image:

![linked list](https://media.geeksforgeeks.org/wp-content/uploads/20240410135517/linked-list.webp)

A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL. Each node in a list consists of at least two parts:

- Data
- Pointer (Or Reference) to the next node

### Example: Defining Linked List in Python
```python 
# Node class
class Node:
 
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize
                        # next as null
 
# Linked List class
class LinkedList:
     
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
```
### Let us create a simple linked list with 3 nodes.

```python  
# Node class
class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    list = LinkedList()
 
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
 
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
 
    list.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     | 3  | None |
    +----+------+     +----+------+     +----+------+
    '''
 
    list.head.next = second; # Link first node with second
 
    '''
    Now next of first Node refers to second. So they
    both are linked.
 
    list.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     | 3  | null |
    +----+------+     +----+------+     +----+------+
    '''
 
    second.next = third; # Link second node with the third node
 
    '''
    Now next of second Node refers to third. So all three
    nodes are linked.
 
    list.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->| 3  | null |
    +----+------+     +----+------+     +----+------+
    '''
```
## Linked List Traversal 
In the previous program, we have created a simple linked list with three nodes. Let us traverse the created list and print the data of each node. For traversal, let us write a general-purpose function printList() that prints any given list.

```python 
class Node:
 
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # This function prints contents of linked list starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
 
 
if __name__=='__main__':
 
    # Start with the empty list
    list = LinkedList()
 
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
 
    list.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
 
    list.printList()
```
#### Output
```
1
2
3
```