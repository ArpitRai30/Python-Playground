"""
Testing in Python - Unit Tests, Integration Tests, and Best Practices
"""

import unittest
import pytest
import doctest
from unittest.mock import Mock, patch, MagicMock
import tempfile
import os
import json

# ===== SAMPLE CODE TO TEST =====

class Calculator:
    """Simple calculator class for demonstration."""
    
    def add(self, a, b):
        """Add two numbers.
        
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.add(-1, 1)
        0
        """
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Calculate base raised to exponent."""
        return base ** exponent

class BankAccount:
    """Bank account class for testing."""
    
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance
        self._transactions = []
    
    @property
    def balance(self):
        """Get current balance."""
        return self._balance
    
    def deposit(self, amount):
        """Deposit money."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(f"Deposit: +${amount}")
        return self._balance
    
    def withdraw(self, amount):
        """Withdraw money."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transactions.append(f"Withdrawal: -${amount}")
        return self._balance
    
    def get_transaction_history(self):
        """Get transaction history."""
        return self._transactions.copy()

class FileProcessor:
    """File processor for testing file operations."""
    
    def read_json_file(self, filename):
        """Read JSON file."""
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
    
    def write_json_file(self, filename, data):
        """Write data to JSON file."""
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

class APIClient:
    """Simple API client for testing."""
    
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_user(self, user_id):
        """Get user by ID (simulated)."""
        # This would normally make an HTTP request
        if user_id == 1:
            return {"id": 1, "name": "John Doe", "email": "john@example.com"}
        elif user_id == 2:
            return {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
        else:
            return None

# ===== UNITTEST EXAMPLES =====

class TestCalculator(unittest.TestCase):
    """Unit tests for Calculator class using unittest."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def tearDown(self):
        """Tear down test fixtures after each test method."""
        # Clean up if needed
        pass
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        result = self.calc.add(5, -3)
        self.assertEqual(result, 2)
    
    def test_subtract(self):
        """Test subtraction."""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)
    
    def test_multiply(self):
        """Test multiplication."""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)
    
    def test_divide_normal(self):
        """Test normal division."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_power(self):
        """Test power calculation."""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        result = self.calc.power(5, 0)
        self.assertEqual(result, 1)

class TestBankAccount(unittest.TestCase):
    """Unit tests for BankAccount class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.account = BankAccount(100)
    
    def test_initial_balance(self):
        """Test initial balance is set correctly."""
        account = BankAccount(50)
        self.assertEqual(account.balance, 50)
    
    def test_negative_initial_balance(self):
        """Test negative initial balance raises exception."""
        with self.assertRaises(ValueError):
            BankAccount(-10)
    
    def test_deposit_positive_amount(self):
        """Test depositing positive amount."""
        new_balance = self.account.deposit(50)
        self.assertEqual(new_balance, 150)
        self.assertEqual(self.account.balance, 150)
    
    def test_deposit_negative_amount(self):
        """Test depositing negative amount raises exception."""
        with self.assertRaises(ValueError):
            self.account.deposit(-10)
    
    def test_deposit_zero_amount(self):
        """Test depositing zero amount raises exception."""
        with self.assertRaises(ValueError):
            self.account.deposit(0)
    
    def test_withdraw_valid_amount(self):
        """Test withdrawing valid amount."""
        new_balance = self.account.withdraw(30)
        self.assertEqual(new_balance, 70)
        self.assertEqual(self.account.balance, 70)
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than balance raises exception."""
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    
    def test_transaction_history(self):
        """Test transaction history is recorded."""
        self.account.deposit(25)
        self.account.withdraw(10)
        
        history = self.account.get_transaction_history()
        self.assertEqual(len(history), 2)
        self.assertIn("Deposit: +$25", history)
        self.assertIn("Withdrawal: -$10", history)

# ===== PYTEST EXAMPLES =====

class TestCalculatorPytest:
    """Pytest examples for Calculator class."""
    
    def setup_method(self):
        """Setup method for each test."""
        self.calc = Calculator()
    
    def test_add_basic(self):
        """Test basic addition."""
        assert self.calc.add(2, 3) == 5
    
    def test_add_zero(self):
        """Test adding zero."""
        assert self.calc.add(5, 0) == 5
        assert self.calc.add(0, 5) == 5
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert self.calc.multiply(5, 0) == 0
    
    def test_divide_by_zero_pytest(self):
        """Test division by zero with pytest."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

