# Important DataFrame Functions
import pandas as pd

# Student Dictionary
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("Info Function of Dataframe")
print(df.info())

print('\n Describe Function of Dataframe')
print(df.describe())

print("\n Head Function")
print(df.head()) # top 5 rows

print("\n tail function")
print(df.tail()) # last 5 rows

print("\n Sort Student by descending order")
sort_by_marks = df.sort_values(by="Marks", ascending=False)
print(sort_by_marks)

print("\n Reset index after sorting")
reset_after_sorting = sort_by_marks.reset_index(drop=True)
print(reset_after_sorting)