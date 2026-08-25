# Task 1: Creating NumPy Arrays

import numpy as np

arr1 = np.arange(1, 11)
arr2 = np.arange(1, 10).reshape(3, 3)
arr3 = np.array([10, 20, 30, 40, 50])

print(arr1)
print(arr2)
print(arr3)

# Shape of Arrays
print("arr1 shape:", arr1.shape)
print("arr2 shape:", arr2.shape)
print("arr3 shape:", arr3.shape)

# Datatypes of Arrays
print("\nData Types:")
print("arr1 dtype:", arr1.dtype)
print("arr2 dtype:", arr2.dtype)
print("arr3 dtype:", arr3.dtype)