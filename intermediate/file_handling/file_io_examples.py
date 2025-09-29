"""
File Handling and I/O Operations in Python
"""

import os
import json
import csv
import pickle
from pathlib import Path
import tempfile
import shutil

# Create a temporary directory for our examples
temp_dir = "/tmp/file_examples"
os.makedirs(temp_dir, exist_ok=True)

# Basic file operations
print("=== BASIC FILE OPERATIONS ===")

# Writing to a file
def write_text_file():
    """Demonstrate writing to a text file."""
    file_path = os.path.join(temp_dir, "sample.txt")
    
    # Using with statement (recommended)
    with open(file_path, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a sample text file.\n")
        file.write("Python file handling is easy!\n")
    
    print(f"File written to: {file_path}")
    return file_path

# Reading from a file
def read_text_file(file_path):
    """Demonstrate reading from a text file."""
    print(f"\nReading from: {file_path}")
    
    # Read entire file
    with open(file_path, 'r') as file:
        content = file.read()
        print("Entire file content:")
        print(content)
    
    # Read line by line
    with open(file_path, 'r') as file:
        print("Line by line:")
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")
    
    # Read all lines into a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Total lines: {len(lines)}")

file_path = write_text_file()
read_text_file(file_path)

# File modes and operations
print("\n=== FILE MODES ===")

def demonstrate_file_modes():
    """Show different file opening modes."""
    file_path = os.path.join(temp_dir, "modes_demo.txt")
    
    # Write mode ('w') - overwrites existing content
    with open(file_path, 'w') as file:
        file.write("Initial content\n")
    
    # Append mode ('a') - adds to existing content
    with open(file_path, 'a') as file:
        file.write("Appended content\n")
        file.write("More appended content\n")
    
    # Read and print
    with open(file_path, 'r') as file:
        print("File after append:")
        print(file.read())
    
    # Read mode with different options
    with open(file_path, 'r') as file:
        print("First line only:", file.readline().strip())
    
    print(f"File created at: {file_path}")

demonstrate_file_modes()

# Working with CSV files
print("\n=== CSV FILE OPERATIONS ===")

def csv_operations():
    """Demonstrate CSV file operations."""
    csv_path = os.path.join(temp_dir, "employees.csv")
    
    # Sample employee data
    employees = [
        ['Name', 'Age', 'Department', 'Salary'],
        ['Alice', 30, 'Engineering', 75000],
        ['Bob', 25, 'Marketing', 55000],
        ['Charlie', 35, 'Engineering', 85000],
        ['Diana', 28, 'HR', 60000]
    ]
    
    # Writing CSV
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(employees)
    
    print(f"CSV file written to: {csv_path}")
    
    # Reading CSV
    print("Reading CSV file:")
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    
    # Reading CSV with DictReader
    print("\nReading CSV as dictionaries:")
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Name']}: {row['Department']}, ${row['Salary']}")
    
    # Writing CSV with DictWriter
    dict_csv_path = os.path.join(temp_dir, "products.csv")
    products = [
        {'name': 'Laptop', 'price': 999.99, 'category': 'Electronics'},
        {'name': 'Book', 'price': 19.99, 'category': 'Education'},
        {'name': 'Coffee', 'price': 4.99, 'category': 'Food'}
    ]
    
    with open(dict_csv_path, 'w', newline='') as file:
        fieldnames = ['name', 'price', 'category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
    
    print(f"Dictionary CSV written to: {dict_csv_path}")

csv_operations()

# Working with JSON files
print("\n=== JSON FILE OPERATIONS ===")

def json_operations():
    """Demonstrate JSON file operations."""
    json_path = os.path.join(temp_dir, "data.json")
    
    # Sample data
    data = {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ],
        "settings": {
            "theme": "dark",
            "notifications": True,
            "language": "en"
        },
        "metadata": {
            "version": "1.0",
            "created": "2024-01-01"
        }
    }
    
    # Writing JSON
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"JSON file written to: {json_path}")
    
    # Reading JSON
    with open(json_path, 'r') as file:
        loaded_data = json.load(file)
    
    print("Loaded JSON data:")
    print(f"Number of users: {len(loaded_data['users'])}")
    print(f"Theme: {loaded_data['settings']['theme']}")
    
    # Pretty print JSON
    print("\nPretty printed JSON:")
    print(json.dumps(loaded_data, indent=2))

json_operations()

# Binary file operations and Pickle
print("\n=== BINARY FILES AND PICKLE ===")

