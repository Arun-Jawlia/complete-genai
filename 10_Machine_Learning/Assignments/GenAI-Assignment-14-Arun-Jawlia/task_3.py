
# PART 2 Feature Encoding
# Task3: One Hot Encoding
'''
Dataset Name: Sales Data
Link: https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

Target Column: Amount

'''

import pandas as pd
import numpy as np

df  = pd.read_csv('data.csv')

print(df.head())

categorical_cols = df.select_dtypes(include='object').columns

print("Categorical columns" ,categorical_cols)

encoded_df = pd.get_dummies(df, columns = categorical_cols, drop_first = True, dtype= int)

print("dummies first 5 rows" ,encoded_df.head())

print("dummies first 5 rows", encoded_df.shape)