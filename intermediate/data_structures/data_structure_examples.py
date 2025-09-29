"""
Data Structures in Python - Advanced Collections and Custom Implementations
"""

from collections import deque, defaultdict, Counter, namedtuple
import heapq

# Stack implementation using list
class Stack:
    """Simple stack implementation using list."""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return stack size."""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

print("=== STACK IMPLEMENTATION ===")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack: {stack}")
print(f"Pop: {stack.pop()}")
print(f"Peek: {stack.peek()}")
print(f"Size: {stack.size()}")

# Queue implementation using deque
class Queue:
    """Queue implementation using deque for efficiency."""
    
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to rear of queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()
    
    def front(self):
        """Return front item without removing."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return queue size."""
        return len(self.items)
    
    def __str__(self):
        return str(list(self.items))

print("\n=== QUEUE IMPLEMENTATION ===")
queue = Queue()
queue.enqueue("first")
queue.enqueue("second")
queue.enqueue("third")
print(f"Queue: {queue}")
print(f"Dequeue: {queue.dequeue()}")
print(f"Front: {queue.front()}")
print(f"Size: {queue.size()}")

# Linked List implementation
class Node:
    """Node for linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Simple linked list implementation."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Add element to end of list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add element to beginning of list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete first occurrence of data."""
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def find(self, data):
        """Find element in list."""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

print("\n=== LINKED LIST IMPLEMENTATION ===")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
print(f"Linked List: {ll}")
print(f"Find 2: position {ll.find(2)}")
print(f"Delete 2: {ll.delete(2)}")
print(f"After deletion: {ll}")
print(f"Length: {len(ll)}")

# Binary Tree implementation
class TreeNode:
    """Node for binary tree."""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Binary tree implementation."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert data into binary search tree."""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper method for insertion."""
        if node is None:
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        
        return node
    
    def inorder_traversal(self):
        """In-order traversal (left, root, right)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper for in-order traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Pre-order traversal (root, left, right)."""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper for pre-order traversal."""
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def find(self, data):
        """Find data in tree."""
        return self._find_recursive(self.root, data)
    
    def _find_recursive(self, node, data):
        """Helper for finding data."""
        if node is None or node.data == data:
            return node is not None
        
        if data < node.data:
            return self._find_recursive(node.left, data)
        else:
            return self._find_recursive(node.right, data)

print("\n=== BINARY TREE IMPLEMENTATION ===")
bt = BinaryTree()
numbers = [5, 3, 7, 2, 4, 6, 8]
for num in numbers:
    bt.insert(num)

print(f"In-order traversal: {bt.inorder_traversal()}")
print(f"Pre-order traversal: {bt.preorder_traversal()}")
print(f"Find 4: {bt.find(4)}")
print(f"Find 9: {bt.find(9)}")

# Advanced collections from collections module
print("\n=== COLLECTIONS MODULE ===")

# defaultdict
dd = defaultdict(list)
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
for word in words:
    dd[word[0]].append(word)
print(f"Words by first letter: {dict(dd)}")

# Counter
text = "hello world"
counter = Counter(text)
print(f"Character count in '{text}': {counter}")
print(f"Most common: {counter.most_common(3)}")

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, 4)
print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Distance: {((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5:.2f}")

# deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"Deque: {dq}")
print(f"Pop left: {dq.popleft()}")
print(f"Pop right: {dq.pop()}")
print(f"After pops: {dq}")

# Priority Queue using heapq
print("\n=== PRIORITY QUEUE (HEAPQ) ===")
tasks = []
heapq.heappush(tasks, (3, "Low priority task"))
heapq.heappush(tasks, (1, "High priority task"))
heapq.heappush(tasks, (2, "Medium priority task"))

print("Processing tasks by priority:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority {priority}: {task}")

# Set operations and advanced usage
print("\n=== ADVANCED SET OPERATIONS ===")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2, 3}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")
print(f"Union A ∪ B: {set_a.union(set_b)}")
print(f"Intersection A ∩ B: {set_a.intersection(set_b)}")
print(f"Difference A - B: {set_a.difference(set_b)}")
print(f"Symmetric difference A △ B: {set_a.symmetric_difference(set_b)}")
print(f"Is C subset of A? {set_c.issubset(set_a)}")
print(f"Is A superset of C? {set_a.issuperset(set_c)}")

# Dictionary advanced operations
print("\n=== ADVANCED DICTIONARY OPERATIONS ===")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 5, "e": 6}

# Dictionary comprehension
squared_dict = {k: v**2 for k, v in dict1.items()}
print(f"Squared values: {squared_dict}")

# Merge dictionaries (Python 3.9+)
merged = dict1 | dict2
print(f"Merged (dict1 | dict2): {merged}")

# Dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person_dict = dict(zip(keys, values))
print(f"Dict from zip: {person_dict}")

# Nested dictionary
nested = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(f"Nested dict: {nested}")
print(f"Person1 name: {nested['person1']['name']}")