# Lesson 4: Introduction to Data Engineering – Mentor Guide

This session introduces students to the Pandas library and the basics of working with structured data in Python.

***

## Topics I Like to Emphasize

- **Creating Series and DataFrames**  
  Show how `pd.Series()` and `pd.DataFrame()` work from lists and dictionaries. Emphasize how DataFrames are like Excel tables or SQL query results.

- **Indexing by label vs position**  
  Use `.loc[]` when referencing by row label and `.iloc[]` when referencing by row number (position). Labels can be repeated and out of order, positions are always numeric and sequential.

- **Using `.copy()` before modifying**  
  Prevents modifying the original DataFrame by accident. Without it, students may edit a view, not the actual data, leading to bugs.

- **Loading data from files**  
  Use `pd.read_csv()` and `pd.read_json()` to get data into Pandas. Files can contain junk like "unknown" or missing values, which we clean up later.

- **Data inspection**  
  Use `df.head()`, `df.tail()`, and `df.info()` to preview and understand structure, missing data, and column types.

- **Safe updates with `.loc`**  
  Use `df.loc[row_index, 'column_name'] = value` instead of `df['col'][i] = x`, which is unreliable and may not modify the DataFrame at all.

- **Cleaning Dirty Data**

  - ### `pd.to_numeric(..., errors="coerce")`
    Converts strings like `"42"` to the number `42`.  
    If a string can’t be converted (like `"unknown"`), `errors="coerce"` turns it into `NaN` instead of crashing your code.  
    Example:  
    ```python
    pd.to_numeric(["10", "n/a", "55"], errors="coerce")  
    → [10.0, NaN, 55.0]
    ```

  - ### `.fillna()` with mean or median
    Fills in missing values (`NaN`) so your analysis doesn’t break.  
    Example:  
    ```python
    df["Salary"] = df["Salary"].fillna(df["Salary"].median())
    ```
    This replaces all missing salaries with the median value of that column.

  - ### `.str.strip()`, `.str.upper()`
    Cleans up messy string fields.  
    `.strip()` removes leading/trailing spaces (like `" Bob "` becomes `"Bob"`).  
    `.upper()` changes everything to uppercase so `"Sales"` and `"sales"` are treated the same.

  - ### `pd.to_datetime()`
    Converts text like `"2021/01/15"` or `"April 31, 2021"` into proper datetime objects.  
    If the date is invalid, `errors="coerce"` turns it into `NaT` (Not a Time), avoiding a crash.  
    Example:  
    ```python
    pd.to_datetime(["2021-01-01", "not a date"], errors="coerce")
    → [2021-01-01 00:00:00, NaT]
    ```

***

## Common Pitfalls (All demonstrated in `code.py`)

- **Using `[i]` to access rows**  
  If the index is custom or repeated, `[i]` might return unexpected results or fail. Use `.iloc[i]` for the row in position `i`.

- **Modifying a view, not the original DataFrame**  
  `df2 = df[df["Age"] > 30]` is a filtered view. Changing `df2["Age"][0] = 99` might not affect `df`. Use `.copy()` to be safe.

- **Crashes during conversion**  
  Trying `pd.to_numeric(["10", "abc"])` without `errors="coerce"` raises an error. Use `errors="coerce"` to handle bad data.

- **Setting values using `df['col'][i] = x`**  
  This may show a warning and not work. Always use `df.loc[i, 'col'] = x`.

- **Messy text fields**  
  `"  Bob "` and `"BOB"` are not the same when filtering. Clean these with `.str.strip()` and `.str.upper()`.

***

## Sample Prompts for Discussion (with Answers)

- **What’s the difference between `iloc[1]` and `series[1]`?**  
  `iloc[1]` gets the second row by position. `series[1]` gets the value at index label `1`, which could be something totally different or not exist at all.

- **Why is `.copy()` used before modifying a DataFrame?**  
  It ensures you’re working on a new object. Without it, your changes may not save, or you might edit a view instead of the real data.

- **What does `errors="coerce"` do in conversions?**  
  If Pandas encounters a bad value like `"unknown"` when trying to convert to numbers or dates, it quietly replaces it with `NaN` (for numbers) or `NaT` (for dates), letting the program continue without crashing.

- **How does `.fillna()` help in real-world data?**  
  Missing values can break math or graphs. Use `.fillna()` to plug in safe defaults like the column mean or median.

- **What’s the best way to clean up text data?**  
  `.str.strip()` removes extra spaces, `.str.upper()` makes casing consistent. Together, they help match names like `" alice "` and `"ALICE"`.

- **How do `.head()` and `.info()` help you understand new data?**  
  `.head()` shows the first few rows so you see what the data looks like. 5 rows by default
  `.info()` tells you what types each column is (text, number, date), how much is missing, and how big the DataFrame is.
