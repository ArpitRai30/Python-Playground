"""
Beginner Python Projects - Simple and Educational
"""

import random
import time
import os
from datetime import datetime

# ===== PROJECT 1: NUMBER GUESSING GAME =====

def number_guessing_game():
    """Simple number guessing game."""
    print("=== NUMBER GUESSING GAME ===")
    print("I'm thinking of a number between 1 and 100!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try higher.")
            elif guess > secret_number:
                print("Too high! Try lower.")
            else:
                print(f"🎉 Congratulations! You guessed {secret_number} in {attempts} attempts!")
                return
                
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    print(f"😞 Game over! The number was {secret_number}")

# ===== PROJECT 2: TO-DO LIST MANAGER =====

class TodoList:
    """Simple to-do list manager."""
    
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []
    
    def add_task(self, task):
        """Add a new task."""
        self.tasks.append({
            'id': len(self.tasks) + len(self.completed_tasks) + 1,
            'task': task,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        print(f"✅ Added task: {task}")
    
    def list_tasks(self):
        """List all pending tasks."""
        if not self.tasks:
            print("📝 No pending tasks!")
            return
        
        print("\n📋 PENDING TASKS:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['task']} (Created: {task['created']})")
    
    def complete_task(self, task_number):
        """Mark a task as completed."""
        if 1 <= task_number <= len(self.tasks):
            completed_task = self.tasks.pop(task_number - 1)
            completed_task['completed'] = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.completed_tasks.append(completed_task)
            print(f"✅ Completed: {completed_task['task']}")
        else:
            print("❌ Invalid task number!")
    
    def list_completed(self):
        """List completed tasks."""
        if not self.completed_tasks:
            print("🎯 No completed tasks yet!")
            return
        
        print("\n🎯 COMPLETED TASKS:")
        for task in self.completed_tasks:
            print(f"✅ {task['task']} (Completed: {task['completed']})")
    
    def delete_task(self, task_number):
        """Delete a pending task."""
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"🗑️ Deleted: {deleted_task['task']}")
        else:
            print("❌ Invalid task number!")

def todo_list_demo():
    """Demonstrate to-do list functionality."""
    print("\n=== TO-DO LIST MANAGER ===")
    
    todo = TodoList()
    
    # Demo operations
    todo.add_task("Learn Python basics")
    todo.add_task("Build a project")
    todo.add_task("Practice algorithms")
    todo.add_task("Read documentation")
    
    todo.list_tasks()
    
    print("\nCompleting some tasks...")
    todo.complete_task(1)  # Complete first task
    todo.complete_task(3)  # Complete third task (now second in list)
    
    todo.list_tasks()
    todo.list_completed()
    
    print("\nDeleting a task...")
    todo.delete_task(1)
    todo.list_tasks()

# ===== PROJECT 3: SIMPLE CALCULATOR =====

class SimpleCalculator:
    """Interactive calculator with history."""
    
    def __init__(self):
        self.history = []
    
    def calculate(self, expression):
        """Calculate mathematical expression."""
        try:
            result = eval(expression)
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def show_history(self):
        """Show calculation history."""
        if not self.history:
            print("📊 No calculations yet!")
            return
        
        print("\n📊 CALCULATION HISTORY:")
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
    
    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        print("🧹 History cleared!")

def calculator_demo():
    """Demonstrate calculator functionality."""
    print("\n=== SIMPLE CALCULATOR ===")
    
    calc = SimpleCalculator()
    
    # Demo calculations
    expressions = [
        "2 + 3",
        "10 * 5",
        "100 / 4",
        "2 ** 8",
        "(15 + 5) * 2",
        "25 % 7"
    ]
    
    print("Performing sample calculations:")
    for expr in expressions:
        result = calc.calculate(expr)
        print(f"{expr} = {result}")
    
    calc.show_history()

# ===== PROJECT 4: PASSWORD GENERATOR =====

class PasswordGenerator:
    """Generate secure passwords."""
    
    def __init__(self):
        self.lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digits = "0123456789"
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate_password(self, length=12, include_uppercase=True, 
                         include_digits=True, include_symbols=True):
        """Generate a random password."""
        if length < 4:
            return "Password length should be at least 4 characters"
        
        # Build character set
        chars = self.lowercase
        
        if include_uppercase:
            chars += self.uppercase
        if include_digits:
            chars += self.digits
        if include_symbols:
            chars += self.symbols
        
        # Generate password
        password = ''.join(random.choice(chars) for _ in range(length))
        
        return password
    
    def check_password_strength(self, password):
        """Check password strength."""
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Use at least 8 characters")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Include lowercase letters")
        
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Include uppercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Include numbers")
        
        if any(c in self.symbols for c in password):
            score += 1
        else:
            feedback.append("Include special characters")
        
        strength_levels = {
            5: "Very Strong 🔒",
            4: "Strong 🔐",
            3: "Medium 🔓",
            2: "Weak ⚠️",
            1: "Very Weak ❌",
            0: "Very Weak ❌"
        }
        
        return {
            'score': score,
            'strength': strength_levels[score],
            'feedback': feedback
        }

