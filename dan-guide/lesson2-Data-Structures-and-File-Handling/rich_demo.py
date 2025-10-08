from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.syntax import Syntax

console = Console()

# Text with styles
console.print("This is [bold magenta]Rich[/bold magenta]!", style="green")
console.print("Visual output in the terminal made easy.\n", style="bold cyan")

# Table demo
table = Table(title="Student Grades")
table.add_column("Name", style="yellow", no_wrap=True)
table.add_column("Assignment", style="cyan")
table.add_column("Grade", justify="right", style="green")

table.add_row("Alice", "Homework 1", "95")
table.add_row("Bob", "Homework 1", "88")
table.add_row("Charlie", "Homework 1", "92")

console.print(table)

# Markdown demo
md = """
# Welcome to Rich
This is a markdown **demo**.

- It's great for quick documentation.
- Easy to read.
- Shows _emphasis_, lists, and headings.

Try it!
"""
console.print(Markdown(md))

# Syntax-highlighted code block
code = '''
def add(a, b):
    return a + b

print(add(3, 4))
'''
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