def binary_and_pickle_operations():
    """Demonstrate binary file operations and pickle."""
    
    # Working with pickle (serialization)
    pickle_path = os.path.join(temp_dir, "data.pickle")
    
    # Data to serialize
    complex_data = {
        'numbers': [1, 2, 3, 4, 5],
        'nested': {'a': 1, 'b': [2, 3]},
        'tuple_data': (10, 20, 30),
        'set_data': {1, 2, 3, 4, 5}
    }
    
    # Writing with pickle
    with open(pickle_path, 'wb') as file:
        pickle.dump(complex_data, file)
    
    print(f"Pickle file written to: {pickle_path}")
    
    # Reading with pickle
    with open(pickle_path, 'rb') as file:
        loaded_data = pickle.load(file)
    
    print("Loaded pickle data:")
    print(f"Numbers: {loaded_data['numbers']}")
    print(f"Set data: {loaded_data['set_data']}")
    
    # Binary file copy
    source_path = os.path.join(temp_dir, "source_binary.bin")
    dest_path = os.path.join(temp_dir, "dest_binary.bin")
    
    # Create binary file
    with open(source_path, 'wb') as file:
        file.write(b"This is binary data\x00\x01\x02\x03")
    
    # Copy binary file
    with open(source_path, 'rb') as src, open(dest_path, 'wb') as dst:
        dst.write(src.read())
    
    print(f"Binary file copied from {source_path} to {dest_path}")

binary_and_pickle_operations()

# File and directory operations
print("\n=== FILE AND DIRECTORY OPERATIONS ===")

def file_directory_operations():
    """Demonstrate file and directory operations."""
    
    # Create directory structure
    subdir = os.path.join(temp_dir, "subdir")
    os.makedirs(subdir, exist_ok=True)
    
    # Create some files
    for i in range(3):
        file_path = os.path.join(subdir, f"file_{i}.txt")
        with open(file_path, 'w') as file:
            file.write(f"Content of file {i}\n")
    
    # List directory contents
    print("Directory contents:")
    for item in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"File: {item} ({size} bytes)")
        elif os.path.isdir(item_path):
            print(f"Directory: {item}")
    
    # File information
    sample_file = os.path.join(temp_dir, "sample.txt")
    if os.path.exists(sample_file):
        stat = os.stat(sample_file)
        print(f"\nFile info for {sample_file}:")
        print(f"Size: {stat.st_size} bytes")
        print(f"Modified: {stat.st_mtime}")
        print(f"Is file: {os.path.isfile(sample_file)}")
        print(f"Is directory: {os.path.isdir(sample_file)}")
    
    # Using pathlib (modern approach)
    path = Path(temp_dir)
    print(f"\nUsing pathlib:")
    print(f"Directory exists: {path.exists()}")
    print(f"Is directory: {path.is_dir()}")
    
    # List files with pathlib
    txt_files = list(path.glob("*.txt"))
    print(f"Text files: {[f.name for f in txt_files]}")

file_directory_operations()

# Context managers and file handling
print("\n=== CONTEXT MANAGERS ===")

class FileManager:
    """Custom context manager for file operations."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()

# Using custom context manager
context_file = os.path.join(temp_dir, "context_example.txt")
with FileManager(context_file, 'w') as file:
    file.write("Using custom context manager\n")

# Exception handling with files
print("\n=== EXCEPTION HANDLING ===")

def safe_file_operations():
    """Demonstrate safe file operations with exception handling."""
    
    try:
        # Try to read a non-existent file
        with open("nonexistent_file.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found!")
    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Safe file reading with fallback
    def read_file_safe(filename, default=""):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except (FileNotFoundError, PermissionError):
            return default
    
    content = read_file_safe("nonexistent.txt", "Default content")
    print(f"Safe read result: {content}")

safe_file_operations()

# File operations with different encodings
print("\n=== FILE ENCODINGS ===")

def encoding_examples():
    """Demonstrate file operations with different encodings."""
    
    # Unicode text
    unicode_text = "Hello, 世界! 🌍 Ñoël café résumé"
    
    # Write with UTF-8 encoding
    utf8_file = os.path.join(temp_dir, "unicode_utf8.txt")
    with open(utf8_file, 'w', encoding='utf-8') as file:
        file.write(unicode_text)
    
    # Read with UTF-8 encoding
    with open(utf8_file, 'r', encoding='utf-8') as file:
        read_text = file.read()
        print(f"UTF-8 text: {read_text}")
    
    # Check file size and encoding
    file_size = os.path.getsize(utf8_file)
    print(f"File size: {file_size} bytes")

encoding_examples()

# Cleanup information
print(f"\n=== FILES CREATED ===")
print(f"All example files created in: {temp_dir}")
print("Contents:")
for root, dirs, files in os.walk(temp_dir):
    level = root.replace(temp_dir, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)
        print(f"{subindent}{file} ({size} bytes)")

print(f"\nNote: Files are in temporary directory {temp_dir}")
print("These files will persist for this session but may be cleaned up automatically.")