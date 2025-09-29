"""
Error Handling and Exception Management in Python
"""

import traceback
import logging
import sys
from contextlib import contextmanager

# Basic exception handling
print("=== BASIC EXCEPTION HANDLING ===")

def basic_exception_examples():
    """Demonstrate basic exception handling."""
    
    # Try-except block
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
    # Multiple exception types
    try:
        numbers = [1, 2, 3]
        value = numbers[10]  # IndexError
    except (IndexError, KeyError) as e:
        print(f"Error accessing data: {e}")
    
    # Generic exception handling
    try:
        int("not_a_number")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")

basic_exception_examples()

# Specific exception types
print("\n=== SPECIFIC EXCEPTION TYPES ===")

def specific_exceptions():
    """Demonstrate handling specific exception types."""
    
    # ValueError
    try:
        age = int(input("Enter your age (simulated): "))
    except ValueError:
        print("ValueError: Please enter a valid number")
        age = 25  # Default value
    
    # TypeError
    try:
        result = "string" + 5
    except TypeError as e:
        print(f"TypeError: {e}")
    
    # KeyError
    person = {"name": "Alice", "age": 30}
    try:
        profession = person["profession"]
    except KeyError:
        print("KeyError: 'profession' not found in person data")
        profession = "Unknown"
    
    # FileNotFoundError
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("FileNotFoundError: File does not exist")
    
    # AttributeError
    try:
        numbers = [1, 2, 3]
        numbers.append_item(4)  # Wrong method name
    except AttributeError as e:
        print(f"AttributeError: {e}")

# Simulate input for the example
import builtins
original_input = builtins.input
builtins.input = lambda prompt: "25"  # Mock input
specific_exceptions()
builtins.input = original_input  # Restore original input

# Try-except-else-finally
print("\n=== TRY-EXCEPT-ELSE-FINALLY ===")

