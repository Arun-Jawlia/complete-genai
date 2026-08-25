# Aggregation Operations

import numpy as np

data = np.array([[10,20,30], [40,50,60], [70,80,90]])

# for row --> axis = 1 and for column --< axis = 0
row_wise_sum = np.sum(data, axis = 1)
column_wise_sum = np.sum(data, axis = 0)
minimum_value = np.max(data)
maximum_value = np.min(data)
mean = np.mean(data)

print("row_wise_sum:", row_wise_sum) 
print("column_wise_sum:", column_wise_sum) 
print("minimum_value:", minimum_value)
print("maximum_value: ", maximum_value)
print("mean: ", mean)