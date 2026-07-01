#pylint: disable = all

'''
Task 2 : Load Dataset From JSON
'''

import pandas as pd

df = pd.read_json('employees.json')

print(df)
print(df.head())
print(df.dtypes)
print(type(df))