# Pytest fixtures
@pytest.fixture
def sample_account():
    """Fixture for BankAccount."""
    return BankAccount(1000)

@pytest.fixture
def empty_account():
    """Fixture for empty BankAccount."""
    return BankAccount(0)

def test_account_deposit(sample_account):
    """Test account deposit using fixture."""
    initial_balance = sample_account.balance
    sample_account.deposit(100)
    assert sample_account.balance == initial_balance + 100

def test_account_multiple_operations(sample_account):
    """Test multiple account operations."""
    sample_account.deposit(200)
    sample_account.withdraw(150)
    assert sample_account.balance == 1050

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (-3, -4, -7)
])
def test_calculator_add_parametrized(a, b, expected):
    """Test calculator addition with multiple parameters."""
    calc = Calculator()
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("amount,expected_error", [
    (-10, "Deposit amount must be positive"),
    (0, "Deposit amount must be positive"),
])
def test_invalid_deposits(sample_account, amount, expected_error):
    """Test invalid deposit amounts."""
    with pytest.raises(ValueError, match=expected_error):
        sample_account.deposit(amount)

# ===== MOCKING EXAMPLES =====

class TestFileProcessor(unittest.TestCase):
    """Test FileProcessor with mocking."""
    
    def setUp(self):
        self.processor = FileProcessor()
    
    @patch('builtins.open')
    @patch('json.load')
    def test_read_json_file_success(self, mock_json_load, mock_open):
        """Test successful JSON file reading with mocking."""
        # Setup mocks
        mock_data = {"name": "John", "age": 30}
        mock_json_load.return_value = mock_data
        
        # Test
        result = self.processor.read_json_file("test.json")
        
        # Assertions
        self.assertEqual(result, mock_data)
        mock_open.assert_called_once_with("test.json", 'r')
        mock_json_load.assert_called_once()
    
    @patch('builtins.open', side_effect=FileNotFoundError())
    def test_read_json_file_not_found(self, mock_open):
        """Test JSON file not found error."""
        with self.assertRaises(FileNotFoundError):
            self.processor.read_json_file("nonexistent.json")
    
    @patch('builtins.open')
    @patch('json.dump')
    def test_write_json_file(self, mock_json_dump, mock_open):
        """Test JSON file writing with mocking."""
        test_data = {"test": "data"}
        
        self.processor.write_json_file("output.json", test_data)
        
        mock_open.assert_called_once_with("output.json", 'w')
        mock_json_dump.assert_called_once_with(test_data, mock_open().__enter__(), indent=2)

class TestAPIClient(unittest.TestCase):
    """Test APIClient with mocking."""
    
    def setUp(self):
        self.client = APIClient("https://api.example.com")
    
    def test_get_user_found(self):
        """Test getting existing user."""
        result = self.client.get_user(1)
        expected = {"id": 1, "name": "John Doe", "email": "john@example.com"}
        self.assertEqual(result, expected)
    
    def test_get_user_not_found(self):
        """Test getting non-existent user."""
        result = self.client.get_user(999)
        self.assertIsNone(result)

# ===== INTEGRATION TESTS =====

