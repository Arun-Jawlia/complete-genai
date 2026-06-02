# Task 1: Pandas Series Basics

import pandas as pd

marks = [78,85,90,66,72]

series = pd.Series(marks)
series_values = series.values
index_values = series.index
datatype = series.dtype

print("Series from list: ", series)
print("Indexes: ", index_values)
print("Series Values", series_values)
print("Data type of Series", datatype)

print("First Element: ", series[0])
print("Last Two Element: ", series[-2:])