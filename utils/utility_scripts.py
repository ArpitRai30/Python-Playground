"""
Python Utility Scripts and Tools
"""

import os
import sys
import json
import csv
import time
import shutil
import hashlib
import requests
from datetime import datetime, timedelta
import subprocess

# ===== SYSTEM UTILITIES =====

class SystemInfo:
    """Get system information."""
    
    @staticmethod
    def get_python_info():
        """Get Python version and path information."""
        return {
            'version': sys.version,
            'executable': sys.executable,
            'path': sys.path[:3],  # First 3 paths
            'platform': sys.platform
        }
    
    @staticmethod
    def get_disk_usage(path='.'):
        """Get disk usage information."""
        try:
            total, used, free = shutil.disk_usage(path)
            return {
                'total_gb': round(total / (1024**3), 2),
                'used_gb': round(used / (1024**3), 2),
                'free_gb': round(free / (1024**3), 2),
                'usage_percent': round((used / total) * 100, 2)
            }
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def get_env_info():
        """Get environment variables."""
        important_vars = ['PATH', 'HOME', 'USER', 'PYTHONPATH']
        env_info = {}
        
        for var in important_vars:
            env_info[var] = os.environ.get(var, 'Not set')
        
        return env_info

# ===== FILE UTILITIES =====

class FileUtils:
    """File manipulation utilities."""
    
    @staticmethod
    def find_files(directory, pattern="*", extension=None):
        """Find files matching pattern or extension."""
        import glob
        
        if extension:
            pattern = f"*.{extension.lstrip('.')}"
        
        search_pattern = os.path.join(directory, "**", pattern)
        return glob.glob(search_pattern, recursive=True)
    
    @staticmethod
    def get_file_hash(filepath, algorithm='md5'):
        """Get file hash."""
        hash_func = getattr(hashlib, algorithm)()
        
        try:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except Exception as e:
            return f"Error: {e}"
    
    @staticmethod
    def backup_file(filepath, backup_dir=None):
        """Create backup of file with timestamp."""
        if not os.path.exists(filepath):
            return f"File {filepath} does not exist"
        
        if backup_dir is None:
            backup_dir = os.path.dirname(filepath)
        
        os.makedirs(backup_dir, exist_ok=True)
        
        filename = os.path.basename(filepath)
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{name}_backup_{timestamp}{ext}"
        backup_path = os.path.join(backup_dir, backup_filename)
        
        try:
            shutil.copy2(filepath, backup_path)
            return backup_path
        except Exception as e:
            return f"Backup failed: {e}"
    
    @staticmethod
    def clean_directory(directory, days_old=7, dry_run=True):
        """Clean old files from directory."""
        cutoff_date = datetime.now() - timedelta(days=days_old)
        removed_files = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if file_time < cutoff_date:
                        if not dry_run:
                            os.remove(file_path)
                        removed_files.append(file_path)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
        
        return removed_files

# ===== NETWORK UTILITIES =====

class NetworkUtils:
    """Network-related utilities."""
    
    @staticmethod
    def check_website(url, timeout=5):
        """Check if website is accessible."""
        try:
            response = requests.get(url, timeout=timeout)
            return {
                'url': url,
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'accessible': response.status_code == 200
            }
        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'error': str(e),
                'accessible': False
            }
    
    @staticmethod
    def download_file(url, local_filename=None, chunk_size=8192):
        """Download file from URL."""
        if local_filename is None:
            local_filename = url.split('/')[-1]
        
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if total_size > 0:
                            percent = (downloaded / total_size) * 100
                            print(f"\rDownloading... {percent:.1f}%", end='')
            
            print(f"\nDownloaded: {local_filename}")
            return local_filename
        
        except Exception as e:
            return f"Download failed: {e}"
    
    @staticmethod
    def get_public_ip():
        """Get public IP address."""
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            return response.json()['ip']
        except Exception as e:
            return f"Error getting IP: {e}"

# ===== DATA UTILITIES =====

