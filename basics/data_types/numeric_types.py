"""
Numeric Data Types in Python
"""

# Integer operations
integer_num = 42
print(f"Integer: {integer_num}")
print(f"Type: {type(integer_num)}")

# Float operations
float_num = 3.14159
print(f"Float: {float_num}")
print(f"Type: {type(float_num)}")

# Complex numbers
complex_num = 3 + 4j
print(f"Complex: {complex_num}")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")

# Number system conversions
decimal = 255
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(f"Decimal: {decimal}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")

# Mathematical operations
a, b = 10, 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# Type conversion
str_num = "123"
converted_int = int(str_num)
converted_float = float(str_num)
print(f"String to int: {converted_int}")
print(f"String to float: {converted_float}")

# Built-in numeric functions
numbers = [1, 2, 3, 4, 5]
print(f"Sum: {sum(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Absolute value of -5: {abs(-5)}")
print(f"Round 3.7: {round(3.7)}")
print(f"Round 3.14159 to 2 places: {round(3.14159, 2)}")