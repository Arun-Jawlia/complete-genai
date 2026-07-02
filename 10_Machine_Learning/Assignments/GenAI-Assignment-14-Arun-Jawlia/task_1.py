
# PART 1 FEATURE ENGINEERING
# CREATING NEW FEATURES

import pandas as pd
import numpy as np

df  = pd.read_csv('data.csv')

print(df.head())

#  Convert Amount to Numeric

df['Amount'] = df['Amount'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)


# Add new Feature : Price per Box
df['Price Per Box'] = df['Amount'] / df['Boxes Shipped']

#  Add New Feature: Revenue Category
df['Revenue Category'] = np.where(df['Amount']>= 1000, 'High', 'Low')

# Add New Feature: Boxex Category
df['Boxes Category'] = pd.cut(df['Boxes Shipped'],bins = [0,100,200,300,1000], labels = ['Low', 'Medium', 'High', 'Very High'])

print(df.head())

print(df.columns)