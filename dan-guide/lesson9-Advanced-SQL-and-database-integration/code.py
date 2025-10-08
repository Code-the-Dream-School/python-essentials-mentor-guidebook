# Advanced SQL & Database Integration — WEEK 9 CTD Mentor Session

#! Concepts: 
# Subqueries, 
# Complex JOINs, 
# Aggregation + HAVING, 
# Indexing, 
# Transactions, 
# SQL Injection Prevention, 
# Window & Date Functions


import sqlite3

def pause():
    input("\nPress Enter to continue...\n")

# Connect to the database
with sqlite3.connect("../db/company.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  #? Enforce foreign key constraints
    cursor = conn.cursor()

    #! Setup: Create Employees and Projects tables
    cursor.execute("DROP TABLE IF EXISTS Employees")
    cursor.execute("DROP TABLE IF EXISTS Projects")
    cursor.execute("""
        CREATE TABLE Employees (
            employee_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE Projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        )
    """)
    cursor.executemany("INSERT INTO Employees (name, department, salary) VALUES (?, ?, ?)", [
        ('Alice', 'HR', 72000),
        ('Bob', 'IT', 80000),
        ('Charlie', 'HR', 68000),
        ('Dana', 'Finance', 95000),
        ('Eli', 'IT', 75000)
    ])
    cursor.executemany("INSERT INTO Projects (name, department) VALUES (?, ?)", [
        ('Project A', 'HR'),
        ('Project B', 'IT'),
        ('Project C', 'Finance')
    ])
    conn.commit()

    #! Subquery: Find highest-paid employee in each department
    print("== Subquery: Highest-paid employee in each department ==")
    cursor.execute("""
        SELECT department, name, salary
        FROM Employees AS e
        WHERE salary = (
            SELECT MAX(salary)
            FROM Employees
            WHERE department = e.department
        )
    """)
    print(cursor.fetchall())
    pause()

    #? Subqueries allow for intermediate calculations within a main query
    #? Useful for comparisons like finding max/min values within groups
    #? Example: SELECT * FROM Employees e WHERE salary = (SELECT MAX(salary) FROM Employees WHERE department = e.department)
    #? ie: Returns employees who are the highest-paid within their department

    #* Useful for checking if a value exists in another result set
    #* Example: SELECT * FROM Employees WHERE department IN (SELECT department FROM Projects)
    #* ie: Returns employees whose department is assigned to at least one project

    #? Useful for filtering out values not present in another result set
    #? Example: SELECT * FROM Employees WHERE department NOT IN (SELECT department FROM Projects)
    #? ie: Returns employees in departments that have no projects

    #* Useful for confirming related data exists (more efficient than IN) - stops as SOON as it finds a match. IN fetches all values.
    #* Example: SELECT * FROM Employees e WHERE EXISTS (SELECT 1 FROM Projects p WHERE p.department = e.department)
    #* ie: Returns employees if their department matches at least one row in Projects

    #? Useful for confirming related data does not exist
    #? Example: SELECT * FROM Employees e WHERE NOT EXISTS (SELECT 1 FROM Projects p WHERE p.department = e.department)
    #? ie: Returns employees whose department does not appear at all in the Projects table

    #* Useful for comparing against all values in a subquery
    #* Example: SELECT * FROM Employees WHERE salary > ALL (SELECT salary FROM Employees WHERE department = 'HR')
    #* ie: Returns employees who earn more than every employee in the HR department

    #? Useful for checking if a value is greater than any in a group
    #? Example: SELECT * FROM Employees WHERE salary > ANY (SELECT salary FROM Employees WHERE department = 'HR')
    #? ie: Returns employees who earn more than the lowest-paid employee in the HR department

    #* Useful for correlating one table against a grouped summary
    #* Example: SELECT * FROM Employees e WHERE salary > (SELECT AVG(salary) FROM Employees WHERE department = e.department)
    #* ie: Returns employees earning above the average in their own department

    #! Complex JOIN: Employees working on 'Project A'
    #? INNER JOIN: Returns only employees who belong to a department that has a project named 'Project A'
    print("== INNER JOIN: Employees working on Project A ==")
    cursor.execute("""
        SELECT Employees.name, Projects.name AS project_name
        FROM Employees
        INNER JOIN Projects ON Employees.department = Projects.department
        WHERE Projects.name = 'Project A'
    """)
    print(cursor.fetchall())
    pause()

    

    print("== LEFT JOIN: All employees and their project (if any) ==")
    cursor.execute("""
        SELECT Employees.name, Projects.name AS project_name
        FROM Employees
        LEFT JOIN Projects ON Employees.department = Projects.department
    """)
    print(cursor.fetchall())
    pause()

    #? INNER JOIN: Returns records with matching values in both tables
    #? LEFT JOIN: Returns all records from the left table, and matched records from the right table
    #? RIGHT JOIN: Not directly supported in SQLite; can be simulated using LEFT JOINs
    #? FULL OUTER JOIN: Not directly supported in SQLite; can be simulated using UNION of LEFT and RIGHT JOINs

    #! Aggregation: Average salary per department
    print("== GROUP BY + Aggregation: Salary stats per department ==")
    cursor.execute("""
        SELECT department, 
            COUNT(*) AS num_employees, 
            ROUND(AVG(salary), 2) AS avg_salary,
            SUM(salary) AS total_salary,
            MIN(salary) AS lowest_salary,
            MAX(salary) AS highest_salary
        FROM Employees
        GROUP BY department
    """)
    print(cursor.fetchall())
    pause()

    #? COUNT(): SELECT department, COUNT(*) FROM Employees GROUP BY department
    #? AVG(): SELECT department, AVG(salary) FROM Employees GROUP BY department
    #? SUM(): SELECT department, SUM(salary) FROM Employees GROUP BY department
    #? MIN(): SELECT department, MIN(salary) FROM Employees GROUP BY department
    #? MAX(): SELECT department, MAX(salary) FROM Employees GROUP BY department
    #? GROUP BY: Groups rows by column(s) so aggregation functions apply to each group

    #! HAVING: Departments with average salary > 70,000
    print("== HAVING: Departments with avg salary > 70k ==")
    cursor.execute("""
        SELECT department, 
            COUNT(*) AS num_employees,
            ROUND(AVG(salary), 2) AS avg_salary,
            SUM(salary) AS total_salary
        FROM Employees
        GROUP BY department
        HAVING avg_salary > 70000
    """)
    print(cursor.fetchall())
    pause()

    #! HAVING vs WHERE: Filter rows before vs after grouping
    print("== WHERE filters raw rows; HAVING filters grouped results ==")
    cursor.execute("""
        SELECT department, 
            COUNT(*) AS num_employees,
            ROUND(AVG(salary), 2) AS avg_salary,
            SUM(salary) AS total_salary
        FROM Employees
        WHERE salary > 50000
        GROUP BY department
        HAVING avg_salary > 70000
    """)
    print(cursor.fetchall())
    pause()

    #? HAVING: Filters groups based on aggregate functions like AVG(), COUNT(), SUM(), etc.
    #? WHERE: Filters rows BEFORE grouping (used for raw row values) - used to limit which rows get grouped/included in aggregation
    #? Example: WHERE salary > 50000 excludes low salaries from even being counted or averaged
    #? Example with WHERE: SELECT * FROM Employees WHERE salary > 70000
    #? Example with HAVING: SELECT department, AVG(salary) FROM Employees GROUP BY department HAVING AVG(salary) > 70000

    #? You can use HAVING with COUNT():
    #? SELECT department FROM Employees GROUP BY department HAVING COUNT(*) > 2
    #? ie: Returns departments with more than 2 employees

    #? You can use HAVING with SUM():
    #? SELECT department FROM Employees GROUP BY department HAVING SUM(salary) > 150000
    #? ie: Returns departments whose combined salaries exceed 150k
    
    #! Indexing: Create index on department column
    print("== Creating index on department column ==")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_department ON Employees(department)")
    print("Index created.")
    pause()

    #? Think of an index like a phone book:
    #? Instead of flipping through every page to find “Bob”, you go straight to the ‘B’ section
    #? An index is a separate structure that keeps a sorted, searchable map of one column (like department)

    #? It’s not a separate table you can SELECT from directly, but the database engine uses it behind the scenes
    #? It doesn't store full rows — just keys and pointers to rows in the original table

    #? Creating this:
    #? CREATE INDEX idx_department ON Employees(department)
    #? Tells SQLite: “Keep department values sorted and quick to search”
    #? SQLite indexes are stored as B-trees (balanced tree structures)
    #? They keep indexed values sorted, allowing for fast lookups, range scans, and ORDER BY

    #! B tree example: https://www.cs.usfca.edu/~galles/visualization/BTree.html

    #! Transactions: Demonstrate COMMIT and ROLLBACK
    print("== BEFORE TRANSACTION ==")
    cursor.execute("SELECT name, department, salary FROM Employees WHERE department = 'Marketing'")
    print(cursor.fetchall())
    pause()

    #! Successful transaction
    print("== SUCCESSFUL TRANSACTION (Frank + Grace) ==")
    try:
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("INSERT INTO Employees (name, department, salary) VALUES (?, ?, ?)", ('Frank', 'Marketing', 70000))
        cursor.execute("INSERT INTO Employees (name, department, salary) VALUES (?, ?, ?)", ('Grace', 'Marketing', 72000))
        conn.commit()
        print("Transaction committed.")
    except Exception as e:
        conn.rollback()
        print("Transaction rolled back due to error:", e)
    pause()

    print("== AFTER SUCCESSFUL TRANSACTION ==")
    cursor.execute("SELECT name, department, salary FROM Employees WHERE department = 'Marketing'")
    print(cursor.fetchall())
    pause()

    #! Failed transaction
    print("== FAILED TRANSACTION (missing salary) ==")
    try:
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("INSERT INTO Employees (name, department, salary) VALUES (?, ?, ?)", ('Hank', 'Marketing', 69000))
        #! Only fails if salary is set to NOT NULL
        cursor.execute("INSERT INTO Employees (name, department, salary) VALUES (?, ?, ?)", ('Invalid', 'Marketing', None))
        conn.commit()
        print("Transaction committed.")
    except Exception as e:
        conn.rollback()
        print("Transaction rolled back due to error:", e)
    pause()

    print("== AFTER FAILED TRANSACTION ==")
    cursor.execute("SELECT name, department, salary FROM Employees WHERE department = 'Marketing'")
    print(cursor.fetchall())
    pause()

    #? Transactions ensure that a set of operations either all succeed or all fail
    #? BEGIN TRANSACTION starts a new transaction
    #? COMMIT saves the changes
    #? ROLLBACK undoes the changes in case of an error

    #! SQL Injection: Unsafe query using string concatenation
    print("== SQL Injection Demo: UNSAFE query ==")
    malicious_input = "'HR' OR 1=1"  # attacker tries to trick the WHERE clause 
    #! Same as running SELECT * FROM Employees WHERE department = 'HR' OR 1=1 - notice it isn't a string 1=1 is always 
    #! True so it returns all rows. 
    query = f"SELECT * FROM Employees WHERE department = {malicious_input}"  #! Do not do this
    print("Injected Query:", query)
    try:
        cursor.execute(query)
        print(cursor.fetchall())
    except Exception as e:
        print("Error during injection test:", e)
    pause()

    #? This returns ALL employees, not just HR — because the injected OR 1=1 makes the WHERE clause always true
    #? This simulates an attacker bypassing filters or gaining access to unauthorized data

    #! SQL Injection Prevention: Safe parameterized version
    print("== SQL Injection Prevention: SAFE parameterized query ==")
    safe_input = "'HR' OR 1=1"  # same malicious input
    cursor.execute("SELECT * FROM Employees WHERE department = ?", (safe_input,)) 
    #! results in SELECT * FROM Employees WHERE department = "'HR' OR 1=1"
    print(cursor.fetchall())
    pause()

    #? Parameterized query treats the entire string as a literal value — not executable SQL
    #? The database searches for an actual department named "'HR' OR 1=1'" (which likely doesn't exist)
    #? Safe approach blocks injection from altering query logic

    #! Window Function: RANK() — show top salaries per department
    print("== Window Function: Rank employees by salary within each department ==")
    cursor.execute("""
        SELECT name, department, salary,
            RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
        FROM Employees
    """)
    print(cursor.fetchall())
    pause()

    #? PARTITION BY groups rows by department without collapsing them
    #? ORDER BY sorts salaries in each group
    #? RANK() gives position — rank 1 = highest salary in that department

    #! GROUP BY: Max salary per department (collapsed view — one row per group)
    print("== GROUP BY: Highest salary per department ==")
    cursor.execute("""
        SELECT department, 
            MAX(salary) AS highest_salary
        FROM Employees
        GROUP BY department
    """)
    print(cursor.fetchall())
    pause()

    #? GROUP BY collapses rows into one per department No names included. 
    #? MAX() shows highest salary, but not who earned it

    #! Date Function: Calculate age in days using Employees table

    print("== Adding date_of_birth column to Employees table ==")
    cursor.execute("ALTER TABLE Employees ADD COLUMN date_of_birth TEXT")

    #? Update some existing employees with DOBs
    cursor.execute("UPDATE Employees SET date_of_birth = '1985-05-15' WHERE name = 'Alice'")
    cursor.execute("UPDATE Employees SET date_of_birth = '1990-08-22' WHERE name = 'Bob'")
    cursor.execute("UPDATE Employees SET date_of_birth = '1979-12-30' WHERE name = 'Charlie'")
    conn.commit()
    pause()

    print("== Date Function: Age in days from Employees ==")
    cursor.execute("""
        SELECT name, date_of_birth,
            JULIANDAY('now') - JULIANDAY(date_of_birth) AS age_in_days
        FROM Employees
        WHERE date_of_birth IS NOT NULL
    """)
    print(cursor.fetchall())
    pause()

    #? JULIANDAY('now') gives today's date as a float
    #? Subtracting JULIANDAY(date_of_birth) returns the number of days alive

    #! Cleanup: Drop created tables
    cursor.execute("DROP TABLE IF EXISTS Employees")
    cursor.execute("DROP TABLE IF EXISTS Projects")
    conn.commit()