class DataUtils:
    """Data processing utilities."""
    
    @staticmethod
    def csv_to_json(csv_file, json_file=None):
        """Convert CSV to JSON."""
        if json_file is None:
            json_file = csv_file.replace('.csv', '.json')
        
        try:
            data = []
            with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)
            
            with open(json_file, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=2, ensure_ascii=False)
            
            return f"Converted {csv_file} to {json_file}"
        
        except Exception as e:
            return f"Conversion failed: {e}"
    
    @staticmethod
    def json_to_csv(json_file, csv_file=None):
        """Convert JSON to CSV."""
        if csv_file is None:
            csv_file = json_file.replace('.json', '.csv')
        
        try:
            with open(json_file, 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
            
            if not data:
                return "No data to convert"
            
            if not isinstance(data, list):
                data = [data]
            
            with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            
            return f"Converted {json_file} to {csv_file}"
        
        except Exception as e:
            return f"Conversion failed: {e}"
    
    @staticmethod
    def clean_text_data(text):
        """Clean text data."""
        import re
        import string
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Remove special characters (optional)
        # text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Convert to lowercase
        text = text.lower()
        
        return text
    
    @staticmethod
    def validate_email(email):
        """Simple email validation."""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

# ===== LOG UTILITIES =====

class LogUtils:
    """Logging utilities."""
    
    @staticmethod
    def setup_logger(name, log_file, level='INFO'):
        """Set up a logger."""
        import logging
        
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level.upper()))
        
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_format = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_format)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    @staticmethod
    def parse_log_file(log_file, pattern=None):
        """Parse log file and extract information."""
        import re
        
        results = []
        try:
            with open(log_file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    if pattern:
                        if re.search(pattern, line):
                            results.append({'line': line_num, 'content': line.strip()})
                    else:
                        results.append({'line': line_num, 'content': line.strip()})
            
            return results
        except Exception as e:
            return f"Error parsing log: {e}"

# ===== PERFORMANCE UTILITIES =====

class PerformanceUtils:
    """Performance monitoring utilities."""
    
    @staticmethod
    def time_function(func, *args, **kwargs):
        """Time function execution."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        return {
            'result': result,
            'execution_time': end_time - start_time,
            'function_name': func.__name__
        }
    
    @staticmethod
    def memory_usage():
        """Get memory usage information."""
        try:
            import psutil
            process = psutil.Process()
            memory_info = process.memory_info()
            
            return {
                'rss_mb': round(memory_info.rss / 1024 / 1024, 2),
                'vms_mb': round(memory_info.vms / 1024 / 1024, 2),
                'percent': process.memory_percent()
            }
        except ImportError:
            return "psutil not available - install with: pip install psutil"
    
    @staticmethod
    def profile_code(code_string, globals_dict=None):
        """Profile code execution."""
        import cProfile
        import io
        import pstats
        
        if globals_dict is None:
            globals_dict = {}
        
        profiler = cProfile.Profile()
        profiler.enable()
        
        try:
            exec(code_string, globals_dict)
        except Exception as e:
            return f"Error executing code: {e}"
        finally:
            profiler.disable()
        
        # Get stats
        stats_stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stats_stream)
        stats.sort_stats('cumulative')
        stats.print_stats(10)  # Top 10 functions
        
        return stats_stream.getvalue()

# ===== MAIN DEMONSTRATION =====

def demonstrate_utilities():
    """Demonstrate all utility functions."""
    print("PYTHON UTILITY SCRIPTS AND TOOLS")
    print("=" * 50)
    
    # System Information
    print("\n=== SYSTEM INFORMATION ===")
    sys_info = SystemInfo()
    
    python_info = sys_info.get_python_info()
    print(f"Python Version: {python_info['version'].split()[0]}")
    print(f"Python Executable: {python_info['executable']}")
    print(f"Platform: {python_info['platform']}")
    
    disk_info = sys_info.get_disk_usage('.')
    print(f"Disk Usage: {disk_info['used_gb']} GB / {disk_info['total_gb']} GB ({disk_info['usage_percent']}%)")
    
    # File Utilities
    print("\n=== FILE UTILITIES ===")
    file_utils = FileUtils()
    
    # Find Python files in current directory
    python_files = file_utils.find_files('.', extension='py')[:5]  # First 5
    print(f"Python files found: {len(python_files)}")
    for file in python_files:
        print(f"  - {os.path.basename(file)}")
    
    # Get hash of this file
    this_file = __file__
    if os.path.exists(this_file):
        file_hash = file_utils.get_file_hash(this_file)
        print(f"Hash of this file (MD5): {file_hash[:16]}...")
    
    # Network Utilities
    print("\n=== NETWORK UTILITIES ===")
    net_utils = NetworkUtils()
    
    # Check website accessibility
    test_sites = ['https://httpbin.org', 'https://python.org']
    for site in test_sites:
        result = net_utils.check_website(site)
        status = "✅" if result['accessible'] else "❌"
        print(f"{status} {site}: {result.get('status_code', 'Error')}")
    
    # Get public IP
    public_ip = net_utils.get_public_ip()
    print(f"Public IP: {public_ip}")
    
    # Data Utilities
    print("\n=== DATA UTILITIES ===")
    data_utils = DataUtils()
    
    # Test email validation
    test_emails = ['user@example.com', 'invalid-email', 'test@domain.org']
    for email in test_emails:
        valid = data_utils.validate_email(email)
        status = "✅" if valid else "❌"
        print(f"{status} {email}")
    
    # Clean text example
    dirty_text = "  Hello,    World!!!   This   is  MESSY   text.  "
    clean_text = data_utils.clean_text_data(dirty_text)
    print(f"Original: '{dirty_text}'")
    print(f"Cleaned:  '{clean_text}'")
    
    # Performance Utilities
    print("\n=== PERFORMANCE UTILITIES ===")
    perf_utils = PerformanceUtils()
    
    # Time a simple function
    def test_function():
        return sum(range(10000))
    
    timing_result = perf_utils.time_function(test_function)
    print(f"Function: {timing_result['function_name']}")
    print(f"Result: {timing_result['result']}")
    print(f"Execution time: {timing_result['execution_time']:.6f} seconds")
    
    # Memory usage
    memory_info = perf_utils.memory_usage()
    if isinstance(memory_info, dict):
        print(f"Memory usage: {memory_info['rss_mb']} MB ({memory_info['percent']:.1f}%)")
    else:
        print(f"Memory info: {memory_info}")
    
    print("\n" + "=" * 50)
    print("UTILITY SCRIPT USAGE EXAMPLES")
    print("=" * 50)
    print("📁 File operations:")
    print("  - Find all images: FileUtils.find_files('/path', extension='jpg')")
    print("  - Backup important file: FileUtils.backup_file('important.txt')")
    print("  - Clean old files: FileUtils.clean_directory('/tmp', days_old=30)")
    
    print("\n🌐 Network operations:")
    print("  - Check site status: NetworkUtils.check_website('https://example.com')")
    print("  - Download file: NetworkUtils.download_file('https://example.com/file.zip')")
    
    print("\n📊 Data processing:")
    print("  - Convert CSV to JSON: DataUtils.csv_to_json('data.csv')")
    print("  - Validate emails: DataUtils.validate_email('user@domain.com')")
    
    print("\n⚡ Performance monitoring:")
    print("  - Time functions: PerformanceUtils.time_function(my_function)")
    print("  - Profile code: PerformanceUtils.profile_code('your_code_here')")
    
    print("\n💡 Pro Tips:")
    print("  - Create shell scripts that call these utilities")
    print("  - Set up cron jobs for automated file cleaning")
    print("  - Use logging utilities for better debugging")
    print("  - Combine utilities to create powerful automation scripts")

if __name__ == "__main__":
    demonstrate_utilities()