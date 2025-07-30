import pandas as pd
import numpy as np
import json

def wait():
    input("\nPress Enter to continue...\n")

#! Section 1: Series and Indexing
print("=== Creating Series ===")

# Series: A one-dimensional array-like structure, similar to a list or array, but with added features such as customizable indexes. 
# Each element in a Series is associated with a label (the index), allowing for more intuitive data manipulation and access.

series = pd.Series([1, 3, 5, 7, 9], name="numbers")
print(series)
wait()

# Index labels can be non-sequential and even repeated
custom_index_series = pd.Series(['Tom', 'Li', 'Antonio', 'Mary'], index=[5, 2, 2, 3])
print("Custom index with non-unique labels:")
print(custom_index_series)

wait()
# Accessing by label (2) returns all entries with label 2
print("Access by label 2:")
print(custom_index_series[2])

wait()
# Trying to access by position using [1] may fail if you meant label 1
print("Access by label vs position (may behave differently):")
print("Series:")
print(custom_index_series)

print("\nAccess with [1] (label-based):")
try:
    print(custom_index_series[1])  # This tries to access label '1', not position 1
except Exception as e:
    print("Error using [1]:", e)

wait()
print("\nAccess with iloc[1] (position-based):")
try:
    print(custom_index_series.iloc[1])  # This correctly accesses the second row
except Exception as e:
    print("Error using iloc[1]:", e)

wait()

print("Reset index to remove custom labels:")
print(custom_index_series.reset_index(drop=True))
wait()

#! Section 2: Creating and Modifying DataFrames
print("=== Creating and Modifying DataFrames ===")

# Data Frame: A two-dimensional table where each column can hold different types of data. 
# This is the most commonly used data structure in Pandas.

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)
wait()

# Always make a copy before modifying a DataFrame - to avoid modifying a view and throwing an error.
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("Added Salary column:")
print(task1_with_salary)
wait()
# Demonstrate failure when assigning a column with too few values
try:
    task1_with_salary['Money'] = [70000, 80000]  # Only 2 values for 3 rows
except ValueError as e:
    print("Caught error when trying to assign too few salary values:")
    print(e)

print("\nDataFrame after failed Money column assignment:")
print(task1_with_salary)
wait()

#increment a value - in this case "Age"
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("Increased all ages by 1:")
print(task1_older)
wait()

task1_older.to_csv("employees.csv", index=False)
print("Saved to employees.csv (without index column)")
wait()

#! Section 3: Loading from CSV and JSON
print("=== Loading Data ===")

task2_employees = pd.read_csv("employees.csv")
print("Read from CSV:")
print(task2_employees)
wait()
# Create our JSON file
json_data = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]
with open("additional_employees.json", "w") as f:
    json.dump(json_data, f)
print("JSON Data saved to additional_employees.json")
wait()
#read our JSON file
json_employees = pd.read_json("additional_employees.json")
print("Read from JSON:")
print(json_employees)
wait()

#show our csv and JSON employees:
print(task2_employees)
print(json_employees)
wait()

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("Combined both CSV and JSON into one DataFrame:")
print(more_employees)
wait()

#! Section 4: Viewing and Inspecting Data
print("=== Data Inspection ===")
wait()

first_three = more_employees.head(3) #does 5 by default.
print("First 3 rows:")
print(first_three)
wait()

last_two = more_employees.tail(2) #does 5 by default. 
print("Last 2 rows:")
print(last_two)
wait()

employee_shape = more_employees.shape #this is a tuple of (rows, cols)
print("Shape of the combined DataFrame:")
print(employee_shape)
wait()

print("Info summary (shows data types and non-null values):")
more_employees.info()
wait()

#! Section 5: Data Modification – Good vs Bad
print("=== Modifying Data Safely ===")

# BAD: Modifying a view of a column directly (this may give SettingWithCopyWarning)
print("\nBad way of modifying a single value using a copy of a Series:")
print(more_employees)
age_series_view = more_employees['Age']
print(age_series_view)
wait()
try:
    age_series_view[2] = 99
except Exception as e:
    print("Error or warning:", e)

print("DataFrame after bad modification:")
print(more_employees)
wait()

# BETTER: Use a copy of the Series, then reassign it back
print("Better way using copy of the Series:")
age_series_copy = more_employees['Age'].copy()
age_series_copy[2] = 45
more_employees['Age'] = age_series_copy
print(more_employees)
wait()

# BEST: Modify the DataFrame directly using .loc[]
print("Best way using .loc:")
more_employees.loc[2, 'Age'] = 50
print(more_employees)
wait()

#! Section 6: Data Cleaning
print("=== Cleaning Dirty Data ===")

dirty_sample = pd.DataFrame({
    "Name": [" Alice ", "Bob", "Alice", "Eve", "Alice"],
    "Age": ["58", "Thirty", "24", None, "24"],
    "Salary": ["105000", "unknown", "70000", "n/a", "70000"],
    "Department": [" Biotech", "engineering", "HR", "Engineering ", "HR"],
    "Hire Date": ["2014-02-07", "not_a_date", "2020-01-01", "2021/06/15", "2020-01-01"]
})
dirty_sample.to_csv("dirty_data.csv", index=False)

dirty_data = pd.read_csv("dirty_data.csv")
print("Original data:")
print(dirty_data)
wait()

clean_data = dirty_data.copy()

# Remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("After dropping duplicates:")
print(clean_data)
wait()

# Convert Age to numeric, replace errors with NaN
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("Age to numeric:")
print(clean_data)
wait()
# Replace known bad values in Salary and convert to numeric
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("replace bad values:")
print(clean_data)
wait()
# Fill missing Age with the mean, Salary with the median
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print("Fill in missing Age/Salary:")
print(clean_data)
wait()
# Convert date column
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print("Convert date:")
print(clean_data)
wait()
clean_data["Hire Date"] = clean_data["Hire Date"].fillna(pd.Timestamp("1900-01-01"))
print("default date:")
print(clean_data)
wait()
# Remove whitespace and standardize case
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

print("Cleaned data, whitespace and casing:")
print(clean_data)
wait()
