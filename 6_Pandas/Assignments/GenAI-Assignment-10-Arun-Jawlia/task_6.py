# Filtering and Conditional Selection

import pandas as pd

# Student Dictionary
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)
print(df.dtypes)

print('Student who scored more than 75 marks')
scored_more_than_75_marks = df[df['Marks'] >= 75]
print(scored_more_than_75_marks)

print("\n Students belonging to subject maths")
stds_belongs_to_maths = df[df['Subject']== 'Math']
print(stds_belongs_to_maths)

print("\n Student scored more than average marks")
avg_marks = df['Marks'].mean()
print(avg_marks)
stds_more_than_avg_marks = df[df['Marks'] >= avg_marks]
print(stds_more_than_avg_marks)

print("\n Student who failed ( marks < 70 )")
failed_stds = df[df['Marks'] < 70]
print(failed_stds)