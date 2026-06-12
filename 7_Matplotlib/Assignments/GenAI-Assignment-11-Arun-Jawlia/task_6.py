# pylint: disable = all 
# Task 6: Histogram ( Marks Distribution )

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('student_depression_dataset.csv')    

plt.figure(figsize=(10,5))

plt.title("Distribution of CGPA as the Students")

plt.xlabel("CGPA Range")

plt.ylabel("Number of Students")

plt.hist(df['CGPA'], bins = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
plt.show()