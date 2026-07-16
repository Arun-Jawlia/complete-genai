
# PART 1 FEATURE ENGINEERING
# Task 2: Handing Data and Text Features ( if Available)
'''
Dataset Name: Sales Data
Link: https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

Target Column: Amount

'''

import pandas as pd
import numpy as np

df  = pd.read_csv('data.csv')

print(df.head())

# Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day Name'] = df['Date'].dt.day_name

# Sales Person
df["Sales Person Length"] = df["Sales Person"].str.len()
df["Product Word Count"] = df["Product"].str.split().str.len()

print(df.head())