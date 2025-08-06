# code.py

import pandas as pd
import numpy as np
import os

def wait():
    input("\nPress Enter to continue...\n")

#! SECTION 1: Data Selection
print("=== Section 1: Data Selection ===")

df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 30],
    'Salary': [50000, 60000, 70000, 80000, 55000]
})
df2 = pd.DataFrame({
    'Name': ['Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
    'Age': [28, 33, 35, 29, 40],
    'Salary': [52000, 58000, 72000, 61000, 85000]
})
df3 = pd.DataFrame({
    'Name': ['Frank', 'Helen', 'Ian', 'Hima', 'Chaka'],
    'Age': [17, 93, 12, 57, 106],
    'Favorite Color': ['blue', 'pink', 'burgundy', 'red', 'turquoise']
})

print(df1)
wait()
print(df1['Name'])
wait()
print(df1[['Name', 'Salary']])
wait()
print(df1.iloc[:3]) #Position based
wait()
print(df1.loc[[0,2]]) #LABEL BASED 
wait()

#! SECTION 2: Data Aggregation
print("=== Section 2: Data Aggregation ===")
agg = df1.groupby('Age')['Salary'].agg(['mean', 'sum', 'count'])
print(agg)
wait()

#! SECTION 3: Merging and Joining
print("=== Section 3: Merging and Joining ===")
merged = pd.merge(df1, df3, on='Name', how='outer', suffixes=['_left', '_right'])
print(merged)
wait()
merged['Salary'] = merged['Salary'].fillna(15000)
merged['Favorite Color'] = merged['Favorite Color'].fillna("yellow")
merged['Age'] = np.where(merged['Age_left'].notna(), merged['Age_left'], merged['Age_right'])
merged.drop(columns=['Age_left', 'Age_right'], inplace=True)
print(merged)
wait()

df1_b = df1.set_index('Name')
df3_b = df3.set_index('Name')
joined = df1_b.join(df3_b, how='outer', lsuffix='_df1', rsuffix='_df3')
print(joined)
wait()

#! SECTION 4: Row Filtering
print("=== Section 4: Filtering Rows ===")
print(df1[df1['Age'] > 30])
wait()

#! SECTION 5: Sorting
print("=== Section 5: Sorting ===")
print(df1.sort_values(by='Salary', ascending=False))
wait()

#! SECTION 6: Rename Columns
print("=== Section 6: Rename Columns ===")
renamed = df1.rename(columns={'Age': 'Employee Age', 'Salary': 'Employee Salary'})
print(renamed)
wait()

#! SECTION 7: Data Transformation
print("=== Section 7: Data Transformation ===")
df1['Salary'] = df1['Salary'] * 1.1
print(df1)
wait()

#! SECTION 8: Concatenation
print("=== Section 8: Concatenation ===")
concatenated = pd.concat([df1, df2], ignore_index=True)
print(concatenated)
wait()

#! SECTION 9: Football Data Wrangling
print("=== Section 9: Football Data Wrangling ===")
football_path = ""
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        if filename == 'results.csv':
            football_path = os.path.join(dirname, filename)

if football_path:
    football = pd.read_csv(football_path)
    print(football.head())
    wait()

    subset = football[['home_team', 'away_team', 'home_score', 'away_score', 'date']]
    results_2 = subset.rename(columns={
        'home_team': 'team',
        'away_team': 'opponent',
        'home_score': 'points_for',
        'away_score': 'points_against'
    })
    results_3 = subset.rename(columns={
        'away_team': 'team',
        'home_team': 'opponent',
        'away_score': 'points_for',
        'home_score': 'points_against'
    })
    football = pd.concat([results_2, results_3], ignore_index=True)
    print(football.head())
    wait()

    pa = football.groupby('team')['points_against'].mean().sort_values(ascending=False)
    print("Worst 10 defenses:")
    print(pa.head(10))
    wait()

#! SECTION 10: Tunisia Results
print("=== Section 10: Tunisia Results ===")
if football_path:
    tunisia = football[football['team'] == 'Tunisia']
    recent = tunisia.sort_values(by='date', ascending=False).head(10)
    print(recent)
    wait()
