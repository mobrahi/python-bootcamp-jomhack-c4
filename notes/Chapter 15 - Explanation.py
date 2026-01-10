import sqlite3

class DatabaseManager:
    def __init__(self, db_name="example.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Initialize database with tables"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            """)

# Explanation 1: This section initialises an SQLite database and creates tables if they do not already exist.
# It demonstrates how Python connects to a database, executes SQL CREATE statements, and defines table
# structures with primary keys, constraints, and relationships. This shows how databases are set up to
# store structured data persistently.

    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (name, email, age)
                    VALUES (?, ?, ?)
                """, (name, email, age))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return None

# Explanation 2: This section inserts a new user record into the database using an SQL INSERT statement.
# It uses parameterised queries to safely pass values into the database and handles potential errors
# such as duplicate entries using exception handling. This demonstrates how data can be added securely
# and reliably to a database table.

    def create_post(self, user_id, title, content):
        """Create a new post"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO posts (user_id, title, content)
                VALUES (?, ?, ?)
            """, (user_id, title, content))
            return cursor.lastrowid
        
# Explanation 3: This section inserts a new post record into the database and links it to an existing user
# through a foreign key. It demonstrates how related data can be stored across multiple tables while
# maintaining relationships between them. This shows how databases support structured and connected data.

    def get_all_users(self):
        """Get all users"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
        
# Explanation 4: This section retrieves all user records from the database using a SELECT statement.
# It connects to the SQLite database, executes a query to read all rows from the users table,
# and returns the results as a list. This demonstrates how stored data can be read from a database
# and used within a Python program.

    def get_user_posts(self, user_id):
        """Get posts by user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.id, p.title, p.content, p.created_at
                FROM posts p
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
            """, (user_id,))
            return cursor.fetchall()
        
# Explanation 5: This section retrieves all posts belonging to a specific user by filtering results
# using a WHERE condition. It demonstrates the use of parameterised SQL queries to safely pass
# values into a SELECT statement and shows how results can be ordered using ORDER BY.
# This demonstrates reading related data from multiple records.

    def delete_user(self, user_id):
        """Delete user and their posts"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM posts WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            return cursor.rowcount > 0
        
# Explanation 6: This section deletes a user and all related posts from the database.
# It first removes records from the posts table before deleting the user to maintain data consistency.
# This demonstrates how DELETE statements are used and how databases handle related data safely.

    def display_menu():
        """Display the main menu"""
        print("\n" + "=" * 40)
        print("DATABASE MANAGER")
        print("=" * 40)
        print("1. Create User")
        print("2. View All Users")
        print("3. Create Post")
        print("4. View User Posts")
        print("5. Delete User")
        print("6. Exit")
        print("=" * 40)

# Explanation 7: This section displays a text-based menu to the user in the terminal.
# It provides clear options for interacting with the database system and guides user input.
# This demonstrates how programs can use menus to improve usability in command-line applications.

    def main():
        """Main interactive CLI function"""
        db = DatabaseManager()

        while True:
            display_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                print("\n-- Create New User --")
                name = input("Enter name: ").strip()
                email = input("Enter email: ").strip()
                try:
                    age = int(input("Enter age: ").strip())
                    user_id = db.create_user(name, email, age)
                    if user_id:
                        print(f"✓ User created successfully! ID: {user_id}")
                    else:
                        print("✗ Failed to create user")
                except ValueError:
                    print("✗ Invalid age. Please enter a number.")

            elif choice == "2":
                print("\n-- All Users --")
                users = db.get_all_users()
                if users:
                    for user in users:
                        print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]} | Age: {user[3]}")
                else:
                    print("No users found.")

# Explanation 8: This section controls the main execution of the program using a loop.
# It repeatedly displays the menu, accepts user input, and calls the appropriate database functions.
# This demonstrates how multiple database operations can be combined into an interactive program
# that allows users to create, view, and manage data.

        elif choice == "3":
            print("\n-- Create New Post --")
            try:
                user_id = int(input("Enter user ID: ").strip())
                title = input("Enter post title: ").strip()
                content = input("Enter post content: ").strip()
                post_id = db.create_post(user_id, title, content)
                if post_id:
                    print(f"✓ Post created successfully! ID: {post_id}")
                else:
                    print("✗ Failed to create post")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")

        elif choice == "4":
            print("\n-- View User Posts --")
            try:
                user_id = int(input("Enter user ID: ").strip())
                posts = db.get_user_posts(user_id)
                if posts:
                    for post in posts:
                        print(f"Post ID: {post[0]}")
                        print(f"Title: {post[1]}")
                        print(f"Content: {post[2]}")
                        print(f"Created: {post[3]}")
                        print("-" * 30)
                else:
                    print("No posts found for this user.")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")

# Explanation 9: This section allows the user to create a new post for an existing user and to view all posts
# belonging to a specific user. It accepts user input, validates numeric values, and calls database methods
# to insert and retrieve data. The program then displays the retrieved records in a clear format, demonstrating
# how user interaction, input validation, and database queries work together in a practical application.

        elif choice == "5":
            print("\n-- Delete User --")
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                confirm = input("Are you sure you want to delete user (y/N): ").strip().lower()
                if confirm == "y":
                    if db.delete_user(user_id):
                        print("✓ User deleted successfully")
                    else:
                        print("✗ User not found or deletion failed")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")

        elif choice == "6":
            print("\nGoodbye! 👋")
            break

        else:
            print("✗ Invalid choice. Please enter 1-6.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
     main()

# Explanation 10: This section allows the user to delete a user and all associated data after confirmation.
# It also provides an option to exit the program safely. The code includes input validation, confirmation
# prompts, and proper program termination using a loop break. This demonstrates controlled program flow,
# safe data deletion, and clean program execution in a command-line database system.




# CHAPTER 15 - Student Learning Explanation

# MASTER EXPLANATION (SQLite Database Manager Program)
#
# This program demonstrates how Python can be used to build a complete database-driven application using SQLite,
# organised with a class-based (object-oriented) design. A DatabaseManager class is used to keep all database
# operations in one place. When an object of this class is created, it initialises the database file and creates
# the required tables (users and posts) if they do not already exist, ensuring the database structure is ready
# before any operations are performed.
#
# The program implements CRUD functionality. It can CREATE records by inserting new users and posts using SQL
# INSERT statements with parameterised queries (placeholders) so that values are passed safely into SQL. It can
# READ records using SELECT statements, either returning all users or returning posts for a particular user,
# demonstrating how related data is stored across tables using a foreign key (posts.user_id referencing users.id).
# It can DELETE records by removing a user and their associated posts, helping maintain data consistency.
#
# The program also includes input validation and error handling. Numeric inputs such as age and user_id are
# converted to integers inside try/except blocks so invalid inputs do not crash the program. Database constraints,
# such as unique emails, can trigger errors which are handled to keep the program robust.
#
# A text-based menu system runs in a loop in the terminal, allowing the user to choose actions such as creating
# a user, viewing all users, creating a post, viewing a user’s posts, deleting a user, or exiting. Each menu
# option calls the appropriate DatabaseManager method, showing how user interaction and database operations work
# together in a practical application. The program ends cleanly when the user chooses the exit option.