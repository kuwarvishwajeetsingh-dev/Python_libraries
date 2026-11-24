import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name':  ['Amit', 'Riya', 'Karan', 'Sneha'],
    'Marks': [85, 92, 78, 88],
    'City':  ['Delhi', 'Noida', 'Delhi', 'Pune'],
    'State':  ['Delhi', 'UP', 'Delhi', 'Mumbai'],
    'Ph No':  ['1232345678', '9876543210', '1234567890', '0987654321']
}
df = pd.DataFrame(data)
print(df)

print("-----------------------------")
df.to_csv("students.csv", index=False)    # save as students.csv
df = pd.read_csv("students.csv")          # now this file exists
df.to_excel("data.xlsx", index=False)
df = pd.read_excel("data.xlsx")
print(df)
print("-----------------------------")
df.head()        # first 5 rows
df.tail(2)       # last 2 rows
df.shape         # (rows, columns)
df.info()        # column types, null counts
df.describe()    # count, mean, std, min, max for numeric columns
df.columns       # column names
print("-----------------------------")
print("Selecting data")
df['Name']              # one column  (returns Series)
df[['Name', 'Marks']]   # multiple columns (returns DataFrame)

df.loc[0]               # row by LABEL
df.iloc[0]              # row by POSITION
df.loc[1, 'Marks']      # 92
df.iloc[1, 1]           # 92
print("-----------------------------")
print("Filtering data")
df[df['Marks'] > 80]    # rows where Marks > 80
print(df[df['Marks'] > 80])
df['Grade'] = ['B', 'A', 'C', 'B']      # new column
print(df)
df['Marks'] = df['Marks'] + 5           # modify
print(df)
df = df.drop('Grade', axis=1)           # delete column (axis=1)
print(df)
df = df.drop(0, axis=0)                 # delete row (axis=0)
print(df)
print("-----------------------------")
print("Sorting and Grouping")

df.sort_values('Marks', ascending=False)
print(df.sort_values('Marks', ascending=False))

df.groupby('City')['Marks'].mean()     # average marks per city
print(df.groupby('City')['Marks'].mean())
print("-----------------------------")
print("Plotting histogram of Marks")
plt.hist(df['Marks'], bins=4, edgecolor='black')
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.show()