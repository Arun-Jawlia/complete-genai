# Create a DataFrame
import pandas as pd

# Student Dictionary
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("Type of dataframe", type(df))

first_3_rows = df.head(3)
last_2_rows = df.tail(2)
dataframe_shape = df.shape
columns_names = df.columns

print("First 3 Rows")
print(first_3_rows)
print("\nLast 2 Rows")
print(last_2_rows)
print("\nDataframe Shape: ", dataframe_shape)
print("\nColumns Name: ", columns_names)