class IntegrationTestBankSystem(unittest.TestCase):
    """Integration tests for bank system."""
    
    def setUp(self):
        """Set up integration test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.account_file = os.path.join(self.temp_dir, "account.json")
    
    def tearDown(self):
        """Clean up integration test environment."""
        if os.path.exists(self.account_file):
            os.remove(self.account_file)
        os.rmdir(self.temp_dir)
    
    def test_account_with_file_operations(self):
        """Test bank account with file persistence."""
        # Create account and perform operations
        account = BankAccount(1000)
        account.deposit(500)
        account.withdraw(200)
        
        # Save account state to file
        account_data = {
            "balance": account.balance,
            "transactions": account.get_transaction_history()
        }
        
        processor = FileProcessor()
        processor.write_json_file(self.account_file, account_data)
        
        # Read back from file
        loaded_data = processor.read_json_file(self.account_file)
        
        # Verify data integrity
        self.assertEqual(loaded_data["balance"], 1300)
        self.assertEqual(len(loaded_data["transactions"]), 2)
        self.assertIn("Deposit: +$500", loaded_data["transactions"])
        self.assertIn("Withdrawal: -$200", loaded_data["transactions"])

# ===== PERFORMANCE TESTS =====

class PerformanceTestCalculator(unittest.TestCase):
    """Performance tests for Calculator."""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_calculation_performance(self):
        """Test calculation performance."""
        import time
        
        start_time = time.time()
        
        # Perform many calculations
        for i in range(10000):
            self.calc.add(i, i + 1)
            self.calc.multiply(i, 2)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Assert that operations complete within reasonable time
        self.assertLess(execution_time, 1.0, "Calculations took too long")

# ===== DOCTEST EXAMPLES =====

def doctest_example():
    """
    Example function with doctests.
    
    >>> doctest_example()
    'Hello from doctest!'
    
    >>> len(doctest_example())
    18
    """
    return "Hello from doctest!"

def fibonacci(n):
    """
    Calculate fibonacci number.
    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ===== TEST RUNNERS AND MAIN =====

def run_unittest_examples():
    """Run unittest examples."""
    print("=== RUNNING UNITTEST EXAMPLES ===")
    
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTest(unittest.makeSuite(TestCalculator))
    suite.addTest(unittest.makeSuite(TestBankAccount))
    suite.addTest(unittest.makeSuite(TestFileProcessor))
    suite.addTest(unittest.makeSuite(IntegrationTestBankSystem))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print(f"\nTests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

def run_doctest_examples():
    """Run doctest examples."""
    print("\n=== RUNNING DOCTEST EXAMPLES ===")
    
    # Test Calculator class doctests
    print("Testing Calculator doctests:")
    doctest.testmod(verbose=True)
    
    # Test specific functions
    print("\nTesting individual functions:")
    doctest.run_docstring_examples(doctest_example, globals(), verbose=True)
    doctest.run_docstring_examples(fibonacci, globals(), verbose=True)

def main():
    """Main function to demonstrate testing concepts."""
    print("PYTHON TESTING EXAMPLES")
    print("=" * 50)
    
    print("Testing frameworks and concepts covered:")
    print("✓ unittest - Python's built-in testing framework")
    print("✓ pytest - Popular third-party testing framework")
    print("✓ Mock objects and patching")
    print("✓ Fixtures and test setup/teardown")
    print("✓ Parametrized tests")
    print("✓ Integration tests")
    print("✓ Performance tests")
    print("✓ Doctests")
    print("✓ Exception testing")
    print("✓ File and I/O testing")
    
    # Run examples
    run_unittest_examples()
    run_doctest_examples()
    
    print("\n" + "=" * 50)
    print("TESTING BEST PRACTICES")
    print("=" * 50)
    print("1. Write tests before or alongside your code (TDD)")
    print("2. Test edge cases and error conditions")
    print("3. Use meaningful test names that describe what's being tested")
    print("4. Keep tests simple and focused on one thing")
    print("5. Use fixtures for common test setup")
    print("6. Mock external dependencies")
    print("7. Aim for high test coverage but focus on critical paths")
    print("8. Run tests frequently during development")
    print("9. Use continuous integration to run tests automatically")
    print("10. Refactor tests when refactoring code")
    
    print("\nTesting commands:")
    print("- Run unittest: python -m unittest test_module.py")
    print("- Run pytest: pytest test_module.py")
    print("- Run with coverage: pytest --cov=module_name")
    print("- Run doctests: python -m doctest module.py -v")

if __name__ == "__main__":
    main()