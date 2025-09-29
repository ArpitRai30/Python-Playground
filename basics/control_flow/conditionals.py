"""
Control Flow in Python - If/Else Statements
"""

# Basic if statement
print("=== BASIC IF STATEMENT ===")
age = 18
if age >= 18:
    print("You are an adult!")

# If-else statement
print("\n=== IF-ELSE STATEMENT ===")
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# If-elif-else statement
print("\n=== IF-ELIF-ELSE STATEMENT ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Nested if statements
print("\n=== NESTED IF STATEMENTS ===")
username = "admin"
password = "secret123"
is_active = True

if username == "admin":
    if password == "secret123":
        if is_active:
            print("Welcome, Admin!")
        else:
            print("Account is deactivated.")
    else:
        print("Incorrect password.")
else:
    print("Access denied.")

# Multiple conditions with logical operators
print("\n=== MULTIPLE CONDITIONS ===")
age = 25
has_license = True
has_car = False

if age >= 18 and has_license:
    if has_car:
        print("You can drive your own car!")
    else:
        print("You can drive, but you need a car.")
elif age >= 16:
    print("You can get a learner's permit.")
else:
    print("You're too young to drive.")

# Checking membership
print("\n=== MEMBERSHIP CHECKING ===")
valid_users = ["alice", "bob", "charlie"]
current_user = "alice"

if current_user in valid_users:
    print(f"Welcome back, {current_user}!")
else:
    print("User not found.")

# Checking data types
print("\n=== TYPE CHECKING ===")
data = "Hello"

if isinstance(data, str):
    print("Data is a string")
elif isinstance(data, int):
    print("Data is an integer")
elif isinstance(data, list):
    print("Data is a list")
else:
    print("Unknown data type")

# Short-circuit evaluation
print("\n=== SHORT-CIRCUIT EVALUATION ===")
x = 0
y = 5

# This won't cause division by zero because of short-circuit
if x != 0 and y / x > 2:
    print("Condition met")
else:
    print("Condition not met or x is zero")

# Ternary operator (conditional expression)
print("\n=== TERNARY OPERATOR ===")
weather = "sunny"
activity = "go to the beach" if weather == "sunny" else "stay indoors"
print(f"Since it's {weather}, let's {activity}")

# Complex conditional logic
print("\n=== COMPLEX CONDITIONAL LOGIC ===")
user_age = 22
user_country = "USA"
has_passport = True
has_visa = False

can_travel = (
    user_age >= 18 and 
    has_passport and 
    (user_country == "USA" or has_visa)
)

if can_travel:
    print("You can travel internationally!")
else:
    print("Travel requirements not met.")
    
    # Detailed feedback
    if user_age < 18:
        print("- You must be 18 or older")
    if not has_passport:
        print("- You need a passport")
    if user_country != "USA" and not has_visa:
        print("- You need a visa for international travel")

# Pattern matching (Python 3.10+)
print("\n=== PATTERN MATCHING (Python 3.10+) ===")
def describe_animal(animal):
    match animal:
        case "dog":
            return "Loyal companion"
        case "cat":
            return "Independent hunter"
        case "bird":
            return "Flying friend"
        case _:  # Default case
            return "Unknown animal"

animals = ["dog", "cat", "fish"]
for animal in animals:
    description = describe_animal(animal)
    print(f"{animal}: {description}")

# Using conditions with empty collections
print("\n=== EMPTY COLLECTIONS ===")
empty_list = []
empty_string = ""
empty_dict = {}

if empty_list:
    print("List has items")
else:
    print("List is empty")

if not empty_string:
    print("String is empty")

if empty_dict:
    print("Dictionary has items")
else:
    print("Dictionary is empty")