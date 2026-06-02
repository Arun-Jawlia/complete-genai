# Percentiles and Sorting

import numpy as np

marks = np.array([78,85,90,66,72,88,95,60])

avg = np.mean(marks)
sorted_marks = np.sort(marks)
percentile_25 = np.percentile(marks, 25)
percentile_50 = np.percentile(marks, 50)
percentile_75 = np.percentile(marks, 75)

student_above_average_marks = np.sum(marks > avg)

print(sorted_marks)
print("25 Percentile:", percentile_25)
print("50 Percentile:", percentile_50)
print("75 Percentile:", percentile_75)

print("Average Marks:", avg)
print("Students Above Average:", student_above_average_marks)