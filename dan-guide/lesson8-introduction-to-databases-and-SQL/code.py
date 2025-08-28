import sqlite3
import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

def wait():
    input("\nPress Enter to continue...\n")

#? Primary key vs Foreign KEY
#? Primary key = "this table’s unique ID"
#? Foreign key = "points to another table’s ID"

#! SECTION 1: Create SQLite Database and Tables
with sqlite3.connect("school_demo.db") as conn:
    #! this ensures that the FK exists or denies the insert.
    conn.execute("PRAGMA foreign_keys = 1") 
    cursor = conn.cursor()

    #? Drop tables if they already exist to start fresh each run
    cursor.execute("DROP TABLE IF EXISTS Enrollments")
    cursor.execute("DROP TABLE IF EXISTS Courses")
    cursor.execute("DROP TABLE IF EXISTS Students")
    cursor.execute("DROP TABLE IF EXISTS Accounts") 
    cursor.execute("DROP TABLE IF EXISTS Users") 

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL UNIQUE,
        instructor_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students (student_id),
        FOREIGN KEY (course_id) REFERENCES Courses (course_id)
    )
    """)

    print("Tables created successfully.")
wait()

#! SECTION 2: Insert Data with Helper Functions
def add_student(cursor, name, age, major):
    try:
        cursor.execute(
            "INSERT INTO Students (name, age, major) VALUES (?, ?, ?)",
            (name, age, major)
        )
        student_id = cursor.lastrowid
        print(f"Added student '{name}' (ID: {student_id})")
    except sqlite3.Error as e:
        print(f"Error adding student '{name}': {e}")

def add_course(cursor, course_name, instructor_name):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?, ?)", (course_name, instructor_name))
    except sqlite3.IntegrityError:
        print(f"Course '{course_name}' already exists.")

def enroll_student(cursor, student_id, course_id):
    cursor.execute("SELECT * FROM Students WHERE student_id = ?", (student_id,))
    if not cursor.fetchone():
        print(f"No student with ID {student_id}")
        return

    cursor.execute("SELECT * FROM Courses WHERE course_id = ?", (course_id,))
    if not cursor.fetchone():
        print(f"No course with ID {course_id}")
        return

    cursor.execute("""
        SELECT * FROM Enrollments
        WHERE student_id = ? AND course_id = ?
    """, (student_id, course_id))
    if cursor.fetchone():
        print(f"Student {student_id} is already enrolled in course {course_id}")
        return

    cursor.execute("""
        INSERT INTO Enrollments (student_id, course_id)
        VALUES (?, ?)
    """, (student_id, course_id))
    print(f"Student ID {student_id} enrolled in Course ID {course_id}")

with sqlite3.connect("school_demo.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Insert students and courses
    add_student(cursor, "Alice", 20, "Computer Science")
    add_student(cursor, "Bob", 19, "History")
    add_student(cursor, "Charlie", 19, "Biology")
    add_student(cursor, "Alice", 97, "Chemistry") #! duplicate name for demo to show PK FK importance
    add_student(cursor, "Daisy", 23, "Philosophy") #? NOT enrolled, for JOIN demo.

    add_course(cursor, "Math 101", "Dr. Smith")
    add_course(cursor, "English 101", "Ms. Jones")
    add_course(cursor, "Chemistry 101", "Dr. Lee")
    add_course(cursor, "Physics 101", "Dr. Brown")  #? No one enrolls in this

    conn.commit()
    print("Sample data inserted.")
wait()

#! SECTION 3: Enroll Students
with sqlite3.connect("school_demo.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    enroll_student(cursor, 1, 1)  # First Alice → Math 101
    enroll_student(cursor, 1, 3)  # First Alice → Chemistry 101
    enroll_student(cursor, 2, 1)  # Bob → Math 101
    enroll_student(cursor, 2, 2)  # Bob → English 101
    enroll_student(cursor, 3, 2)  # Charlie → English 101
    enroll_student(cursor, 4, 3)  # Second Alice  → Chemistry 101

    conn.commit()
wait()

#! SECTION 4: Query Data - Simple SELECTs
with sqlite3.connect("school_demo.db") as conn:
    cursor = conn.cursor()

    print("# All students:")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    print("\n# Students ordered by age:")
    #? cursor.execute("SELECT * FROM Students ORDER BY age DESC") default is ASC
    cursor.execute("SELECT * FROM Students ORDER BY age")
    for row in cursor.fetchall():
        print(row)
    
    print("\n# Courses taught by Dr. Smith:")
    cursor.execute("SELECT * FROM Courses WHERE instructor_name = 'Dr. Smith'")
    for row in cursor.fetchall():
        print(row)

wait()

#! SECTION 5: Complex Queries and Joins

with sqlite3.connect("school_demo.db") as conn:
    cursor = conn.cursor()

    #? INNER JOIN - Returns only rows where there is a match in BOTH tables.
    #? IE students who are enrolled in courses only. 
    print("\n# INNER JOIN: Students with enrolled courses")
    cursor.execute("""
        SELECT Students.name, Courses.course_name
        FROM Students
        INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id
        INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
    """)
    for row in cursor.fetchall():
        print(row)

    wait()

    #? 1 student per row. still an INNER join:
    print("\n# INNER JOIN: Students with enrolled courses 1 per row concat courses")
    cursor.execute("""
        SELECT Students.student_id, Students.name, GROUP_CONCAT(Courses.course_name, ', ') AS courses
        FROM Students
        INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id
        INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
        GROUP BY Students.student_id;
    """)
    for row in cursor.fetchall():
        print(row)

    wait()

    #? 1 student per row. still an INNER join Query by name(show a bad query, using name with 2 students name Alice):
    print("\n# INNER JOIN: Students with enrolled courses 1 per row concat courses")
    cursor.execute("""
        SELECT Students.name, GROUP_CONCAT(Courses.course_name, ', ') AS courses
        FROM Students
        INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id
        INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
        GROUP BY Students.name; 
    """) #! Would run fine with student_id
    for row in cursor.fetchall():
        print(row)

    wait()

    #? LEFT JOIN - Returns all rows from Students, even if not enrolled.
    print("\n# LEFT JOIN: All students, including those without courses")
    cursor.execute("""
        SELECT Students.name, Courses.course_name
        FROM Students
        LEFT JOIN Enrollments ON Students.student_id = Enrollments.student_id
        LEFT JOIN Courses ON Enrollments.course_id = Courses.course_id
    """)
    for row in cursor.fetchall():
        print(row)

    wait()

    #? CROSS JOIN - Returns every possible student-course combination.
    print("\n# CROSS JOIN: Every possible student and course pairing")
    cursor.execute("""
        SELECT Students.name, Courses.course_name
        FROM Students
        CROSS JOIN Courses
    """)
    for row in cursor.fetchall():
        print(row)

    wait()

    #? SELF JOIN - Compares rows within the same table.
    print("\n# SELF JOIN: Pairs of students who are the same age")
    cursor.execute("""
        SELECT Students.name, OtherStudents.name, Students.age
        FROM Students
        INNER JOIN Students AS OtherStudents
        ON Students.age = OtherStudents.age
        AND Students.student_id != OtherStudents.student_id
    """)
    for row in cursor.fetchall():
        print(row)

    wait()

    #? RIGHT JOIN - SQLite does not support RIGHT JOIN directly.
    # We simulate RIGHT JOIN by swapping the LEFT JOIN table order.
    print("\n# RIGHT JOIN (simulated using LEFT JOIN): All courses, even if no students are enrolled")
    cursor.execute("""
        SELECT Courses.course_name, Students.name
        FROM Courses
        LEFT JOIN Enrollments ON Courses.course_id = Enrollments.course_id
        LEFT JOIN Students ON Enrollments.student_id = Students.student_id
    """)
    for row in cursor.fetchall():
        print(row)

    wait()

    #? FULL OUTER JOIN - Not directly supported in SQLite - Returns ALL rows from BOTH tables..
    # Simulate with UNION of two LEFT JOINs.
    print("\n# FULL OUTER JOIN (simulated): All students and courses")
    cursor.execute("""
        SELECT Students.name, Courses.course_name
        FROM Students
        LEFT JOIN Enrollments ON Students.student_id = Enrollments.student_id
        LEFT JOIN Courses ON Enrollments.course_id = Courses.course_id

        UNION

        SELECT Students.name, Courses.course_name
        FROM Courses
        LEFT JOIN Enrollments ON Courses.course_id = Enrollments.course_id
        LEFT JOIN Students ON Enrollments.student_id = Students.student_id
    """)
    for row in cursor.fetchall():
        print(row)
    
wait()

#! SECTION 6: Updating and Deleting
with sqlite3.connect("school_demo.db") as conn:
    cursor = conn.cursor()

    print("# Updating Charlie's name to Charles")
    cursor.execute("UPDATE Students SET name = 'Charles', age = 20 WHERE name = 'Charlie'")
    conn.commit()

    cursor.execute("SELECT * FROM Students WHERE name = 'Charles'")
    print(cursor.fetchone())
    wait() 

    print("\n# Deleting students younger than 21")
    cursor.execute("DELETE FROM Students WHERE age < 21")
    conn.commit()

    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

wait()

#! SECTION 7: Using Pandas with SQL
#? Using INNER join from earlier into Dataframe
with sqlite3.connect("school_demo.db") as conn:
    sql = """
    SELECT Students.name AS student, Courses.course_name AS course
    FROM Students
    JOIN Enrollments ON Students.student_id = Enrollments.student_id
    JOIN Courses ON Enrollments.course_id = Courses.course_id
    """
    df = pd.read_sql_query(sql, conn)
    print("# Loaded into Pandas DataFrame:")
    print(df)

wait()

#! SECTION 8: Demonstrating Transactions (Customer → Bank)
with sqlite3.connect("school_demo.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Create accounts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Accounts (
        account_id INTEGER PRIMARY KEY,
        owner TEXT NOT NULL,
        balance REAL NOT NULL
    )
    """)

    # Seed demo data if empty
    cursor.execute("SELECT COUNT(*) FROM Accounts")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO Accounts (owner, balance) VALUES (?, ?)
        """, [
            ("Alice", 500.0),
            ("Bank", 10000.0)
        ])
        conn.commit()

    print("\n# Before Transaction")
    cursor.execute("SELECT owner, balance FROM Accounts")
    for row in cursor.fetchall():
        print(row)
    wait()

    try:
        print("# BEGIN transaction")
        conn.execute("BEGIN")
        wait()

        print("# Fetch Alice's balance")
        cursor.execute("SELECT balance FROM Accounts WHERE owner = ?", ("Alice",))
        customer_balance = cursor.fetchone()
        print("Alice's balance:", customer_balance[0])
        wait()

        amount = 200.0
        print(f"# Check if Alice has enough funds to transfer ${amount}")
        if customer_balance[0] < amount:
            print("Insufficient funds")
            conn.rollback()  #? cursor.execute("ROLLBACK") does this too.
            raise Exception("Insufficient funds")
        wait()

        print("# Deducting from Alice")
        cursor.execute("""
            UPDATE Accounts SET balance = balance - ? WHERE owner = ?
        """, (amount, "Alice"))
        cursor.execute("SELECT balance FROM Accounts WHERE owner = ?", ("Alice",))
        new_balance = cursor.fetchone()[0]
        print(f"Alice's new balance: ${new_balance:.2f}")
        wait()

        print("# Adding funds to Bank")
        cursor.execute("""
            UPDATE Accounts SET balance = balance + ? WHERE owner = ?
        """, (amount, "Bank"))
        cursor.execute("SELECT balance FROM Accounts WHERE owner = ?", ("Bank",))
        new_balance = cursor.fetchone()[0]
        print(f"The banks new balance is: ${new_balance:.2f}")
        wait()

        print("# Commit transaction")
        conn.commit()
        print(f"\nTransaction successful: Transferred ${amount} from Alice → Bank.")
    except Exception as e:
        print(f"Transaction failed: {e}")
        conn.rollback() 

    print("\n# After Transaction")
    cursor.execute("SELECT owner, balance FROM Accounts")
    for row in cursor.fetchall():
        print(row)
    wait()

    #! Forced failure example to demonstrate rollback
    print("\n# FORCED FAILURE: Attempting to transfer too much")
    try:
        conn.execute("BEGIN")
        amount = 9999.0
        print(f"Attempting to transfer ${amount} from Alice → Bank")
        cursor.execute("SELECT balance FROM Accounts WHERE owner = ?", ("Alice",))
        customer_balance = cursor.fetchone()
        print("Alice's balance:", customer_balance[0])
        wait()

        if customer_balance[0] < amount:
            print("Insufficient funds detected, rolling back…")
            conn.rollback()  
            raise Exception("Insufficient funds")
        wait()

        cursor.execute("""
            UPDATE Accounts SET balance = balance - ? WHERE owner = ?
        """, (amount, "Alice"))
        cursor.execute("""
            UPDATE Accounts SET balance = balance + ? WHERE owner = ?
        """, (amount, "Bank"))
        conn.commit()

    except Exception as e:
        print(f"Transaction failed: {e}")
        conn.rollback()  

    print("\n# After Forced Rollback")
    cursor.execute("SELECT owner, balance FROM Accounts")
    for row in cursor.fetchall():
        print(row)
    wait()

#! SECTION 9: Preventing SQL Injection Attacks

with sqlite3.connect("school_demo.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Seed data if empty
    cursor.execute("SELECT COUNT(*) FROM Users")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO Users (username, password) VALUES (?, ?)
        """, [
            ("alice", "password123"),
            ("bob", "hunter2")
        ])
        conn.commit()

    print("# Demo Users Table:")
    cursor.execute("SELECT user_id, username, password FROM Users")
    for row in cursor.fetchall():
        print(row)
    wait()

    #! BAD EXAMPLE: vulnerable to SQL injection
    print("\n# BAD EXAMPLE: Vulnerable Login Query")
    username_input = "alice' --" #? username_input = "' OR 1=1 --"
    password_input = "doesntmatter"
    try:
        # This builds the query directly from user input — VERY DANGEROUS!
        #! SELECT * FROM Users WHERE username = 'alice' --' AND password = 'doesntmatter'; 
        #! -- is a comment and ignores everything else
        #! SELECT * FROM Users WHERE username = '' OR 1=1 --' AND password = 'irrelevant'; 
        #! OR 1=1 = True and would dump all users. 
        query = f"SELECT * FROM Users WHERE username = '{username_input}' AND password = '{password_input}'"
        print("Executing vulnerable query:", query)
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            print("!! Logged in as:", result[1])
        else:
            print("Login failed.")
    except Exception as e:
        print("Error during bad login:", e)
    wait()

    #? GOOD EXAMPLE: safe parameterized query
    print("\n# GOOD EXAMPLE: Secure Login Query")
    username_input = "alice' --"
    password_input = "doesntmatter"
    try:
        # Using ? placeholders prevents injection
        query = "SELECT * FROM Users WHERE username = ? AND password = ?"
        print("Executing safe query:", query)
        cursor.execute(query, (username_input, password_input))
        result = cursor.fetchone()
        if result:
            print("Logged in as:", result[1])
        else:
            print("Login failed safely.")
    except Exception as e:
        print("Error during safe login:", e)
    wait()

print("\n# Takeaway:")
print("- Always use parameterized queries with `?` placeholders.")
print("- Never concatenate raw user input into SQL statements.")
print("- SQLite and most modern DBs fully support parameter binding.")
wait()