def password_generator_demo():
    """Demonstrate password generator."""
    print("\n=== PASSWORD GENERATOR ===")
    
    generator = PasswordGenerator()
    
    print("Generating different types of passwords:")
    
    # Different password types
    passwords = [
        ("Basic (lowercase only)", generator.generate_password(12, False, False, False)),
        ("With uppercase", generator.generate_password(12, True, False, False)),
        ("With numbers", generator.generate_password(12, True, True, False)),
        ("Full strength", generator.generate_password(12, True, True, True)),
        ("Short (8 chars)", generator.generate_password(8)),
        ("Long (20 chars)", generator.generate_password(20))
    ]
    
    for desc, password in passwords:
        strength = generator.check_password_strength(password)
        print(f"{desc}: {password}")
        print(f"  Strength: {strength['strength']}")
        if strength['feedback']:
            print(f"  Suggestions: {', '.join(strength['feedback'])}")
        print()

# ===== PROJECT 5: WORD FREQUENCY COUNTER =====

class WordFrequencyCounter:
    """Count word frequencies in text."""
    
    def __init__(self):
        self.stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'shall', 'can', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'
        }
    
    def clean_text(self, text):
        """Clean and normalize text."""
        import string
        # Remove punctuation and convert to lowercase
        text = text.lower()
        for punct in string.punctuation:
            text = text.replace(punct, ' ')
        return text
    
    def count_words(self, text, exclude_stop_words=True):
        """Count word frequencies."""
        cleaned_text = self.clean_text(text)
        words = cleaned_text.split()
        
        word_count = {}
        for word in words:
            word = word.strip()
            if word and (not exclude_stop_words or word not in self.stop_words):
                word_count[word] = word_count.get(word, 0) + 1
        
        return word_count
    
    def get_top_words(self, word_count, n=10):
        """Get top N most frequent words."""
        return sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:n]
    
    def analyze_text(self, text):
        """Perform complete text analysis."""
        word_count = self.count_words(text)
        total_words = sum(word_count.values())
        unique_words = len(word_count)
        
        return {
            'total_words': total_words,
            'unique_words': unique_words,
            'word_frequencies': word_count,
            'top_words': self.get_top_words(word_count)
        }

def word_frequency_demo():
    """Demonstrate word frequency counter."""
    print("\n=== WORD FREQUENCY COUNTER ===")
    
    counter = WordFrequencyCounter()
    
    sample_text = """
    Python is a high-level programming language. Python is known for its simplicity
    and readability. Many developers love Python because Python makes programming
    fun and productive. Python has a large community and extensive libraries.
    Learning Python is a great choice for beginners in programming.
    """
    
    print("Sample text:")
    print(sample_text.strip())
    
    analysis = counter.analyze_text(sample_text)
    
    print(f"\n📊 TEXT ANALYSIS:")
    print(f"Total words: {analysis['total_words']}")
    print(f"Unique words: {analysis['unique_words']}")
    
    print(f"\n🔝 TOP 10 WORDS:")
    for word, count in analysis['top_words']:
        print(f"{word}: {count}")

