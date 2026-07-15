
'''
Task 5: Standardization ( StandardScaler)
'''

import pandas as pd
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

df  = pd.read_csv('online_retail.csv')

print(df.head())

print(df.info())

numerical_features = ['Quantity', 'UnitPrice', 'CustomerID']

categorical_features = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "InvoiceDate",
    "Country"
]

scaled_data = ss.fit_transform(df[numerical_features])

scaled_df = pd.DataFrame(
    scaled_data,
    columns=numerical_features
)

print(scaled_df.head())
print("Mean Value",scaled_df.mean())
print("Standard Deviation" ,scaled_df.std())