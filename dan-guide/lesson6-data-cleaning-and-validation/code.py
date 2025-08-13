#! SECTION 1: Import Pandas
import pandas as pd
import numpy as np

def wait():
    input("\nPress Enter to continue...\n")

#! SECTION 2: Fixing Phone Numbers
data = {'Name': ['Tom', 'Dick', 'Harry', 'Mary'],
        'Phone': [3212347890, '(212)555-8888', '752-9103','8659134568']}
df = pd.DataFrame(data)
df['Correct Phone'] = df['Phone'].astype(str)

def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ''
        for c in phone:
            if c in '0123456789':
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None

print("# Before fixing phones")
print(df)
wait()

df['Correct Phone'] = df['Correct Phone'].map(fix_phone)

print("# After fixing phones")
print(df)
wait()

#! SECTION 3: Using Built-in Numpy/Pandas Functions
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [20, 22, 43]}
df2 = pd.DataFrame(data)

print("# Before increasing age")
print(df2)
wait()

df2['Age'] = df2['Age'] + 1

print("# After increasing age")
print(df2)
wait()

#! SECTION 4: Data Discretization
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'Grade': [78, 40, 85]}
df3 = pd.DataFrame(data)

print("# Before discretization")
print(df3)
wait()

df3['Grade'] = pd.cut(df3['Grade'], 3, labels = ["bad", "okay", "great"])

print("# After discretization")
print(df3)
wait()

#! SECTION 5: Removing Duplicates
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 32],
        'Score': [85, 92, 85, 76]}
df4 = pd.DataFrame(data)

print("# Original DataFrame with duplicates")
print(df4)
wait()

df_cleaned = df4.drop_duplicates()
print("# After removing exact duplicates")
print(df_cleaned)
wait()

df_cleaned_by_name = df4.drop_duplicates(subset='Name')
print("# After removing duplicates based on Name")
print(df_cleaned_by_name)
wait()

#! SECTION 6: Handling Outliers
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 200, 43, -5]}
df5 = pd.DataFrame(data)

print("# Before handling outliers")
print(df5)
wait()

median_age = df5['Age'].median()
df5['Age'] = df5['Age'].apply(lambda x: median_age if x > 100 or x < 0 else x)

print("# After handling outliers")
print(df5)
wait()

#! SECTION 7: Data Transformation
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['20', '22', '43']}
df6 = pd.DataFrame(data)

print("# Before type conversion")
print(df6)
wait()

df6['Age'] = df6['Age'].astype(int)

print("# After type conversion")
print(df6)
wait()

# Example of converting dates (no error handling here)
data = {'Name': ['Alice', 'Bob'], 'JoinDate': ['2020-01-01', '2020-02-15']}
df7 = pd.DataFrame(data)

print("# Before converting JoinDate to datetime")
print(df7)
wait()

df7['JoinDate'] = pd.to_datetime(df7['JoinDate'])

print("# After converting JoinDate to datetime")
print(df7)
wait()


#? cheatsheet download -> https://drive.google.com/file/d/1FvreYeQYWN0oTC6He-7adNqhl_Qu-5SK/view?usp=sharing