import time
from rich.console import Console

console = Console()

questions = [
    {
        "question": "What is the purpose of dropna()?",
        "options": {
            "A": "Convert all columns to strings",
            "B": "Drop all duplicate values",
            "C": "Remove rows with missing data",
            "D": "Reset the DataFrame index"
        },
        "answer": "C"
    },
    {
        "question": "Which method replaces missing values with a fixed value?",
        "options": {
            "A": "fillna()",
            "B": "dropna()",
            "C": "astype()",
            "D": "apply()"
        },
        "answer": "A"
    },
    {
        "question": "Which method changes column data types?",
        "options": {
            "A": "drop_duplicates()",
            "B": "astype()",
            "C": "cut()",
            "D": "apply()"
        },
        "answer": "B"
    },
    {
        "question": "Which method removes repeated rows from a DataFrame?",
        "options": {
            "A": "dropna()",
            "B": "drop_duplicates()",
            "C": "fillna()",
            "D": "replace()"
        },
        "answer": "B"
    },
    {
        "question": "What does pd.cut() do?",
        "options": {
            "A": "Deletes a DataFrame column",
            "B": "Aggregates pivot tables",
            "C": "Bins numeric data into intervals",
            "D": "Filters by string values"
        },
        "answer": "C"
    },
    {
        "question": "Which argument defines bin ranges in pd.cut()?",
        "options": {
            "A": "labels",
            "B": "bins (2nd arg)",
            "C": "right",
            "D": "include_lowest"
        },
        "answer": "B"
    },
    {
        "question": "What function lets you apply a custom function to each row or column?",
        "options": {
            "A": "astype()",
            "B": "apply()",
            "C": "replace()",
            "D": "groupby()"
        },
        "answer": "B"
    },
    {
        "question": "Which axis value would apply a function across columns (one row at a time)?",
        "options": {
            "A": "0",
            "B": "1",
            "C": "None",
            "D": "'columns'"
        },
        "answer": "B"
    },
    {
        "question": "How would you identify outliers and replace them with NaN?",
        "options": {
            "A": "cut() with labels",
            "B": "pivot_table()",
            "C": "apply() with a condition",
            "D": "astype('float')"
        },
        "answer": "C"
    },
    {
        "question": "What value can you pass to fillna() to replace missing scores with the median?",
        "options": {
            "A": "df.mean()",
            "B": "None",
            "C": "df.median()",
            "D": "errors='coerce'"
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
