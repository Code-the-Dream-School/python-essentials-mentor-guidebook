import sqlite3
import questionary
from rich.console import Console

console = Console()
DB_NAME = "demo_cache.db"


def init_db():
    """Create a sample SQLite database with a cache table"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cache (
            key TEXT PRIMARY KEY,
            value TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def insert_into_cache(key, value):
    """Insert or update cache values"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cache (key, value)
        VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET value=excluded.value
    """, (key, value))
    conn.commit()
    conn.close()


def read_from_cache(key):
    """Read a cached value"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM cache WHERE key=?", (key,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None


def show_cache_contents():
    """Display the cache table contents"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT key, value, created_at FROM cache")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print("[yellow]Cache is empty[/yellow]")
        return

    console.print("\n[bold cyan]Current Cache Entries:[/bold cyan]")
    for r in rows:
        console.print(f"[green]{r[0]}[/green] → {r[1]} (added {r[2]})")


def explain_sqlite_use_cases():
    """Interactive explanation of SQLite use-cases"""
    explanations = {
        "Embedded local caches": (
            "SQLite is perfect for apps needing fast, small local caches. "
            "For example, browsers use SQLite to store history, cookies, and session data."
        ),
        "Offline-first mobile apps": (
            "Mobile apps like WhatsApp or Signal use SQLite to store messages locally "
            "when offline and sync later when the connection is restored."
        ),
        "Config storage for desktop apps": (
            "Applications like Spotify and Skype store preferences, playlists, and user data "
            "in SQLite since it's lightweight and reliable."
        ),
        "Lightweight prototyping DB": (
            "SQLite requires no setup and is serverless, making it perfect for testing "
            "and rapid prototyping before moving to a heavier database."
        ),
        "Ad-hoc data analysis": (
            "SQLite can handle structured CSV/JSON imports and quick SQL queries locally, "
            "making it ideal for small-scale analytics and ETL experiments."
        )
    }

    info = questionary.checkbox(
        "Select SQLite use-cases you want to learn about:",
        choices=list(explanations.keys())
    ).ask()

    # If user selects nothing, show all use-cases
    if not info:
        console.print("[yellow]No use-cases selected. Showing all:[/yellow]\n")
        info = explanations.keys()

    console.print("\n[bold blue]SQLite Use-Case Details:[/bold blue]")
    for item in info:
        console.print(f"[cyan]• {item}[/cyan]: {explanations[item]}")


def main():
    console.rule("[bold magenta]SQLite + Questionary Interactive Demo")
    init_db()

    while True:
        choice = questionary.select(
            "Choose an action:",
            choices=[
                "1. Insert or Update Cache",
                "2. Read from Cache",
                "3. Show Cache Contents",
                "4. Learn About SQLite Use-Cases",
                "5. Exit"
            ]
        ).ask()

        # Use match-case for cleaner control flow (Python 3.10+)
        match choice[0]:  # Only look at the first number
            case "1":
                key = questionary.text("Enter cache key:").ask()
                value = questionary.text("Enter cache value:").ask()
                insert_into_cache(key, value)
                console.print(f"[green]Saved '{key}' → '{value}' to cache[/green]")

            case "2":
                key = questionary.text("Enter cache key to read:").ask()
                value = read_from_cache(key)
                if value:
                    console.print(f"[cyan]Value:[/cyan] {value}")
                else:
                    console.print(f"[red]No entry found for key '{key}'[/red]")

            case "3":
                show_cache_contents()

            case "4":
                explain_sqlite_use_cases()

            case "5":
                console.print("[bold yellow]Exiting demo. Goodbye![/bold yellow]")
                break

            case _:
                console.print("[red]Invalid selection[/red]")


if __name__ == "__main__":
    main()
