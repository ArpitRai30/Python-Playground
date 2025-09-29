"""
Object-Oriented Programming in Python - Classes and Objects
"""

# Basic class definition
class Person:
    """A simple Person class."""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Initialize a Person instance."""
        self.name = name  # Instance variable
        self.age = age    # Instance variable
    
    def introduce(self):
        """Method to introduce the person."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Method to increment age."""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old."

print("=== BASIC CLASS USAGE ===")
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())
print(f"Species: {Person.species}")
print(person1.have_birthday())

# Class with properties and validation
class BankAccount:
    """Bank account class with property validation."""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance  # Protected attribute
        self._transaction_history = []
    
    @property
    def balance(self):
        """Get the current balance."""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        """Set balance with validation."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
    
    def deposit(self, amount):
        """Deposit money to account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transaction_history.append(f"Deposit: +${amount}")
        return f"Deposited ${amount}. New balance: ${self._balance}"
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transaction_history.append(f"Withdrawal: -${amount}")
        return f"Withdrew ${amount}. New balance: ${self._balance}"
    
    def get_transaction_history(self):
        """Get transaction history."""
        return self._transaction_history.copy()
    
    def __str__(self):
        """String representation of account."""
        return f"Account {self.account_number}: ${self._balance}"

print("\n=== BANK ACCOUNT CLASS ===")
account = BankAccount("123456", 1000)
print(account)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.balance}")
print(f"Transaction history: {account.get_transaction_history()}")

# Inheritance
class Student(Person):
    """Student class inheriting from Person."""
    
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.major = major
        self.grades = {}
    
    def add_grade(self, subject, grade):
        """Add a grade for a subject."""
        self.grades[subject] = grade
    
    def get_gpa(self):
        """Calculate GPA."""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def introduce(self):
        """Override parent method."""
        return f"Hi, I'm {self.name}, a {self.major} student (ID: {self.student_id})"

print("\n=== INHERITANCE ===")
student = Student("Charlie", 20, "S12345", "Computer Science")
print(student.introduce())
student.add_grade("Math", 95)
student.add_grade("Physics", 88)
student.add_grade("Programming", 92)
print(f"GPA: {student.get_gpa():.2f}")

# Multiple inheritance
class Flyer:
    """Mixin class for flying ability."""
    
    def fly(self):
        return "Flying through the air!"

class Swimmer:
    """Mixin class for swimming ability."""
    
    def swim(self):
        return "Swimming through water!"

class Duck(Flyer, Swimmer):
    """Duck class with multiple inheritance."""
    
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} says: Quack!"

print("\n=== MULTIPLE INHERITANCE ===")
duck = Duck("Donald")
print(duck.quack())
print(duck.fly())
print(duck.swim())

# Abstract base class
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate area (must be implemented by subclasses)."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter (must be implemented by subclasses)."""
        pass

class Rectangle(Shape):
    """Rectangle class implementing Shape."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

class Circle(Shape):
    """Circle class implementing Shape."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

print("\n=== ABSTRACT BASE CLASS ===")
rectangle = Rectangle(5, 3)
circle = Circle(4)

shapes = [rectangle, circle]
for shape in shapes:
    print(f"{shape}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

# Class methods and static methods
class MathUtils:
    """Utility class demonstrating class and static methods."""
    
    pi = 3.14159
    
    @classmethod
    def circle_area(cls, radius):
        """Class method to calculate circle area."""
        return cls.pi * radius ** 2
    
    @staticmethod
    def is_even(number):
        """Static method to check if number is even."""
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        """Static method to calculate factorial."""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

print("\n=== CLASS AND STATIC METHODS ===")
print(f"Circle area (radius=3): {MathUtils.circle_area(3):.2f}")
print(f"Is 4 even? {MathUtils.is_even(4)}")
print(f"Is 7 even? {MathUtils.is_even(7)}")
print(f"5! = {MathUtils.factorial(5)}")

# Special methods (magic methods)
class Vector:
    """Vector class demonstrating special methods."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer representation."""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Vector addition."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """Scalar multiplication."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Equality comparison."""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Magnitude of vector."""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

print("\n=== SPECIAL METHODS ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"Length of v1: {len(v1)}")

# Property decorators
class Temperature:
    """Temperature class with property decorators."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit."""
        self.celsius = (value - 32) * 5/9

print("\n=== PROPERTY DECORATORS ===")
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")
temp.fahrenheit = 100
print(f"After setting to 100°F: {temp.celsius}°C = {temp.fahrenheit}°F")