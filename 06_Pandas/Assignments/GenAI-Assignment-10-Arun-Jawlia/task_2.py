# Mathematical Operations on Series

import pandas as pd

marks = [78,85,90,66,72]

series = pd.Series(marks)

add_5_to_marks = series + 5
subtract_2_to_marks = series - 2
multiplied_marks = series * 1.05
divided_by_2 = series / 2

print("Add 5 marks to all students: ", add_5_to_marks)
print("Subtract 2 from all values: ", subtract_2_to_marks)
print("Multiple all values by 1.05: ", multiplied_marks)
print("Divide all marks by 2: ", divided_by_2)