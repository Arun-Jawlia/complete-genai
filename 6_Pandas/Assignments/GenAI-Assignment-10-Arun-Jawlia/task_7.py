# Grouping and Basic Analysis

import pandas as pd

# Student Dictionary
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("Average Marks per subject")
avg_marks = df.groupby("Subject")['Marks'].mean()
print(avg_marks)


print("\n count number fo students per subject")
student_count = df.groupby('Subject')['Name'].count()
print(student_count)

print("\n maximum marks per subject")
max_marks = df.groupby('Subject')['Marks'].max()
print(max_marks)