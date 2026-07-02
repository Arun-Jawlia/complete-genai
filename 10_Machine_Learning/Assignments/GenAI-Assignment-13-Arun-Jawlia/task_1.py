#pylint: disable = all

'''
Task 1 : Load Dataset From CSV
'''

import pandas as pd

df = pd.read_csv("Bank_Data.csv")

# Shape of the dataset
print(df.shape)

# Columns Name
print(df.columns)

# First 5 Rows
print(df.head())

# Last 5 Rows
print(df.tail())

# Any Sample 5 Rows
print(df.sample(5))

# Describe
print(df.describe())

# Information 
print(df.info())

# Data Types
print(df.dtypes)