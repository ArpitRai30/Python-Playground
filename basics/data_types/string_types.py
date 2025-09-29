"""
String Data Type in Python - Comprehensive Examples
"""

# String creation
single_quotes = 'Hello, World!'
double_quotes = "Python is awesome"
triple_quotes = """This is a
multi-line string"""

print(single_quotes)
print(double_quotes)
print(triple_quotes)

# String indexing and slicing
text = "Python Programming"
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Substring (0-5): {text[0:6]}")
print(f"Every second character: {text[::2]}")
print(f"Reverse string: {text[::-1]}")

# String methods
sample = "  Hello Python World  "
print(f"Original: '{sample}'")
print(f"Upper: {sample.upper()}")
print(f"Lower: {sample.lower()}")
print(f"Capitalize: {sample.capitalize()}")
print(f"Title: {sample.title()}")
print(f"Strip: '{sample.strip()}'")
print(f"Replace: {sample.replace('Python', 'Java')}")

# String formatting
name = "Alice"
age = 30
score = 95.5

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}, Score: {score:.1f}")

# format() method
print("Name: {}, Age: {}, Score: {:.1f}".format(name, age, score))

# % formatting (older style)
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

# String operations
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print(f"Concatenation: {concatenated}")
print(f"Repetition: {str1 * 3}")
print(f"Length: {len(concatenated)}")
print(f"'Hello' in concatenated: {'Hello' in concatenated}")

# String validation methods
email = "user@example.com"
number = "12345"
alpha = "hello"
alphanum = "hello123"

print(f"'{email}' contains '@': {'@' in email}")
print(f"'{number}' is digit: {number.isdigit()}")
print(f"'{alpha}' is alpha: {alpha.isalpha()}")
print(f"'{alphanum}' is alphanumeric: {alphanum.isalnum()}")

# String splitting and joining
sentence = "Python is a powerful programming language"
words = sentence.split()
print(f"Words: {words}")
print(f"Joined with '-': {'-'.join(words)}")

# String escape characters
escaped = "He said, \"Python is great!\"\nNew line here\tTab here"
print(escaped)

# Raw strings
raw_string = r"C:\Users\name\Documents"
print(f"Raw string: {raw_string}")