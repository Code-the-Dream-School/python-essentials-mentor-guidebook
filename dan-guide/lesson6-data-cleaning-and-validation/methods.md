# Pandas Cheatsheet

## General / DataFrame
- `head(n)` - Show first n rows
- `tail(n)` - Show last n rows
- `info()` - Summary of DataFrame including types and non-null counts
- `describe()` - Summary statistics for numeric columns
- `shape` - Return (rows, columns)
- `columns` - List column names
- `drop(labels, axis=0/1)` - Drop rows (axis=0) or columns (axis=1)
- `rename(columns={'old':'new'})` - Rename columns
- `sort_values(by='col')` - Sort DataFrame by column
- `reset_index()` - Reset index to default integer index
- `set_index('col')` - Set a column as index

## Selection / Access
- `loc[row_indexer, col_indexer]` - Label-based selection
- `iloc[row_indexer, col_indexer]` - Position-based selection
- `at[row_label, col_label]` - Get scalar value by label
- `iat[row_idx, col_idx]` - Get scalar value by integer position
- `[]` - Select column(s) by name

## Filtering / Boolean Indexing
- `df[df['col'] > value]` - Filter rows by condition
- `df[(df['col1'] > x) & (df['col2'] < y)]` - Multiple conditions
- `isin([values])` - Filter rows where column value is in list
- `notna()` / `isna()` - Filter rows based on null values

## Aggregation / Grouping
- `groupby('col')` - Group DataFrame by column
- `sum()` - Sum values
- `mean()` - Average values
- `count()` - Count non-null entries
- `agg({'col': 'func'})` - Apply aggregation function

## Transformation / Manipulation
- `astype('type')` - Change column type
- `fillna(value)` - Fill missing values
- `dropna()` - Remove missing values
- `apply(func)` - Apply function to column or row
- `map(func)` - Map function to Series
- `replace(to_replace, value)` - Replace values

## Combining / Merging
- `concat([df1, df2], axis=0/1)` - Concatenate DataFrames
- `merge(df2, on='col', how='inner/left/right/outer')` - Merge DataFrames
- `join(df2, on='col', how='left')` - Join DataFrames

## Input / Output
- `read_csv('file.csv')` - Read CSV file
- `to_csv('file.csv', index=False)` - Write DataFrame to CSV
- `read_excel('file.xlsx')` - Read Excel file
- `to_excel('file.xlsx', index=False)` - Write DataFrame to Excel