def complete_exception_handling():
    """Demonstrate complete exception handling structure."""
    
    def divide_numbers(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: Division by zero!")
            return None
        except TypeError:
            print("Error: Invalid input types!")
            return None
        else:
            print(f"Division successful: {a} / {b} = {result}")
            return result
        finally:
            print("Division operation completed")
    
    # Test cases
    print("Test 1: Normal division")
    divide_numbers(10, 2)
    
    print("\nTest 2: Division by zero")
    divide_numbers(10, 0)
    
    print("\nTest 3: Invalid types")
    divide_numbers("10", 2)

complete_exception_handling()

# Custom exceptions
print("\n=== CUSTOM EXCEPTIONS ===")

class CustomException(Exception):
    """Base custom exception."""
    pass

class ValidationError(CustomException):
    """Exception for validation errors."""
    
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field

class AuthenticationError(CustomException):
    """Exception for authentication errors."""
    
    def __init__(self, message, username=None):
        super().__init__(message)
        self.username = username

class BankAccount:
    """Bank account class with custom exceptions."""
    
    def __init__(self, balance=0):
        if balance < 0:
            raise ValidationError("Initial balance cannot be negative", "balance")
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive", "amount")
        if amount > self.balance:
            raise ValidationError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValidationError("Deposit amount must be positive", "amount")
        self.balance += amount
        return self.balance

def test_custom_exceptions():
    """Test custom exceptions."""
    
    try:
        # Test invalid initial balance
        account = BankAccount(-100)
    except ValidationError as e:
        print(f"Validation Error: {e} (Field: {e.field})")
    
    # Valid account
    account = BankAccount(1000)
    
    try:
        # Test invalid withdrawal
        account.withdraw(1500)
    except ValidationError as e:
        print(f"Withdrawal Error: {e}")
    
    try:
        # Test invalid deposit
        account.deposit(-50)
    except ValidationError as e:
        print(f"Deposit Error: {e} (Field: {e.field})")

test_custom_exceptions()

# Exception chaining
print("\n=== EXCEPTION CHAINING ===")

def exception_chaining():
    """Demonstrate exception chaining."""
    
    def process_data(data):
        try:
            # Simulate processing that might fail
            if not isinstance(data, dict):
                raise TypeError("Data must be a dictionary")
            return data["result"] * 2
        except KeyError as e:
            # Chain the exception
            raise ValidationError("Missing required field") from e
        except TypeError as e:
            # Re-raise with additional context
            raise ValidationError("Invalid data format") from e
    
    try:
        result = process_data({"wrong_key": 5})
    except ValidationError as e:
        print(f"Validation Error: {e}")
        print(f"Original cause: {e.__cause__}")
        print(f"Exception chain:")
        print(f"  Current: {type(e).__name__}: {e}")
        if e.__cause__:
            print(f"  Caused by: {type(e.__cause__).__name__}: {e.__cause__}")

exception_chaining()

# Context managers for resource management
print("\n=== CONTEXT MANAGERS FOR ERROR HANDLING ===")

@contextmanager
def error_handler(operation_name):
    """Context manager for error handling."""
    print(f"Starting {operation_name}")
    try:
        yield
    except Exception as e:
        print(f"Error in {operation_name}: {type(e).__name__}: {e}")
        # Log error, cleanup, etc.
        return False  # Suppress exception
    else:
        print(f"Successfully completed {operation_name}")
    finally:
        print(f"Finished {operation_name}")

def context_manager_examples():
    """Demonstrate context managers for error handling."""
    
    # Using error handler context manager
    with error_handler("file operation"):
        with open("/tmp/test_file.txt", "w") as f:
            f.write("Test content")
    
    with error_handler("risky calculation"):
        result = 10 / 0  # This will cause an error

context_manager_examples()

# Logging for error tracking
print("\n=== LOGGING FOR ERROR TRACKING ===")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def logging_examples():
    """Demonstrate logging for error tracking."""
    
    def safe_division(a, b):
        try:
            logger.info(f"Attempting division: {a} / {b}")
            result = a / b
            logger.info(f"Division successful: {result}")
            return result
        except ZeroDivisionError:
            logger.error(f"Division by zero attempted: {a} / {b}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in division: {e}")
            logger.debug("Full traceback:", exc_info=True)
            return None
    
    # Test with logging
    safe_division(10, 2)
    safe_division(10, 0)
    safe_division("invalid", 2)

logging_examples()

# Debugging and traceback
print("\n=== DEBUGGING AND TRACEBACK ===")

def debugging_examples():
    """Demonstrate debugging and traceback usage."""
    
    def problematic_function():
        def inner_function():
            def deepest_function():
                raise ValueError("Something went wrong deep in the code")
            deepest_function()
        inner_function()
    
    try:
        problematic_function()
    except ValueError:
        print("Exception caught! Here's the full traceback:")
        traceback.print_exc()
        
        print("\nFormatted traceback:")
        tb_lines = traceback.format_exc()
        print(tb_lines)
        
        print("\nTraceback as list:")
        tb_list = traceback.format_exception(*sys.exc_info())
        for line in tb_list:
            print(f"  {line.strip()}")

debugging_examples()

# Error handling best practices
print("\n=== ERROR HANDLING BEST PRACTICES ===")

def best_practices_examples():
    """Demonstrate error handling best practices."""
    
    # 1. Be specific with exceptions
    def good_exception_handling(data):
        try:
            return int(data)
        except ValueError:
            print(f"Cannot convert '{data}' to integer")
            return None
        except TypeError:
            print(f"Invalid type for conversion: {type(data)}")
            return None
    
    # 2. Don't catch and ignore
    def bad_practice():
        try:
            result = 1 / 0
        except:
            pass  # BAD: Silent failure
    
    def good_practice():
        try:
            result = 1 / 0
        except ZeroDivisionError:
            logger.error("Division by zero attempted")
            return None
    
    # 3. Use finally for cleanup
    def resource_management():
        resource = None
        try:
            resource = "database_connection"  # Simulate resource
            # Do work with resource
            result = 10 / 2
        except Exception as e:
            logger.error(f"Error processing: {e}")
            return None
        finally:
            if resource:
                print("Cleaning up resource")
                # Close connections, files, etc.
    
    # 4. Validate input early
    def process_user_data(name, age, email):
        # Input validation
        if not isinstance(name, str) or not name.strip():
            raise ValidationError("Name must be a non-empty string", "name")
        
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValidationError("Age must be a valid integer between 0 and 150", "age")
        
        if not isinstance(email, str) or "@" not in email:
            raise ValidationError("Email must be a valid email address", "email")
        
        return {"name": name.strip(), "age": age, "email": email.lower()}
    
    # Test examples
    print("Testing good exception handling:")
    print(good_exception_handling("123"))
    print(good_exception_handling("abc"))
    print(good_exception_handling(None))
    
    print("\nTesting resource management:")
    resource_management()
    
    print("\nTesting input validation:")
    try:
        user = process_user_data("John Doe", 30, "john@example.com")
        print(f"Valid user: {user}")
    except ValidationError as e:
        print(f"Validation failed: {e}")
    
    try:
        user = process_user_data("", 30, "john@example.com")
    except ValidationError as e:
        print(f"Validation failed: {e}")

best_practices_examples()

# Exception handling patterns
print("\n=== EXCEPTION HANDLING PATTERNS ===")

def exception_patterns():
    """Demonstrate common exception handling patterns."""
    
    # 1. Retry pattern
    def retry_operation(func, max_retries=3):
        for attempt in range(max_retries):
            try:
                return func()
            except Exception as e:
                if attempt == max_retries - 1:
                    raise  # Re-raise on final attempt
                print(f"Attempt {attempt + 1} failed: {e}")
                print(f"Retrying... ({max_retries - attempt - 1} attempts left)")
    
    # 2. Circuit breaker pattern (simplified)
    class CircuitBreaker:
        def __init__(self, failure_threshold=3):
            self.failure_count = 0
            self.failure_threshold = failure_threshold
            self.is_open = False
        
        def call(self, func):
            if self.is_open:
                raise Exception("Circuit breaker is open")
            
            try:
                result = func()
                self.failure_count = 0  # Reset on success
                return result
            except Exception as e:
                self.failure_count += 1
                if self.failure_count >= self.failure_threshold:
                    self.is_open = True
                    print("Circuit breaker opened!")
                raise
    
    # Test retry pattern
    def unreliable_function():
        import random
        if random.random() < 0.7:  # 70% chance of failure
            raise ConnectionError("Network error")
        return "Success!"
    
    try:
        # Fix the random seed for predictable demo
        import random
        random.seed(42)
        result = retry_operation(unreliable_function, max_retries=3)
        print(f"Operation succeeded: {result}")
    except Exception as e:
        print(f"Operation failed after all retries: {e}")

exception_patterns()

print("\n=== SUMMARY ===")
print("Exception handling covers:")
print("1. Basic try-except blocks")
print("2. Specific exception types")
print("3. Custom exceptions")
print("4. Exception chaining")
print("5. Context managers")
print("6. Logging and debugging")
print("7. Best practices and patterns")
print("\nRemember: Handle exceptions gracefully and provide meaningful error messages!")