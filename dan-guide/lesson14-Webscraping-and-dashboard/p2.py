import sqlite3
import pandas as pd

try:
    # Load cleaned CSV
    df = pd.read_csv("batting_avg_cleaned.csv")

    # Connect to SQLite and create table, students will do this for each CSV.
    with sqlite3.connect("batting_avg.db") as conn:
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS batting_avg_leaders")

        cursor.execute("""
            CREATE TABLE batting_avg_leaders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                year INTEGER,
                league TEXT,
                player TEXT,
                team TEXT,
                avg REAL
            )
        """)

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO batting_avg_leaders (year, league, player, team, avg)
                VALUES (?, ?, ?, ?, ?)
            """, (row["Year"], row["League"], row["Player"], row["Team"], row["AVG"]))

        conn.commit()

    print("Loaded data into batting_avg.db")

except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
    print(f"Error occurred: {e}")
