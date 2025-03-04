import mysql.connector

# Database connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="password",  # Replace with your MySQL password
        database="library_db"  # Replace with your database name
    )

# Create database and tables if they don't exist
def initialize_database():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
    cursor.execute("USE library_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            isbn VARCHAR(20) UNIQUE NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Book Operations
def add_book(title, author, isbn):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)", (title, author, isbn))
    conn.commit()
    cursor.close()
    conn.close()
    print("Book added successfully!")

def view_books():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
    cursor.close()
    conn.close()

def update_book(book_id, title, author, isbn):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = %s, author = %s, isbn = %s WHERE id = %s", (title, author, isbn, book_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Book updated successfully!")

def delete_book(book_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Book deleted successfully!")

# Member Operations
def add_member(name, email):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    print("Member added successfully!")

def view_members():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    for member in members:
        print(f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}")
    cursor.close()
    conn.close()

def update_member(member_id, name, email):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("UPDATE members SET name = %s, email = %s WHERE id = %s", (name, email, member_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Member updated successfully!")

def delete_member(member_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE id = %s", (member_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Member deleted successfully!")

# Main Menu
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Book Operations")
        print("2. Member Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_operations()
        elif choice == "2":
            member_operations()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Book Operations Menu
def book_operations():
    while True:
        print("\nBook Operations")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            add_book(title, author, isbn)
        elif choice == "2":
            view_books()
        elif choice == "3":
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            isbn = input("Enter new ISBN: ")
            update_book(book_id, title, author, isbn)
        elif choice == "4":
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Member Operations Menu
def member_operations():
    while True:
        print("\nMember Operations")
        print("1. Add Member")
        print("2. View Members")
        print("3. Update Member")
        print("4. Delete Member")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            add_member(name, email)
        elif choice == "2":
            view_members()
        elif choice == "3":
            member_id = input("Enter member ID to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            update_member(member_id, name, email)
        elif choice == "4":
            member_id = input("Enter member ID to delete: ")
            delete_member(member_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Entry Point
if __name__ == "__main__":
    initialize_database()
    main_menu()