"""
Flask Web Development - Basic Web Applications
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import json
import os

# Create Flask application
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Sample data storage (in production, use a database)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics"},
    {"id": 2, "name": "Book", "price": 19.99, "category": "Education"},
    {"id": 3, "name": "Coffee", "price": 4.99, "category": "Food"}
]

# Basic route
@app.route('/')
def home():
    """Home page route."""
    return '''
    <h1>Welcome to Python Flask Demo!</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="/users">View Users</a></li>
        <li><a href="/products">View Products</a></li>
        <li><a href="/api/users">Users API</a></li>
        <li><a href="/api/products">Products API</a></li>
        <li><a href="/form">Sample Form</a></li>
    </ul>
    '''

# Route with template
@app.route('/users')
def show_users():
    """Display users page."""
    html = '''
    <h1>Users</h1>
    <table border="1">
        <tr><th>ID</th><th>Name</th><th>Email</th></tr>
    '''
    for user in users:
        html += f'<tr><td>{user["id"]}</td><td>{user["name"]}</td><td>{user["email"]}</td></tr>'
    html += '</table><br><a href="/">Back to Home</a>'
    return html

# Route with URL parameters
@app.route('/user/<int:user_id>')
def show_user(user_id):
    """Display specific user."""
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return f'''
        <h1>User Details</h1>
        <p><strong>ID:</strong> {user["id"]}</p>
        <p><strong>Name:</strong> {user["name"]}</p>
        <p><strong>Email:</strong> {user["email"]}</p>
        <a href="/users">Back to Users</a>
        '''
    else:
        return '<h1>User not found</h1><a href="/users">Back to Users</a>', 404

# Route with query parameters
@app.route('/products')
def show_products():
    """Display products with optional filtering."""
    category = request.args.get('category')
    filtered_products = products
    
    if category:
        filtered_products = [p for p in products if p["category"].lower() == category.lower()]
    
    html = f'''
    <h1>Products{f" - {category}" if category else ""}</h1>
    <p>Filter by category: 
        <a href="/products?category=Electronics">Electronics</a> | 
        <a href="/products?category=Education">Education</a> | 
        <a href="/products?category=Food">Food</a> | 
        <a href="/products">All</a>
    </p>
    <table border="1">
        <tr><th>ID</th><th>Name</th><th>Price</th><th>Category</th></tr>
    '''
    
    for product in filtered_products:
        html += f'''<tr>
            <td>{product["id"]}</td>
            <td>{product["name"]}</td>
            <td>${product["price"]}</td>
            <td>{product["category"]}</td>
        </tr>'''
    
    html += '</table><br><a href="/">Back to Home</a>'
    return html

# API routes (JSON responses)
@app.route('/api/users')
def api_users():
    """API endpoint for users."""
    return jsonify(users)

@app.route('/api/users/<int:user_id>')
def api_user(user_id):
    """API endpoint for specific user."""
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/api/products')
def api_products():
    """API endpoint for products."""
    category = request.args.get('category')
    filtered_products = products
    
    if category:
        filtered_products = [p for p in products if p["category"].lower() == category.lower()]
    
    return jsonify(filtered_products)

# Form handling
@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    """Handle form submission."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In production, save to database
        new_user = {
            "id": len(users) + 1,
            "name": name,
            "email": email,
            "message": message
        }
        
        return f'''
        <h1>Form Submitted Successfully!</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Message:</strong> {message}</p>
        <a href="/form">Submit Another</a> | <a href="/">Home</a>
        '''
    
    # GET request - show form
    return '''
    <h1>Contact Form</h1>
    <form method="POST">
        <p>
            <label for="name">Name:</label><br>
            <input type="text" name="name" required>
        </p>
        <p>
            <label for="email">Email:</label><br>
            <input type="email" name="email" required>
        </p>
        <p>
            <label for="message">Message:</label><br>
            <textarea name="message" rows="4" cols="50" required></textarea>
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <a href="/">Back to Home</a>
    '''

# Session management
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Simple login system."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple authentication (in production, use proper authentication)
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return '''
            <h1>Login Failed</h1>
            <p>Invalid credentials. Try admin/password</p>
            <a href="/login">Try Again</a>
            '''
    
    return '''
    <h1>Login</h1>
    <form method="POST">
        <p>
            <label for="username">Username:</label><br>
            <input type="text" name="username" required>
        </p>
        <p>
            <label for="password">Password:</label><br>
            <input type="password" name="password" required>
        </p>
        <p>
            <input type="submit" value="Login">
        </p>
    </form>
    <p><em>Hint: Try admin/password</em></p>
    <a href="/">Back to Home</a>
    '''

@app.route('/dashboard')
def dashboard():
    """Dashboard for logged-in users."""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return f'''
    <h1>Welcome to Dashboard, {session['username']}!</h1>
    <p>You are successfully logged in.</p>
    <ul>
        <li><a href="/users">Manage Users</a></li>
        <li><a href="/products">Manage Products</a></li>
        <li><a href="/api/users">View Users API</a></li>
    </ul>
    <p><a href="/logout">Logout</a></p>
    '''

@app.route('/logout')
def logout():
    """Logout user."""
    session.pop('username', None)
    return '''
    <h1>Logged Out</h1>
    <p>You have been successfully logged out.</p>
    <a href="/">Home</a> | <a href="/login">Login Again</a>
    '''

# REST API with different HTTP methods
@app.route('/api/users', methods=['POST'])
def create_user():
    """Create new user via API."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required"}), 400
    
    new_user = {
        "id": len(users) + 1,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user via API."""
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if data:
        user.update(data)
    
    return jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete user via API."""
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully"})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return '''
    <h1>Page Not Found</h1>
    <p>The page you're looking for doesn't exist.</p>
    <a href="/">Go Home</a>
    ''', 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return '''
    <h1>Internal Server Error</h1>
    <p>Something went wrong on our end.</p>
    <a href="/">Go Home</a>
    ''', 500

# Template with Jinja2 (if templates directory exists)
@app.route('/template-demo')
def template_demo():
    """Demonstrate template rendering."""
    # Simple inline template
    template_content = '''
    <h1>Template Demo</h1>
    <p>Current user count: {{ user_count }}</p>
    <p>Product count: {{ product_count }}</p>
    <h3>Users:</h3>
    <ul>
    {% for user in users %}
        <li>{{ user.name }} ({{ user.email }})</li>
    {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
    '''
    
    from flask import render_template_string
    return render_template_string(
        template_content,
        users=users,
        user_count=len(users),
        product_count=len(products)
    )

if __name__ == '__main__':
    print("Starting Flask Web Application...")
    print("Available at: http://127.0.0.1:5000")
    print("\nEndpoints:")
    print("- / : Home page")
    print("- /users : View all users")
    print("- /user/<id> : View specific user")
    print("- /products : View products (with optional category filter)")
    print("- /api/users : Users API (supports GET, POST)")
    print("- /api/users/<id> : User API (supports GET, PUT, DELETE)")
    print("- /form : Contact form")
    print("- /login : Login page")
    print("- /dashboard : Protected dashboard")
    print("- /template-demo : Template demonstration")
    print("\nNote: This is a demo application. Run with 'python flask_basics.py'")
    
    # In production, don't use debug=True
    app.run(debug=True, host='127.0.0.1', port=5000)