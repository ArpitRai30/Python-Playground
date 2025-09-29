"""
Collection Data Types in Python
"""

# Lists - Ordered, mutable collections
print("=== LISTS ===")
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]

print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# List methods
fruits.append('orange')
fruits.insert(1, 'grape')
fruits.remove('banana')
print(f"Modified fruits: {fruits}")
print(f"Popped item: {fruits.pop()}")
print(f"Count of 'apple': {fruits.count('apple')}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Tuples - Ordered, immutable collections
print("\n=== TUPLES ===")
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
single_tuple = (42,)  # Note the comma for single item

print(f"Coordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")
print(f"Colors: {colors}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# Dictionaries - Key-value pairs
print("\n=== DICTIONARIES ===")
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'profession': 'Developer'
}

print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age', 'Unknown')}")

# Dictionary methods
person['email'] = 'john@example.com'
person.update({'phone': '123-456-7890'})
print(f"Updated person: {person}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ['python', 'java', 'javascript']}
print(f"Word lengths: {word_lengths}")

# Sets - Unordered collections of unique elements
print("\n=== SETS ===")
unique_numbers = {1, 2, 3, 4, 5, 5, 4}  # Duplicates removed
print(f"Unique numbers: {unique_numbers}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric difference: {set1 ^ set2}")

# Set operations
set1.add(6)
set1.remove(1)
print(f"Modified set1: {set1}")
print(f"Is 3 in set1: {3 in set1}")

# Converting between types
list_from_set = list(unique_numbers)
tuple_from_list = tuple(fruits)
set_from_string = set("hello")

print(f"\nType conversions:")
print(f"List from set: {list_from_set}")
print(f"Tuple from list: {tuple_from_list}")
print(f"Set from string: {set_from_string}")