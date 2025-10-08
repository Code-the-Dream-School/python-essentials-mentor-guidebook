# code.py

import pandas as pd
import numpy as np

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
#? 'inner' – Only rows with matching keys in both DataFrames are kept.
# pd.merge(df1, df2, how='inner')
#? 'left' – All rows from the left DataFrame are kept, and matching rows from the right DataFrame are included. Non-matching right-side rows become NaN.
# pd.merge(df1, df2, how='left')
#? 'right' – All rows from the right DataFrame are kept, and matching rows from the left DataFrame are included. Non-matching left-side rows become NaN.
# pd.merge(df1, df2, how='right')
#? 'outer' – All rows from both DataFrames are kept. Non-matching entries get NaN for missing values.
# pd.merge(df1, df2, how='outer')
#? 'cross' – Performs a cross join (Cartesian product) between the DataFrames. No on key is needed for this join.
# pd.merge(df1, df2, how='cross')
# df1 = pd.DataFrame({
#     'A': [1, 2],
#     'B': ['x', 'y']
# })

# df2 = pd.DataFrame({
#     'C': ['a', 'b', 'c']
# })
#    A  B  C
# 0  1  x  a
# 1  1  x  b
# 2  1  x  c
# 3  2  y  a
# 4  2  y  b
# 5  2  y  c

print(merged)
wait()
merged['Salary'] = merged['Salary'].fillna(15000)
merged['Favorite Color'] = merged['Favorite Color'].fillna("yellow")

#? if left != NaN, uses left, else right
merged['Age'] = np.where(merged['Age_left'].notna(), merged['Age_left'], merged['Age_right']) 
merged.drop(columns=['Age_left', 'Age_right'], inplace=True)
print(merged)
wait()

#? Joins df1_b and df3_b on their index (Name) using an outer join. Both DFs have Age, so we get lsuffix/rsuffix
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

#? Go over Kaggle. 
