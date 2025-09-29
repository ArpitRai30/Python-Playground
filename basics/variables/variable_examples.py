"""
Variables in Python - Examples and Best Practices
"""

# Basic variable assignment
name = "Python Playground"
age = 25
height = 5.9
is_programmer = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Programmer: {is_programmer}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Same value to multiple variables
a = b = c = 10
print(f"a={a}, b={b}, c={c}")

# Variable naming conventions
first_name = "John"  # Snake case (recommended)
lastName = "Doe"     # Camel case
CONSTANT_VALUE = 100 # Constants in uppercase

# Variable scope examples
global_var = "I'm global"

def function_scope_example():
    local_var = "I'm local"
    global global_var
    global_var = "Modified global"
    print(f"Local variable: {local_var}")
    print(f"Global variable inside function: {global_var}")

function_scope_example()
print(f"Global variable outside function: {global_var}")

# Dynamic typing
dynamic_var = 42
print(f"Dynamic var as integer: {dynamic_var}")
dynamic_var = "Now I'm a string"
print(f"Dynamic var as string: {dynamic_var}")
dynamic_var = [1, 2, 3]
print(f"Dynamic var as list: {dynamic_var}")