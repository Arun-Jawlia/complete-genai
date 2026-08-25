# Pandas plotting ( Simple Graphs)

import pandas as pd

# Student Dictionary
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

# Bar Graph
plot_bar_graph_names_vs_marks = df.plot(x='Name',y='Marks',kind='bar',title='Student Names vs Marks')
print(plot_bar_graph_names_vs_marks)

# Line Graph
plot_line_graph_of_marks = df['Marks'].plot(kind='line',title='Marks Line Graph')

print(plot_line_graph_of_marks)

# Histogram
plot_histogram_of_marks = df['Marks'].plot(kind='hist',title='Marks Histogram')
print(plot_histogram_of_marks)