# ===== PROJECT 6: SIMPLE FILE ORGANIZER =====

class FileOrganizer:
    """Organize files by extension."""
    
    def __init__(self):
        self.file_types = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c']
        }
    
    def get_file_category(self, filename):
        """Determine file category based on extension."""
        ext = os.path.splitext(filename)[1].lower()
        
        for category, extensions in self.file_types.items():
            if ext in extensions:
                return category
        
        return 'others'
    
    def organize_files(self, directory_path, simulate=True):
        """Organize files in directory (simulation mode by default)."""
        if not os.path.exists(directory_path):
            return f"Directory {directory_path} does not exist"
        
        organization_plan = {}
        
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            if os.path.isfile(file_path):
                category = self.get_file_category(filename)
                
                if category not in organization_plan:
                    organization_plan[category] = []
                
                organization_plan[category].append(filename)
        
        return organization_plan
    
    def create_directory_structure(self, base_path, plan, simulate=True):
        """Create directory structure for organization."""
        actions = []
        
        for category, files in plan.items():
            category_path = os.path.join(base_path, category)
            
            if not simulate:
                os.makedirs(category_path, exist_ok=True)
            
            actions.append(f"Create directory: {category_path}")
            
            for filename in files:
                source = os.path.join(base_path, filename)
                destination = os.path.join(category_path, filename)
                
                if not simulate:
                    # In real implementation, use shutil.move()
                    pass
                
                actions.append(f"Move: {filename} -> {category}/{filename}")
        
        return actions

def file_organizer_demo():
    """Demonstrate file organizer."""
    print("\n=== FILE ORGANIZER ===")
    
    organizer = FileOrganizer()
    
    # Simulate a directory with various files
    sample_files = [
        "photo1.jpg", "document.pdf", "song.mp3", "video.mp4",
        "script.py", "webpage.html", "archive.zip", "data.csv",
        "image.png", "report.docx", "music.wav", "backup.tar.gz"
    ]
    
    print("Sample files to organize:")
    for file in sample_files:
        category = organizer.get_file_category(file)
        print(f"  {file} -> {category}")
    
    # Create organization plan
    organization_plan = {}
    for file in sample_files:
        category = organizer.get_file_category(file)
        if category not in organization_plan:
            organization_plan[category] = []
        organization_plan[category].append(file)
    
    print(f"\n📁 ORGANIZATION PLAN:")
    for category, files in organization_plan.items():
        print(f"{category.upper()}:")
        for file in files:
            print(f"  - {file}")

# ===== MAIN DEMO FUNCTION =====

def main():
    """Run all beginner project demos."""
    print("BEGINNER PYTHON PROJECTS")
    print("=" * 50)
    
    print("This module contains several beginner-friendly projects:")
    print("1. Number Guessing Game")
    print("2. To-Do List Manager")
    print("3. Simple Calculator")
    print("4. Password Generator")
    print("5. Word Frequency Counter")
    print("6. File Organizer")
    print()
    
    # Run all demos
    # Note: Skipping interactive game for demo
    # number_guessing_game()  # Uncomment for interactive play
    
    todo_list_demo()
    calculator_demo()
    password_generator_demo()
    word_frequency_demo()
    file_organizer_demo()
    
    print("\n" + "=" * 50)
    print("PROJECT IDEAS FOR PRACTICE")
    print("=" * 50)
    print("🎯 Easy Projects:")
    print("- Rock Paper Scissors game")
    print("- Temperature converter")
    print("- Random quote generator")
    print("- Simple quiz application")
    print("- Expense tracker")
    
    print("\n🎯 Intermediate Projects:")
    print("- Web scraper for news/weather")
    print("- URL shortener")
    print("- Basic web API")
    print("- Data visualization with matplotlib")
    print("- Chat bot with natural language processing")
    
    print("\n🎯 Tips for Project Success:")
    print("- Start small and build incrementally")
    print("- Focus on one feature at a time")
    print("- Test your code frequently")
    print("- Ask for feedback from others")
    print("- Document your code and process")
    print("- Share your projects on GitHub")

if __name__ == "__main__":
    main()