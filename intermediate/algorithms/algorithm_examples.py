"""
Common Algorithms in Python - Sorting, Searching, and More
"""

import time
import random

# Sorting Algorithms
def bubble_sort(arr):
    """Bubble sort implementation - O(n²) time complexity."""
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    """Selection sort implementation - O(n²) time complexity."""
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Insertion sort implementation - O(n²) time complexity."""
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Merge sort implementation - O(n log n) time complexity."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """Quick sort implementation - O(n log n) average time complexity."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Testing sorting algorithms
print("=== SORTING ALGORITHMS ===")
test_array = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {test_array}")
print(f"Bubble sort: {bubble_sort(test_array)}")
print(f"Selection sort: {selection_sort(test_array)}")
print(f"Insertion sort: {insertion_sort(test_array)}")
print(f"Merge sort: {merge_sort(test_array)}")
print(f"Quick sort: {quick_sort(test_array)}")
print(f"Python built-in: {sorted(test_array)}")

# Searching Algorithms
def linear_search(arr, target):
    """Linear search - O(n) time complexity."""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    """Binary search - O(log n) time complexity (requires sorted array)."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive binary search."""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

print("\n=== SEARCHING ALGORITHMS ===")
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
print(f"Array: {sorted_array}")
print(f"Searching for: {target}")
print(f"Linear search: index {linear_search(sorted_array, target)}")
print(f"Binary search: index {binary_search(sorted_array, target)}")
print(f"Binary search (recursive): index {binary_search_recursive(sorted_array, target)}")

# Graph Algorithms
class Graph:
    """Simple graph implementation using adjacency list."""
    
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        """Add edge to graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph
    
    def bfs(self, start):
        """Breadth-first search."""
        visited = set()
        queue = [start]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([neighbor for neighbor in self.graph.get(vertex, []) 
                            if neighbor not in visited])
        return result
    
    def dfs(self, start, visited=None):
        """Depth-first search."""
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result

print("\n=== GRAPH ALGORITHMS ===")
g = Graph()
edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]
for u, v in edges:
    g.add_edge(u, v)

print(f"Graph: {g.graph}")
print(f"BFS from 0: {g.bfs(0)}")
print(f"DFS from 0: {g.dfs(0)}")

# Dynamic Programming Examples
def fibonacci_recursive(n):
    """Fibonacci using recursion - exponential time."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, memo={}):
    """Fibonacci with memoization - linear time."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

def fibonacci_dp(n):
    """Fibonacci using dynamic programming - linear time."""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

print("\n=== DYNAMIC PROGRAMMING ===")
n = 10
print(f"Fibonacci({n}):")
print(f"  Recursive: {fibonacci_recursive(n)}")
print(f"  Memoized: {fibonacci_memoized(n)}")
print(f"  DP: {fibonacci_dp(n)}")

# Longest Common Subsequence
def lcs(text1, text2):
    """Longest Common Subsequence using dynamic programming."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

text1, text2 = "abcde", "ace"
print(f"LCS of '{text1}' and '{text2}': {lcs(text1, text2)}")

# Two Pointers Technique
def two_sum_sorted(arr, target):
    """Two sum problem for sorted array using two pointers."""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

def remove_duplicates(arr):
    """Remove duplicates from sorted array in-place."""
    if not arr:
        return 0
    
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1

print("\n=== TWO POINTERS TECHNIQUE ===")
sorted_arr = [2, 7, 11, 15]
target_sum = 9
result = two_sum_sorted(sorted_arr, target_sum)
print(f"Two sum in {sorted_arr} for target {target_sum}: indices {result}")

dup_arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
print(f"Array with duplicates: {dup_arr}")
new_length = remove_duplicates(dup_arr)
print(f"After removing duplicates: {dup_arr[:new_length]}")

# String Algorithms
def is_palindrome(s):
    """Check if string is palindrome (ignoring case and non-alphanumeric)."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def longest_common_prefix(strs):
    """Find longest common prefix among array of strings."""
    if not strs:
        return ""
    
    min_len = min(len(s) for s in strs)
    
    for i in range(min_len):
        char = strs[0][i]
        for string in strs[1:]:
            if string[i] != char:
                return strs[0][:i]
    
    return strs[0][:min_len]

print("\n=== STRING ALGORITHMS ===")
test_strings = ["A man a plan a canal Panama", "race a car", "hello"]
for s in test_strings:
    print(f"'{s}' is palindrome: {is_palindrome(s)}")

string_array = ["flower", "flow", "flight"]
print(f"Longest common prefix of {string_array}: '{longest_common_prefix(string_array)}'")

# Algorithm Performance Comparison
def time_algorithm(func, *args):
    """Measure algorithm execution time."""
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

print("\n=== ALGORITHM PERFORMANCE COMPARISON ===")
large_array = list(range(1000, 0, -1))  # Reverse sorted array

# Compare sorting algorithms on larger dataset
algorithms = [
    ("Python built-in", sorted),
    ("Quick sort", quick_sort),
    ("Merge sort", merge_sort),
]

print("Sorting 1000 elements (reverse sorted):")
for name, func in algorithms:
    result, duration = time_algorithm(func, large_array)
    print(f"{name}: {duration:.6f} seconds")

# Big O notation examples
def constant_time_operation(arr):
    """O(1) - Constant time."""
    return arr[0] if arr else None

def linear_time_operation(arr):
    """O(n) - Linear time."""
    return sum(arr)

def quadratic_time_operation(arr):
    """O(n²) - Quadratic time."""
    result = []
    for i in arr:
        for j in arr:
            result.append(i + j)
    return len(result)

print("\n=== BIG O EXAMPLES ===")
test_sizes = [100, 200, 400]
for size in test_sizes:
    test_arr = list(range(size))
    
    _, const_time = time_algorithm(constant_time_operation, test_arr)
    _, linear_time = time_algorithm(linear_time_operation, test_arr)
    _, quad_time = time_algorithm(quadratic_time_operation, test_arr[:10])  # Smaller for O(n²)
    
    print(f"Size {size}: O(1)={const_time:.6f}s, O(n)={linear_time:.6f}s")