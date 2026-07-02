
# PART 1 FEATURE ENGINEERING
# Handing Data and Text Features 

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


# Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day Name'] = df['Date'].dt.day_name


df["Sales Person Length"] = df["Sales Person"].str.len()
df["Product Word Count"] = df["Product"].str.split().str.len()

print(df.head())