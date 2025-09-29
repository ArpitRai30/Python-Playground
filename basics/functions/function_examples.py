"""
Functions in Python - Definition, Parameters, and Best Practices
"""

# Basic function definition
def greet():
    """Simple function with no parameters."""
    print("Hello, World!")

print("=== BASIC FUNCTION ===")
greet()

# Function with parameters
def greet_person(name):
    """Function with one parameter."""
    print(f"Hello, {name}!")

print("\n=== FUNCTION WITH PARAMETERS ===")
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def add_numbers(a, b):
    """Function that adds two numbers."""
    return a + b

print("\n=== FUNCTION WITH RETURN VALUE ===")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameters
def greet_with_title(name, title="Mr."):
    """Function with default parameter."""
    return f"Hello, {title} {name}!"

print("\n=== FUNCTION WITH DEFAULT PARAMETERS ===")
print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))

# Function with keyword arguments
def create_profile(name, age, city="Unknown", profession="Unknown"):
    """Function demonstrating keyword arguments."""
    return {
        "name": name,
        "age": age,
        "city": city,
        "profession": profession
    }

print("\n=== KEYWORD ARGUMENTS ===")
profile1 = create_profile("Alice", 30)
profile2 = create_profile("Bob", 25, city="New York", profession="Engineer")
print(f"Profile 1: {profile1}")
print(f"Profile 2: {profile2}")

# Function with variable arguments (*args)
def sum_all(*args):
    """Function that accepts variable number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

print("\n=== VARIABLE ARGUMENTS (*args) ===")
print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

# Function with keyword variable arguments (**kwargs)
def print_info(**kwargs):
    """Function that accepts variable keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n=== KEYWORD VARIABLE ARGUMENTS (**kwargs) ===")
print_info(name="Charlie", age=28, city="Boston", job="Designer")

# Function with both *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function with both variable positional and keyword arguments."""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print("\n=== COMBINED *args AND **kwargs ===")
flexible_function(1, 2, 3, name="David", age=32)

# Lambda functions (anonymous functions)
print("\n=== LAMBDA FUNCTIONS ===")
square = lambda x: x ** 2
multiply = lambda x, y: x * y

print(f"Square of 5: {square(5)}")
print(f"Multiply 4 and 6: {multiply(4, 6)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")
print(f"Even numbers: {even_numbers}")

# Higher-order functions
def apply_operation(numbers, operation):
    """Function that takes another function as parameter."""
    return [operation(x) for x in numbers]

def double(x):
    return x * 2

def cube(x):
    return x ** 3

print("\n=== HIGHER-ORDER FUNCTIONS ===")
nums = [1, 2, 3, 4]
doubled = apply_operation(nums, double)
cubed = apply_operation(nums, cube)

print(f"Original: {nums}")
print(f"Doubled: {doubled}")
print(f"Cubed: {cubed}")

# Recursive functions
def factorial(n):
    """Recursive function to calculate factorial."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\n=== RECURSIVE FUNCTION ===")
for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")

# Function scope and global variables
global_var = "I'm global"

def scope_example():
    local_var = "I'm local"
    global global_var
    global_var = "Modified global"
    print(f"Local: {local_var}")
    print(f"Global inside function: {global_var}")

print("\n=== FUNCTION SCOPE ===")
print(f"Global before: {global_var}")
scope_example()
print(f"Global after: {global_var}")

# Function annotations (type hints)
def annotated_function(name: str, age: int) -> str:
    """Function with type annotations."""
    return f"{name} is {age} years old"

print("\n=== FUNCTION ANNOTATIONS ===")
result = annotated_function("Eve", 27)
print(result)

# Nested functions and closures
def outer_function(x):
    """Demonstrates nested functions and closures."""
    def inner_function(y):
        return x + y
    return inner_function

print("\n=== NESTED FUNCTIONS AND CLOSURES ===")
add_five = outer_function(5)
print(f"add_five(3) = {add_five(3)}")

# Decorator example
def timing_decorator(func):
    """Simple decorator example."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

@timing_decorator
def say_hello(name):
    print(f"Hello, {name}!")

print("\n=== DECORATOR EXAMPLE ===")
say_hello("Frank")