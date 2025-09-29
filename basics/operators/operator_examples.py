"""
Python Operators - Comprehensive Examples
"""

# Arithmetic Operators
print("=== ARITHMETIC OPERATORS ===")
a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Assignment Operators
print("\n=== ASSIGNMENT OPERATORS ===")
x = 10
print(f"x = {x}")
x += 5
print(f"x += 5: {x}")
x -= 3
print(f"x -= 3: {x}")
x *= 2
print(f"x *= 2: {x}")
x /= 4
print(f"x /= 4: {x}")
x %= 3
print(f"x %= 3: {x}")
x **= 2
print(f"x **= 2: {x}")

# Comparison Operators
print("\n=== COMPARISON OPERATORS ===")
num1, num2 = 15, 10
print(f"num1 = {num1}, num2 = {num2}")
print(f"Equal: {num1} == {num2} = {num1 == num2}")
print(f"Not Equal: {num1} != {num2} = {num1 != num2}")
print(f"Greater than: {num1} > {num2} = {num1 > num2}")
print(f"Less than: {num1} < {num2} = {num1 < num2}")
print(f"Greater or equal: {num1} >= {num2} = {num1 >= num2}")
print(f"Less or equal: {num1} <= {num2} = {num1 <= num2}")

# Logical Operators
print("\n=== LOGICAL OPERATORS ===")
p, q = True, False
print(f"p = {p}, q = {q}")
print(f"p and q = {p and q}")
print(f"p or q = {p or q}")
print(f"not p = {not p}")
print(f"not q = {not q}")

# Identity Operators
print("\n=== IDENTITY OPERATORS ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")
print(f"list1 is not list2: {list1 is not list2}")

# Membership Operators
print("\n=== MEMBERSHIP OPERATORS ===")
numbers = [1, 2, 3, 4, 5]
text = "Hello World"

print(f"Numbers: {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"6 in numbers: {6 in numbers}")
print(f"6 not in numbers: {6 not in numbers}")
print(f"'Hello' in text: {'Hello' in text}")
print(f"'Python' in text: {'Python' in text}")

# Bitwise Operators
print("\n=== BITWISE OPERATORS ===")
x, y = 12, 10  # 12 = 1100, 10 = 1010 in binary
print(f"x = {x} (binary: {bin(x)})")
print(f"y = {y} (binary: {bin(y)})")
print(f"x & y (AND): {x & y} (binary: {bin(x & y)})")
print(f"x | y (OR): {x | y} (binary: {bin(x | y)})")
print(f"x ^ y (XOR): {x ^ y} (binary: {bin(x ^ y)})")
print(f"~x (NOT): {~x}")
print(f"x << 2 (Left shift): {x << 2}")
print(f"x >> 2 (Right shift): {x >> 2}")

# Operator Precedence Example
print("\n=== OPERATOR PRECEDENCE ===")
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
result3 = 2 ** 3 ** 2  # Right associative
result4 = (2 ** 3) ** 2

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")
print(f"2 ** 3 ** 2 = {result3}")
print(f"(2 ** 3) ** 2 = {result4}")

# Ternary Operator
print("\n=== TERNARY OPERATOR ===")
age = 18
status = "adult" if age >= 18 else "minor"
print(f"Age {age} is {status}")

# Chained Comparisons
print("\n=== CHAINED COMPARISONS ===")
score = 85
grade = "A" if 90 <= score <= 100 else "B" if 80 <= score < 90 else "C" if 70 <= score < 80 else "F"
print(f"Score {score} gets grade: {grade}")

# Multiple comparisons
x = 5
result = 1 < x < 10
print(f"1 < {x} < 10: {result}")