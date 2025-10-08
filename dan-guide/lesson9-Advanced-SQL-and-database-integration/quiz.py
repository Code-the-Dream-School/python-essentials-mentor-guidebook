import time
from rich.console import Console

console = Console()

questions = [
    {
        "question": "What is the purpose of a subquery in SQL?",
        "options": {
            "A": "To create a new database",
            "B": "To store temporary values outside the main query",
            "C": "To nest a query inside another query for filtering or comparison",
            "D": "To delete duplicate rows"
        },
        "answer": "C"
    },
    {
        "question": "Which JOIN returns all rows from the left table and matching rows from the right table?",
        "options": {
            "A": "INNER JOIN",
            "B": "LEFT JOIN",
            "C": "RIGHT JOIN",
            "D": "FULL OUTER JOIN"
        },
        "answer": "B"
    },
    {
        "question": "What is the purpose of the HAVING clause in SQL?",
        "options": {
            "A": "To rename columns in query results",
            "B": "To sort rows in a specific order",
            "C": "To filter grouped results after aggregation",
            "D": "To set default values for NULLs"
        },
        "answer": "C"
    },
    {
        "question": "What is the benefit of creating an index on a column?",
        "options": {
            "A": "It reduces the file size of the database",
            "B": "It enables encryption on that column",
            "C": "It speeds up lookup and filtering operations",
            "D": "It ensures data integrity on that column"
        },
        "answer": "C"
    },
    {
        "question": "Which command starts a transaction in SQLite?",
        "options": {
            "A": "BEGIN TRANSACTION;",
            "B": "START TX;",
            "C": "CREATE TRANSACTION;",
            "D": "BEGIN SESSION;"
        },
        "answer": "A"
    },
    {
        "question": "Why would you use ROLLBACK inside a transaction?",
        "options": {
            "A": "To back up the database",
            "B": "To undo all operations since the transaction began",
            "C": "To pause the transaction for later",
            "D": "To save changes permanently"
        },
        "answer": "B"
    },
    {
        "question": "Which function ranks rows within a group of results?",
        "options": {
            "A": "ROW_NUMBER()",
            "B": "RANK()",
            "C": "DENSE_RANK()",
            "D": "All of the above"
        },
        "answer": "D"
    },
    {
        "question": "How is PARTITION BY used with window functions?",
        "options": {
            "A": "To create a temporary view",
            "B": "To separate results into groups for ranking or calculations",
            "C": "To delete duplicate values",
            "D": "To combine multiple tables"
        },
        "answer": "B"
    },
    {
        "question": "Which SQL clause works like WHERE but for aggregated data?",
        "options": {
            "A": "ORDER BY",
            "B": "LIMIT",
            "C": "GROUP BY",
            "D": "HAVING"
        },
        "answer": "D"
    },
    {
        "question": "What is a potential downside of too many indexes?",
        "options": {
            "A": "Indexes reduce query performance",
            "B": "They make the database schema unreadable",
            "C": "Indexes slow down INSERT and UPDATE operations",
            "D": "They remove NULL values from columns"
        },
        "answer": "C"
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
