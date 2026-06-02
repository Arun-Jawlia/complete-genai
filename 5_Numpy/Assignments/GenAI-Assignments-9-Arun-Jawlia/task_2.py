# Important Mathematical Opeartions

import numpy as np

A = np.array([10,20,30,40])
B = np.array([1,2,3,4])

addition = A + B
subtraction = A - B
multiplication = A * B
division = A / B
power_two = A ** B

print("Addition", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Divison: ", division)
print("Power: ", power_two)

print("-----")
#  Using NumPy Functions

print(np.add(A , B))
print(np.subtract(A , B))