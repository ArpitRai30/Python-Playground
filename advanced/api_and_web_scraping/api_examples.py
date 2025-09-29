"""
API Development and Web Scraping in Python
"""

import requests
import json
import time
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET
from datetime import datetime

# ===== REST API CONSUMPTION =====

class APIClient:
    """Simple API client for making HTTP requests."""
    
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)
    
    def get(self, endpoint, params=None):
        """Make GET request."""
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None
    
    def post(self, endpoint, data=None, json_data=None):
        """Make POST request."""
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.post(url, data=data, json=json_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None
    
    def put(self, endpoint, data=None, json_data=None):
        """Make PUT request."""
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.put(url, data=data, json=json_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            return None
    
    def delete(self, endpoint):
        """Make DELETE request."""
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.delete(url)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            return False

# JSONPlaceholder API examples
def jsonplaceholder_examples():
    """Demonstrate API consumption with JSONPlaceholder."""
    print("=== JSONPlaceholder API Examples ===")
    
    api = APIClient("https://jsonplaceholder.typicode.com/")
    
    # GET all posts
    print("\n1. Getting all posts (first 5):")
    posts = api.get("posts")
    if posts:
        for post in posts[:5]:
            print(f"  Post {post['id']}: {post['title'][:50]}...")
    
    # GET specific post
    print("\n2. Getting specific post:")
    post = api.get("posts/1")
    if post:
        print(f"  Title: {post['title']}")
        print(f"  Body: {post['body'][:100]}...")
    
    # GET post comments
    print("\n3. Getting post comments:")
    comments = api.get("posts/1/comments")
    if comments:
        print(f"  Found {len(comments)} comments")
        for comment in comments[:2]:
            print(f"  - {comment['name']} ({comment['email']})")
    
    # GET users
    print("\n4. Getting users:")
    users = api.get("users")
    if users:
        for user in users[:3]:
            print(f"  {user['name']} - {user['email']} ({user['address']['city']})")
    
    # POST new post
    print("\n5. Creating new post:")
    new_post_data = {
        "title": "My New Post",
        "body": "This is the content of my new post.",
        "userId": 1
    }
    created_post = api.post("posts", json_data=new_post_data)
    if created_post:
        print(f"  Created post with ID: {created_post['id']}")
    
    # PUT update post
    print("\n6. Updating post:")
    update_data = {
        "id": 1,
        "title": "Updated Post Title",
        "body": "Updated post content.",
        "userId": 1
    }
    updated_post = api.put("posts/1", json_data=update_data)
    if updated_post:
        print(f"  Updated post: {updated_post['title']}")

# Weather API example (OpenWeatherMap-like structure)
def weather_api_example():
    """Demonstrate weather API consumption."""
    print("\n=== Weather API Example ===")
    
    # Note: This is a mock example since we don't have a real API key
    # In real usage, you would sign up for an API key from OpenWeatherMap
    
    class WeatherAPI:
        def __init__(self, api_key):
            self.api_key = api_key
            self.base_url = "http://api.openweathermap.org/data/2.5/"
        
        def get_current_weather(self, city):
            """Get current weather for a city."""
            # This is a mock response for demonstration
            mock_response = {
                "name": city,
                "main": {
                    "temp": 22.5,
                    "feels_like": 24.0,
                    "humidity": 65,
                    "pressure": 1013
                },
                "weather": [
                    {
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d"
                    }
                ],
                "wind": {
                    "speed": 3.5,
                    "deg": 180
                }
            }
            return mock_response
        
        def get_forecast(self, city, days=5):
            """Get weather forecast."""
            # Mock forecast data
            forecasts = []
            base_temp = 20
            for i in range(days):
                forecasts.append({
                    "date": f"2024-01-{i+1:02d}",
                    "temp_max": base_temp + i,
                    "temp_min": base_temp + i - 5,
                    "description": "partly cloudy" if i % 2 else "sunny"
                })
            return {"forecasts": forecasts}
    
    # Demo usage
    weather = WeatherAPI("demo_api_key")
    
    print("Current weather for New York:")
    current = weather.get_current_weather("New York")
    print(f"  Temperature: {current['main']['temp']}°C")
    print(f"  Feels like: {current['main']['feels_like']}°C")
    print(f"  Weather: {current['weather'][0]['description']}")
    print(f"  Humidity: {current['main']['humidity']}%")
    
    print(f"\n5-day forecast for New York:")
    forecast = weather.get_forecast("New York")
    for day in forecast['forecasts']:
        print(f"  {day['date']}: {day['temp_max']}°C / {day['temp_min']}°C - {day['description']}")

# ===== WEB SCRAPING =====

def basic_web_scraping():
    """Demonstrate basic web scraping with requests."""
    print("\n=== Basic Web Scraping ===")
    
    try:
        # Scrape a simple webpage
        response = requests.get("https://httpbin.org/html")
        if response.status_code == 200:
            print("Successfully fetched webpage")
            print(f"Content length: {len(response.text)} characters")
            print("First 200 characters:")
            print(response.text[:200] + "...")
        else:
            print(f"Failed to fetch webpage: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")

def scrape_with_headers():
    """Demonstrate web scraping with custom headers."""
    print("\n=== Web Scraping with Headers ===")
    
    # Common headers to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    
    try:
        response = requests.get("https://httpbin.org/user-agent", headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f"User-Agent sent: {data['user-agent']}")
        
        # Demonstrate different response formats
        print("\nTesting different response formats:")
        
        # JSON response
        json_response = requests.get("https://httpbin.org/json")
        if json_response.status_code == 200:
            json_data = json_response.json()
            print(f"JSON data keys: {list(json_data.keys())}")
        
        # XML response (mock example)
        xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<books>
    <book id="1">
        <title>Python Programming</title>
        <author>John Doe</author>
        <price>29.99</price>
    </book>
    <book id="2">
        <title>Web Development</title>
        <author>Jane Smith</author>
        <price>39.99</price>
    </book>
</books>'''
        
        print("\nParsing XML data:")
        root = ET.fromstring(xml_content)
        for book in root.findall('book'):
            title = book.find('title').text
            author = book.find('author').text
            price = book.find('price').text
            print(f"  {title} by {author} - ${price}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error in web scraping: {e}")

def advanced_scraping_techniques():
    """Demonstrate advanced scraping techniques."""
    print("\n=== Advanced Scraping Techniques ===")
    
    # Session management
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Python Scraper 1.0'
    })
    
    # Rate limiting
    def rate_limited_request(url, delay=1):
        """Make request with rate limiting."""
        time.sleep(delay)
        return session.get(url)
    
    # Scraping with parameters
    print("1. Scraping with query parameters:")
    params = {
        'q': 'python programming',
        'format': 'json'
    }
    
    try:
        response = session.get("https://httpbin.org/get", params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"  URL with params: {data['url']}")
            print(f"  Query params: {data['args']}")
    except requests.exceptions.RequestException as e:
        print(f"  Error: {e}")
    
    # Handling forms and POST requests
    print("\n2. Handling forms (POST requests):")
    form_data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    
    try:
        response = session.post("https://httpbin.org/post", data=form_data)
        if response.status_code == 200:
            data = response.json()
            print(f"  Form data received: {data['form']}")
    except requests.exceptions.RequestException as e:
        print(f"  Error: {e}")
    
    # Handling cookies
    print("\n3. Cookie handling:")
    try:
        # Set a cookie
        response = session.get("https://httpbin.org/cookies/set/test_cookie/test_value")
        
        # Check cookies
        response = session.get("https://httpbin.org/cookies")
        if response.status_code == 200:
            data = response.json()
            print(f"  Cookies: {data['cookies']}")
    except requests.exceptions.RequestException as e:
        print(f"  Error: {e}")

# ===== API DEVELOPMENT =====

class SimpleAPIServer:
    """Simple API server implementation using Flask-like structure."""
    
    def __init__(self):
        self.routes = {}
        self.data = {
            'books': [
                {'id': 1, 'title': 'Python Programming', 'author': 'John Doe', 'year': 2023},
                {'id': 2, 'title': 'Web Development', 'author': 'Jane Smith', 'year': 2022},
                {'id': 3, 'title': 'Data Science', 'author': 'Bob Johnson', 'year': 2024}
            ]
        }
    
    def route(self, path, methods=['GET']):
        """Decorator to register routes."""
        def decorator(func):
            self.routes[path] = {'func': func, 'methods': methods}
            return func
        return decorator
    
    def get_books(self):
        """Get all books."""
        return {'books': self.data['books'], 'total': len(self.data['books'])}
    
    def get_book(self, book_id):
        """Get specific book."""
        book = next((b for b in self.data['books'] if b['id'] == book_id), None)
        if book:
            return {'book': book}
        else:
            return {'error': 'Book not found'}, 404
    
    def create_book(self, book_data):
        """Create new book."""
        new_id = max(b['id'] for b in self.data['books']) + 1
        new_book = {
            'id': new_id,
            'title': book_data.get('title', ''),
            'author': book_data.get('author', ''),
            'year': book_data.get('year', datetime.now().year)
        }
        self.data['books'].append(new_book)
        return {'book': new_book, 'message': 'Book created successfully'}, 201
    
    def update_book(self, book_id, book_data):
        """Update existing book."""
        book = next((b for b in self.data['books'] if b['id'] == book_id), None)
        if book:
            book.update(book_data)
            return {'book': book, 'message': 'Book updated successfully'}
        else:
            return {'error': 'Book not found'}, 404
    
    def delete_book(self, book_id):
        """Delete book."""
        book = next((b for b in self.data['books'] if b['id'] == book_id), None)
        if book:
            self.data['books'].remove(book)
            return {'message': 'Book deleted successfully'}
        else:
            return {'error': 'Book not found'}, 404

def api_server_demo():
    """Demonstrate API server functionality."""
    print("\n=== API Server Demo ===")
    
    server = SimpleAPIServer()
    
    print("1. Get all books:")
    result = server.get_books()
    print(f"  Total books: {result['total']}")
    for book in result['books']:
        print(f"  - {book['title']} by {book['author']} ({book['year']})")
    
    print("\n2. Get specific book:")
    result = server.get_book(1)
    if 'book' in result:
        book = result['book']
        print(f"  Found: {book['title']} by {book['author']}")
    
    print("\n3. Create new book:")
    new_book_data = {
        'title': 'Machine Learning Basics',
        'author': 'Alice Brown',
        'year': 2024
    }
    result, status = server.create_book(new_book_data)
    print(f"  {result['message']}")
    print(f"  Created: {result['book']['title']} (ID: {result['book']['id']})")
    
    print("\n4. Update book:")
    update_data = {'year': 2025}
    result = server.update_book(1, update_data)
    if 'book' in result:
        print(f"  {result['message']}")
        print(f"  Updated year to: {result['book']['year']}")
    
    print("\n5. Delete book:")
    result = server.delete_book(2)
    print(f"  {result['message']}")
    
    print("\n6. Final book list:")
    result = server.get_books()
    for book in result['books']:
        print(f"  - {book['title']} by {book['author']} ({book['year']})")

# ===== ERROR HANDLING AND BEST PRACTICES =====

def api_error_handling():
    """Demonstrate API error handling best practices."""
    print("\n=== API Error Handling ===")
    
    def safe_api_request(url, timeout=5, retries=3):
        """Make API request with error handling and retries."""
        for attempt in range(retries):
            try:
                response = requests.get(url, timeout=timeout)
                
                # Check for HTTP errors
                response.raise_for_status()
                
                # Try to parse JSON
                try:
                    return response.json()
                except json.JSONDecodeError:
                    return {'error': 'Invalid JSON response'}
                
            except requests.exceptions.Timeout:
                print(f"  Attempt {attempt + 1}: Request timed out")
            except requests.exceptions.ConnectionError:
                print(f"  Attempt {attempt + 1}: Connection error")
            except requests.exceptions.HTTPError as e:
                print(f"  Attempt {attempt + 1}: HTTP error {e.response.status_code}")
                break  # Don't retry for HTTP errors
            except requests.exceptions.RequestException as e:
                print(f"  Attempt {attempt + 1}: Request failed: {e}")
            
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
        
        return {'error': 'Request failed after all retries'}
    
    # Test with various URLs
    test_urls = [
        "https://httpbin.org/json",  # Should work
        "https://httpbin.org/status/404",  # Will return 404
        "https://httpbin.org/delay/10",  # Will timeout
        "https://nonexistent-domain-12345.com",  # Connection error
    ]
    
    for url in test_urls:
        print(f"\nTesting: {url}")
        result = safe_api_request(url)
        if 'error' in result:
            print(f"  Error: {result['error']}")
        else:
            print(f"  Success: Got response with {len(result)} keys")

# ===== MAIN DEMONSTRATION =====

def main():
    """Main demonstration of API and web scraping concepts."""
    print("API DEVELOPMENT AND WEB SCRAPING EXAMPLES")
    print("=" * 50)
    
    # API consumption examples
    jsonplaceholder_examples()
    weather_api_example()
    
    # Web scraping examples
    basic_web_scraping()
    scrape_with_headers()
    advanced_scraping_techniques()
    
    # API development
    api_server_demo()
    
    # Error handling
    api_error_handling()
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print("✓ API consumption with requests")
    print("✓ RESTful API design patterns")
    print("✓ Web scraping techniques")
    print("✓ Error handling and retries")
    print("✓ Rate limiting and headers")
    print("✓ Session management")
    print("✓ Data parsing (JSON, XML)")
    print("\nIMPORTANT NOTES:")
    print("- Always respect robots.txt and rate limits")
    print("- Use proper headers to identify your scraper")
    print("- Handle errors gracefully")
    print("- Consider using APIs instead of scraping when available")
    print("- Be mindful of terms of service")

if __name__ == "__main__":
    main()