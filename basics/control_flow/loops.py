"""
Loops in Python - For and While Loops
"""

# Basic for loop with range
print("=== BASIC FOR LOOP ===")
for i in range(5):
    print(f"Iteration {i}")

# For loop with start, stop, step
print("\n=== FOR LOOP WITH RANGE PARAMETERS ===")
for i in range(2, 10, 2):  # start=2, stop=10, step=2
    print(f"Even number: {i}")

# Iterating over lists
print("\n=== ITERATING OVER LISTS ===")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")

# Enumerate for index and value
print("\n=== ENUMERATE - INDEX AND VALUE ===")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Iterating over dictionaries
print("\n=== ITERATING OVER DICTIONARIES ===")
student = {"name": "Alice", "age": 20, "grade": "A"}

print("Keys:")
for key in student.keys():
    print(f"  {key}")

print("Values:")
for value in student.values():
    print(f"  {value}")

print("Key-Value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Nested loops
print("\n=== NESTED LOOPS ===")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row

# List comprehension (alternative to loops)
print("\n=== LIST COMPREHENSION ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# While loop
print("\n=== WHILE LOOP ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input simulation
print("\n=== WHILE LOOP WITH CONDITION ===")
number = 1
while number <= 100:
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1
    if number > 15:  # Limit output for demo
        break

# Break and continue statements
print("\n=== BREAK AND CONTINUE ===")
print("Numbers 1-10, skip 5, stop at 8:")
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break     # Stop at 8
    print(i)

# Else clause with loops
print("\n=== ELSE CLAUSE WITH LOOPS ===")
# For loop with else
for i in range(3):
    print(f"For loop iteration {i}")
else:
    print("For loop completed normally")

# While loop with else
count = 0
while count < 3:
    print(f"While loop count {count}")
    count += 1
else:
    print("While loop completed normally")

# Loop with break (else won't execute)
print("\n=== LOOP WITH BREAK (ELSE SKIPPED) ===")
for i in range(5):
    if i == 3:
        print("Breaking out of loop")
        break
    print(f"Iteration {i}")
else:
    print("This won't print because of break")

# Infinite loop with break condition
print("\n=== CONTROLLED INFINITE LOOP ===")
counter = 0
while True:
    if counter >= 3:
        print("Breaking out of infinite loop")
        break
    print(f"Infinite loop iteration {counter}")
    counter += 1

# Zip function for parallel iteration
print("\n=== ZIP FOR PARALLEL ITERATION ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Reversed iteration
print("\n=== REVERSED ITERATION ===")
numbers = [1, 2, 3, 4, 5]
print("Forward:")
for num in numbers:
    print(num, end=" ")

print("\nBackward:")
for num in reversed(numbers):
    print(num, end=" ")
print()

# Loop performance tips
print("\n=== LOOP PERFORMANCE EXAMPLE ===")
# Good: Using range for simple counting
start_time = 0
for i in range(1000000):
    pass
print("Range loop completed")

# Good: List comprehension for simple transformations
original_list = list(range(10))
doubled = [x * 2 for x in original_list]
print(f"Doubled: {doubled[:5]}...")  # Show first 5 elements