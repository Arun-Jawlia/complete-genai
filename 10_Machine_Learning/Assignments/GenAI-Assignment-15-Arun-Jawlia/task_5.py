
'''
Task 5: Standardization ( StandardScaler)

Dataset Name: Sales Data
Link: https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

Target Column: Amount

'''

import pandas as pd
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

df  = pd.read_csv('data.csv')

print(df.head())
print(df.info())

# Convert Amount to Numeric
df['Amount'] = df['Amount'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)
# Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day Name'] = df['Date'].dt.day_name

target_column = ['Amount']
numerical_features = ['Boxes Shipped']
categorical_features = ["Sales Person","Country","Product"]

scaled_data = ss.fit_transform(df[numerical_features])

scaled_data = pd.DataFrame(scaled_data,columns=numerical_features)

print(scaled_data.head())
print("Mean Value",scaled_data.mean())
print("Standard Deviation" ,scaled_data.std())

'''
Mean becomes ~ 0
Standard deviation becomes ~ 0

because of formula = Z = (X - μ)/σ

X: raw data points
μ: the mean average 
σ: standard deviation 

standardscaler substract the mean from each numerical feature and divides it by the standard deviation.
After scaling, the transformed data has a mean close to 0 and a standard deviation close to 1. This ensure that features with
larget numerical range dont dominate features with smaller ranges.

'''