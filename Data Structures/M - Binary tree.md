# Binary Tree
A tree is a  hierarchical data structure that looks like the below figure – 
![](https://miro.medium.com/v2/resize:fit:942/1*5LIURkrDDbz_S9paZ9EdZw.png)

The topmost node of the tree is called the root whereas the bottommost nodes or the nodes with no children are called the leaf nodes. The nodes that are directly under a node are called its children and the nodes that are directly above something are called its parent.

A binary tree is a tree whose elements can have almost two children. Since each element in a binary tree can have only 2 children, we typically name them the left and right children. A Binary Tree node contains the following parts.

- Data
- Pointer to left child
- Pointer to the right child

### Example: Defining Node Class
```python
# A Python class that represents an individual node
# in a Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
```
Now let’s create a tree with 4 nodes in Python. Let’s assume the tree structure looks like below – 
```
     tree
     ----
      1    <-- root
    /   \
   2     3  
  /  
 4
 ```
### Example: Adding data to the tree
```python
# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# create root
root = Node(1)
''' 
following is the tree after above statement
        1
       / \
    None None
'''

root.left = Node(2)
root.right = Node(3)

''' 
2 and 3 become left and right children of 1
        1
      /   \
     /     \
    2        3
  /   \    /   \
None None None None
'''

root.left.left = Node(4)
'''
4 becomes left child of 2
        1
      /   \
     /     \
    2        3
  /   \    /   \
 4   None None None
'''
```
## Tree Traversal
Trees can be traversed in different ways. Following are the generally used ways for traversing trees. Let us consider the below tree – 
```
     tree
     ----
      1    <-- root
    /   \
   2     3  
  / \
 4   5
``` 
### Depth First Traversals:

- Inorder (Left, Root, Right) : 4 2 5 1 3
- Preorder (Root, Left, Right) : 1 2 4 5 3
- Postorder (Left, Right, Root) : 4 5 2 3 1

### Algorithm Inorder(tree)

- Traverse the left subtree, i.e., call Inorder(left-subtree)
Visit the root.
- Traverse the right subtree, i.e., call Inorder(right-subtree)

### Algorithm Preorder(tree)

- Visit the root.
- Traverse the left subtree, i.e., call Preorder(left-subtree)
- Traverse the right subtree, i.e., call Preorder(right-subtree)

### Algorithm Postorder(tree)

- Traverse the left subtree, i.e., call Postorder(left-subtree)
- Traverse the right subtree, i.e., call Postorder(right-subtree)
- Visit the root.
```python
# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)
```
#### Output
```
Preorder traversal of binary tree is
1
2
4
5
3

Inorder traversal of binary tree is
4
2
5
1
3

Postorder traversal of binary tree is
4
5
2
3
1
```
### Time Complexity –  O(n) 

## Breadth-First or Level Order Traversal

Level order traversal of a tree is breadth-first traversal for the tree. The level order traversal of the above tree is 1 2 3 4 5.

For each node, first, the node is visited and then its child nodes are put in a FIFO queue. Below is the algorithm for the same – 

- Create an empty queue q
- temp_node = root /*start from root*/
- Loop while temp_node is not NULL
    - print temp_node->data.
    - Enqueue temp_node’s children (first left then right children) to q
    - Dequeue a node from q

```python
# Python program to print level
# order traversal using Queue

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None

# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return
    
    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):   
        # Print front of queue and
        # remove it from queue
        print (queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level Order Traversal of binary tree is -")
printLevelOrder(root)
```
#### Output
```
Level Order Traversal of binary tree is -
1
2
3
4
5
```
Time Complexity: O(n)