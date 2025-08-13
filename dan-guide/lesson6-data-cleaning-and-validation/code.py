import pandas as pd
import numpy as np

def wait():
    input("\nPress Enter to continue...\n")

#! SECTION 1: Pivot Tables
# Pivot tables help summarize data by grouping values (like totals or averages)
# by one or more columns (e.g., by Product and Region).

data = [
    {'Employee': 'Jones', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9000},
    {'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 4000},
    {'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 11000},
    {'Employee': 'Jones', 'Product': 'Widget', 'Region': 'East', 'Revenue': 4000},
    {'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 5500},
    {'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2345},
    {'Employee': 'Smith', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9007},
    {'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 40003},
    {'Employee': 'Smith', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 110012},
    {'Employee': 'Smith', 'Product': 'Widget', 'Region': 'East', 'Revenue': 9002},
    {'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 15500},
    {'Employee': 'Garcia', 'Product': 'Widget', 'Region': 'West', 'Revenue': 6007},
    {'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 42003},
    {'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 160012},
    {'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 16500},
    {'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2458}
]
sales = pd.DataFrame(data)

print("# Full sales data")
print(sales)
wait()


sales_pivot1 = pd.pivot_table(sales, index=['Product','Region'], values='Revenue', aggfunc='sum', fill_value=0)
# - index=['Product', 'Region']: sets rows using unique combinations of Product and Region
# - values='Revenue': selects the Revenue column to aggregate
# - aggfunc='sum': totals Revenue for each Product-Region combo
# - fill_value=0: replaces missing values (NaN) with 0
print("# Pivot Table 1: Revenue by Product and Region")
print(sales_pivot1)
wait()

sales_pivot2 = pd.pivot_table(sales, index='Product', values='Revenue', columns='Region', aggfunc='sum', fill_value=0)
print("# Pivot Table 2: Revenue by Product (columns split by Region)")
print(sales_pivot2)
wait()

sales_pivot3 = pd.pivot_table(sales, index='Product', values='Revenue', columns=['Region','Employee'], aggfunc='sum', fill_value=0)
print("# Pivot Table 3: Revenue by Product, Region, and Employee")
print(sales_pivot3)
wait()

#! SECTION 2: apply() and row-wise logic
# Use apply() to create new columns based on custom rules across multiple columns

per_employee_sales = sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Plan'] = ['A', 'A', 'B']

def calculate_commission(row):
    if row['Revenue'] < 10000:
        return 0 # No commission unless revenue is at least 10,000
    if row['Commission Plan'] == 'A':
        return 1000 + 0.05 * (row['Revenue'] - 10000) # Plan A: $1000 base + 5% of revenue *above* 10,000
    else:
        return 1400 + 0.04 * (row['Revenue'] - 10000) # Plan B: $1400 base + 4% of revenue *above* 10,000

per_employee_sales['Commission'] = per_employee_sales.apply(calculate_commission, axis=1)

print("# Total revenue and commission by employee (custom logic using apply())")
print(per_employee_sales)
wait()

#! SECTION 3: Handling Missing Data
# Handle missing (NaN) values by either dropping them or filling them in

data = {'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
        'Age': [25, None, 35, 40, 30],
        'Salary': [50000, 60000, None, 80000, 55000],
        'Join Date': ['2020-01-01', None, '2020-03-15', '2020-04-20', None],
        'City': ['New York', 'Los Angeles', 'Chicago', None, 'Miami']}
df = pd.DataFrame(data)

print("# Original data with missing values")
print(df)
wait()

df1 = df.dropna()
print("# After dropna() (rows with ANY missing values removed)")
print(df1)
wait()
#? not handling city for demo. 
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'Salary': df['Salary'].median(),
    'Join Date': '2020-01-01'
})
print("# After fillna() with specific replacements")
print(df_filled)
wait()

df2 = df_filled.dropna(subset=['City']).reset_index(drop=True)
df2['Age'] = df2['Age'].astype(int)
print("# Final cleaned dataset with valid 'City' and integer 'Age'")
print(df2)
wait()

#! SECTION 4: Data Transformation
# Convert types and reformat values like strings and dates

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'JoinDate': ['2023-01-15', '2022-12-20', 'invalid']}
df3 = pd.DataFrame(data)

print("# Raw data with age as strings and bad date format")
print(df3)
wait()

df3['Age'] = df3['Age'].astype(int)
df3['JoinDate'] = pd.to_datetime(df3['JoinDate'], errors='coerce')
#df3['JoinDate'] = df3['JoinDate'].fillna(pd.Timestamp('2000-01-01'))  #? Can replace NaT in this way
print("# After type conversion and handling invalid dates")
print(df3)
wait()

#! SECTION 5: String Replacement and Standardization
# Fix inconsistent labels (like city or location names)

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY']}
df4 = pd.DataFrame(data)
print("Before conversion DF4:")
print(df4)
wait()

df4['Location'] = df4['Location'].replace({'LA': 'Los Angeles', 'NY': 'New York'})
print("# Location column standardized with replace()")
print(df4)
wait()

#! SECTION 6: Data Discretization
# Convert numeric values (like grades or scores) into categories

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Grade': [78, 40, 85]}
df5 = pd.DataFrame(data)
print("Before conversion DF5:")
print(df5)
wait()

df5['GradeCategory'] = pd.cut(df5['Grade'], 3, labels = ["bad", "okay", "great"])
# pd.cut() is used to segment and sort data values into discrete bins using the range of the series"Grade"
# "bad" for 40.0 - 55.0, 
# "okay" for 55.0 - 70.0, 
# "great" for 70.0 - 85.0
print("# Grade column converted into categories with pd.cut()")
print(df5)
wait()

#! SECTION 7: Removing Duplicates
# Detect and remove duplicate rows or entries based on one or more columns

data = {'Name': ['Alice', 'Bob', 'Alice', 'David', 'Alice'],
        'Age': [24, 27, 24, 32, 40],
        'Score': [85, 92, 85, 76, 70]}
df6 = pd.DataFrame(data)
print("Before conversion DF6:")
print(df6)
wait()

df_cleaned = df6.drop_duplicates()
print("# All duplicate rows removed")
print(df_cleaned)
wait()

df_cleaned_by_name = df6.drop_duplicates(subset='Name')
#? useful for something like emails.
print("# Keep only first row per Name")
print(df_cleaned_by_name)
wait()

#! SECTION 8: Removing Outliers
# Replace extreme values that fall outside valid ranges

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 200, 43, -5]}
df7 = pd.DataFrame(data)
print("Before conversion DF7:")
print(df7)
wait()

df7['Age'] = df7['Age'].apply(lambda x: np.nan if x > 100 or x < 0 else x)
print("# After marking invalid ages as NaN")
print(df7)
wait()

df7['Age'] = df7['Age'].fillna(df7['Age'].median())
print("# After filling outlier ages with median")
print(df7)
wait()
