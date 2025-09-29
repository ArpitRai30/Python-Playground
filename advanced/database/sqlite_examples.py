"""
Database Interaction with Python - SQLite and SQL Examples
"""

import sqlite3
import os
from datetime import datetime, date
import json

# Create database file path
db_path = "/tmp/example_database.db"

# Database setup and connection
def create_connection():
    """Create database connection."""
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign keys
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_tables():
    """Create database tables."""
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1
            )
        ''')
        
        # Categories table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            )
        ''')
        
        # Products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price DECIMAL(10, 2) NOT NULL,
                category_id INTEGER,
                stock_quantity INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (category_id) REFERENCES categories (id)
            )
        ''')
        
        # Orders table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                total_amount DECIMAL(10, 2) NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Order items table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')
        
        conn.commit()
        print("Tables created successfully!")
        
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        conn.close()

# CRUD Operations
class UserDatabase:
    """Class for user database operations."""
    
    @staticmethod
    def insert_user(username, email, password_hash):
        """Insert new user."""
        conn = create_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, email, password_hash)
                VALUES (?, ?, ?)
            ''', (username, email, password_hash))
            
            user_id = cursor.lastrowid
            conn.commit()
            return user_id
            
        except sqlite3.Error as e:
            print(f"Error inserting user: {e}")
            return None
        finally:
            conn.close()
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID."""
        conn = create_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            return cursor.fetchone()
            
        except sqlite3.Error as e:
            print(f"Error getting user: {e}")
            return None
        finally:
            conn.close()
    
    @staticmethod
    def get_all_users():
        """Get all users."""
        conn = create_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users ORDER BY created_at DESC')
            return cursor.fetchall()
            
        except sqlite3.Error as e:
            print(f"Error getting users: {e}")
            return []
        finally:
            conn.close()
    
    @staticmethod
    def update_user(user_id, **kwargs):
        """Update user fields."""
        conn = create_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            
            # Build dynamic update query
            set_clause = ', '.join([f"{key} = ?" for key in kwargs.keys()])
            values = list(kwargs.values()) + [user_id]
            
            cursor.execute(f'''
                UPDATE users SET {set_clause}
                WHERE id = ?
            ''', values)
            
            conn.commit()
            return cursor.rowcount > 0
            
        except sqlite3.Error as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def delete_user(user_id):
        """Delete user."""
        conn = create_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()
            return cursor.rowcount > 0
            
        except sqlite3.Error as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            conn.close()

class ProductDatabase:
    """Class for product database operations."""
    
    @staticmethod
    def insert_category(name, description=None):
        """Insert new category."""
        conn = create_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO categories (name, description)
                VALUES (?, ?)
            ''', (name, description))
            
            category_id = cursor.lastrowid
            conn.commit()
            return category_id
            
        except sqlite3.Error as e:
            print(f"Error inserting category: {e}")
            return None
        finally:
            conn.close()
    
    @staticmethod
    def insert_product(name, description, price, category_id, stock_quantity=0):
        """Insert new product."""
        conn = create_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO products (name, description, price, category_id, stock_quantity)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, description, price, category_id, stock_quantity))
            
            product_id = cursor.lastrowid
            conn.commit()
            return product_id
            
        except sqlite3.Error as e:
            print(f"Error inserting product: {e}")
            return None
        finally:
            conn.close()
    
    @staticmethod
    def get_products_with_categories():
        """Get products with category information."""
        conn = create_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.id, p.name, p.description, p.price, p.stock_quantity,
                       c.name as category_name, c.description as category_description
                FROM products p
                LEFT JOIN categories c ON p.category_id = c.id
                ORDER BY p.name
            ''')
            return cursor.fetchall()
            
        except sqlite3.Error as e:
            print(f"Error getting products: {e}")
            return []
        finally:
            conn.close()
    
    @staticmethod
    def search_products(search_term):
        """Search products by name or description."""
        conn = create_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.*, c.name as category_name
                FROM products p
                LEFT JOIN categories c ON p.category_id = c.id
                WHERE p.name LIKE ? OR p.description LIKE ?
                ORDER BY p.name
            ''', (f'%{search_term}%', f'%{search_term}%'))
            return cursor.fetchall()
            
        except sqlite3.Error as e:
            print(f"Error searching products: {e}")
            return []
        finally:
            conn.close()

class OrderDatabase:
    """Class for order database operations."""
    
    @staticmethod
    def create_order(user_id, items):
        """Create order with items."""
        conn = create_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            
            # Calculate total amount
            total_amount = sum(item['price'] * item['quantity'] for item in items)
            
            # Insert order
            cursor.execute('''
                INSERT INTO orders (user_id, total_amount)
                VALUES (?, ?)
            ''', (user_id, total_amount))
            
            order_id = cursor.lastrowid
            
            # Insert order items
            for item in items:
                cursor.execute('''
                    INSERT INTO order_items (order_id, product_id, quantity, price)
                    VALUES (?, ?, ?, ?)
                ''', (order_id, item['product_id'], item['quantity'], item['price']))
            
            conn.commit()
            return order_id
            
        except sqlite3.Error as e:
            print(f"Error creating order: {e}")
            conn.rollback()
            return None
        finally:
            conn.close()
    
    @staticmethod
    def get_user_orders(user_id):
        """Get orders for a user."""
        conn = create_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT o.id, o.total_amount, o.order_date, o.status,
                       COUNT(oi.id) as item_count
                FROM orders o
                LEFT JOIN order_items oi ON o.id = oi.order_id
                WHERE o.user_id = ?
                GROUP BY o.id
                ORDER BY o.order_date DESC
            ''', (user_id,))
            return cursor.fetchall()
            
        except sqlite3.Error as e:
            print(f"Error getting user orders: {e}")
            return []
        finally:
            conn.close()
    
    @staticmethod
    def get_order_details(order_id):
        """Get detailed order information."""
        conn = create_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            
            # Get order info
            cursor.execute('''
                SELECT o.*, u.username
                FROM orders o
                JOIN users u ON o.user_id = u.id
                WHERE o.id = ?
            ''', (order_id,))
            order = cursor.fetchone()
            
            if not order:
                return None
            
            # Get order items
            cursor.execute('''
                SELECT oi.*, p.name as product_name
                FROM order_items oi
                JOIN products p ON oi.product_id = p.id
                WHERE oi.order_id = ?
            ''', (order_id,))
            items = cursor.fetchall()
            
            return {
                'order': order,
                'items': items
            }
            
        except sqlite3.Error as e:
            print(f"Error getting order details: {e}")
            return None
        finally:
            conn.close()

# Advanced SQL queries
def advanced_queries():
    """Demonstrate advanced SQL queries."""
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        
        print("=== ADVANCED SQL QUERIES ===")
        
        # 1. Users with their order counts and total spent
        print("\n1. User Statistics:")
        cursor.execute('''
            SELECT u.username, u.email,
                   COUNT(o.id) as order_count,
                   COALESCE(SUM(o.total_amount), 0) as total_spent
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            GROUP BY u.id, u.username, u.email
            ORDER BY total_spent DESC
        ''')
        
        results = cursor.fetchall()
        for row in results:
            print(f"  {row[0]}: {row[2]} orders, ${row[3]:.2f} total")
        
        # 2. Top selling products
        print("\n2. Top Selling Products:")
        cursor.execute('''
            SELECT p.name, 
                   SUM(oi.quantity) as total_sold,
                   SUM(oi.quantity * oi.price) as revenue
            FROM products p
            JOIN order_items oi ON p.id = oi.product_id
            GROUP BY p.id, p.name
            ORDER BY total_sold DESC
            LIMIT 5
        ''')
        
        results = cursor.fetchall()
        for row in results:
            print(f"  {row[0]}: {row[1]} units sold, ${row[2]:.2f} revenue")
        
        # 3. Categories with product counts and average prices
        print("\n3. Category Analysis:")
        cursor.execute('''
            SELECT c.name as category,
                   COUNT(p.id) as product_count,
                   AVG(p.price) as avg_price,
                   MIN(p.price) as min_price,
                   MAX(p.price) as max_price
            FROM categories c
            LEFT JOIN products p ON c.id = p.category_id
            GROUP BY c.id, c.name
            ORDER BY product_count DESC
        ''')
        
        results = cursor.fetchall()
        for row in results:
            print(f"  {row[0]}: {row[1]} products, avg ${row[2]:.2f}")
        
        # 4. Monthly sales report
        print("\n4. Sales by Month:")
        cursor.execute('''
            SELECT strftime('%Y-%m', order_date) as month,
                   COUNT(*) as order_count,
                   SUM(total_amount) as total_sales
            FROM orders
            GROUP BY strftime('%Y-%m', order_date)
            ORDER BY month DESC
        ''')
        
        results = cursor.fetchall()
        for row in results:
            print(f"  {row[0]}: {row[1]} orders, ${row[2]:.2f} sales")
        
    except sqlite3.Error as e:
        print(f"Error running advanced queries: {e}")
    finally:
        conn.close()

# Database initialization with sample data
def initialize_sample_data():
    """Initialize database with sample data."""
    print("=== INITIALIZING DATABASE ===")
    
    # Create tables
    create_tables()
    
    # Insert sample categories
    cat1 = ProductDatabase.insert_category("Electronics", "Electronic devices and gadgets")
    cat2 = ProductDatabase.insert_category("Books", "Educational and entertainment books")
    cat3 = ProductDatabase.insert_category("Clothing", "Apparel and accessories")
    
    print(f"Created categories: {cat1}, {cat2}, {cat3}")
    
    # Insert sample users
    users_data = [
        ("john_doe", "john@example.com", "hashed_password_1"),
        ("jane_smith", "jane@example.com", "hashed_password_2"),
        ("alice_wilson", "alice@example.com", "hashed_password_3"),
    ]
    
    user_ids = []
    for username, email, password in users_data:
        user_id = UserDatabase.insert_user(username, email, password)
        user_ids.append(user_id)
    
    print(f"Created users: {user_ids}")
    
    # Insert sample products
    products_data = [
        ("Laptop", "High-performance laptop", 999.99, cat1, 10),
        ("Smartphone", "Latest smartphone", 599.99, cat1, 25),
        ("Python Book", "Learn Python programming", 29.99, cat2, 50),
        ("T-Shirt", "Comfortable cotton t-shirt", 19.99, cat3, 100),
        ("Jeans", "Classic blue jeans", 59.99, cat3, 30),
    ]
    
    product_ids = []
    for name, desc, price, category, stock in products_data:
        product_id = ProductDatabase.insert_product(name, desc, price, category, stock)
        product_ids.append(product_id)
    
    print(f"Created products: {product_ids}")
    
    # Create sample orders
    if user_ids and product_ids:
        # Order 1
        items1 = [
            {"product_id": product_ids[0], "quantity": 1, "price": 999.99},
            {"product_id": product_ids[2], "quantity": 2, "price": 29.99}
        ]
        order1 = OrderDatabase.create_order(user_ids[0], items1)
        
        # Order 2
        items2 = [
            {"product_id": product_ids[1], "quantity": 1, "price": 599.99},
            {"product_id": product_ids[3], "quantity": 3, "price": 19.99}
        ]
        order2 = OrderDatabase.create_order(user_ids[1], items2)
        
        print(f"Created orders: {order1}, {order2}")

# Main demonstration function
def demonstrate_database_operations():
    """Demonstrate all database operations."""
    print("=== DATABASE OPERATIONS DEMO ===")
    
    # Initialize with sample data
    initialize_sample_data()
    
    print("\n=== USERS ===")
    users = UserDatabase.get_all_users()
    for user in users:
        print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
    
    print("\n=== PRODUCTS WITH CATEGORIES ===")
    products = ProductDatabase.get_products_with_categories()
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: ${product[3]:.2f}, Category: {product[5]}")
    
    print("\n=== SEARCH PRODUCTS ===")
    search_results = ProductDatabase.search_products("python")
    for product in search_results:
        print(f"Found: {product[1]} - ${product[3]:.2f}")
    
    print("\n=== USER ORDERS ===")
    if users:
        user_orders = OrderDatabase.get_user_orders(users[0][0])
        for order in user_orders:
            print(f"Order ID: {order[0]}, Total: ${order[1]:.2f}, Items: {order[4]}")
    
    # Run advanced queries
    advanced_queries()
    
    print(f"\nDatabase file created at: {db_path}")

if __name__ == "__main__":
    demonstrate_database_operations()