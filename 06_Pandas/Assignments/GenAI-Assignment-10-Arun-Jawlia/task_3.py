# Python Functionalities in Series

import pandas as pd

marks = [78,85,90,66,72]

marks_series = pd.Series(marks)

max_marks = marks_series.max()
min_marks = marks_series.min()
sum_of_marks = marks_series.sum()
mean_marks = marks_series.mean()

print("Maximum marks: ", max_marks)
print("Minimum marks: ", min_marks)
print("Sum of all marks: ", sum_of_marks)
print("Mean of all marks: ", mean_marks)


passed_marks = marks_series.apply(lambda x: x >=70)
print("Passed: ", passed_marks)

print("No of student passed: ", passed_marks.sum() )