import time
from rich.console import Console

console = Console()

questions = [
    {
        "question": "Which SQLite command permanently removes an existing table?",
        "options": {
            "A": "DELETE TABLE",
            "B": "REMOVE TABLE",
            "C": "DROP TABLE",
            "D": "TRUNCATE TABLE"
        },
        "answer": "C"
    },
    {
        "question": "What does enabling 'PRAGMA foreign_keys = ON;' do?",
        "options": {
            "A": "Automatically encrypts the database",
            "B": "Ensures foreign key constraints are enforced",
            "C": "Creates new primary keys for all tables",
            "D": "Disables transaction rollbacks"
        },
        "answer": "B"
    },
    {
        "question": "Which SQL JOIN returns only rows that exist in both tables?",
        "options": {
            "A": "LEFT JOIN",
            "B": "RIGHT JOIN",
            "C": "INNER JOIN",
            "D": "FULL OUTER JOIN"
        },
        "answer": "C"
    },
    {
        "question": "In the lesson, why is grouping by 'student_id' better than grouping by 'name'?",
        "options": {
            "A": "Because student names are always unique",
            "B": "It avoids combining rows when students share the same name",
            "C": "It improves database performance",
            "D": "SQLite requires using primary keys for grouping"
        },
        "answer": "B"
    },
    {
        "question": "Which SQL statement adds a new record to a table?",
        "options": {
            "A": "INSERT INTO",
            "B": "ADD RECORD",
            "C": "UPDATE INTO",
            "D": "NEW ROW"
        },
        "answer": "A"
    },
    {
        "question": "What does a LEFT JOIN return?",
        "options": {
            "A": "Only rows that match between both tables",
            "B": "All rows from the left table, plus matching rows from the right",
            "C": "All rows from the right table, plus matching rows from the left",
            "D": "Only rows that exist in neither table"
        },
        "answer": "B"
    },
    {
        "question": "What is the purpose of transactions in the Accounts example?",
        "options": {
            "A": "They make SELECT queries faster",
            "B": "They ensure multiple related changes succeed or fail together",
            "C": "They automatically back up the database",
            "D": "They enable foreign key constraints"
        },
        "answer": "B"
    },
    {
        "question": "Which method in Pandas loads the result of a SQL query into a DataFrame?",
        "options": {
            "A": "pd.load_sql()",
            "B": "pd.read_sql_query()",
            "C": "pd.sql_to_df()",
            "D": "pd.import_query()"
        },
        "answer": "B"
    },
    {
        "question": "What does the SQL injection attack 'alice' --' do in the vulnerable query?",
        "options": {
            "A": "Deletes all rows from the Users table",
            "B": "Logs in as Alice without checking the password",
            "C": "Encrypts the database",
            "D": "Adds a new user called Alice"
        },
        "answer": "B"
    },
    {
        "question": "How can SQL injection attacks be prevented?",
        "options": {
            "A": "Using string concatenation to build queries",
            "B": "Using parameterized queries with placeholders",
            "C": "Escaping all spaces in user input",
            "D": "Disabling SELECT statements"
        },
        "answer": "B"
    }
]

score = 0
TIME_LIMIT = 20

for i, q in enumerate(questions, 1):
    console.rule(f"[bold blue]Question {i}")
    console.print(q["question"])
    for key, val in q["options"].items():
        console.print(f"[bold]{key}.[/bold] {val}")
    
    console.print(f"\n[bold yellow]You have {TIME_LIMIT} seconds to answer...[/bold yellow]")
    start = time.time()
    answer = ""

    try:
        while time.time() - start < TIME_LIMIT:
            console.print("Your answer (A/B/C/D): ", end="")
            answer = input().strip().upper()
            if answer:
                break
        else:
            raise TimeoutError
    except TimeoutError:
        console.print("[bold red]⏰ Time's up! You missed this question.[/bold red]\n")
        continue

    if answer == q["answer"]:
        console.print("[bold green]✔ Correct![/bold green]\n")
        score += 1
    else:
        console.print(f"[bold red]✘ Wrong![/bold red] The correct answer was [bold yellow]{q['answer']}[/bold yellow]\n")

console.rule("[bold magenta]Quiz Completed")
console.print(f"[bold cyan]Final Score: {score}/{len(questions)}[/bold cyan]")
