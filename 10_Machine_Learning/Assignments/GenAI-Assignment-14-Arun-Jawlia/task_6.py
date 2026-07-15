
'''
Task 5: Standardization ( StandardScaler)
'''

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

mm = MinMaxScaler()
ss = StandardScaler()

df  = pd.read_csv('online_retail.csv')

print(df.head())

print(df.info())

numerical_features = ['Quantity', 'UnitPrice', 'CustomerID']


minmax_data = mm.fit_transform(df[numerical_features])
stdscaler_data = ss.fit_transform(df[numerical_features])

scaled_minmax_df = pd.DataFrame(
    minmax_data,
    columns=numerical_features
)
scaled_std_df = pd.DataFrame(
    stdscaler_data,
    columns=numerical_features
)

print('Minmax')
print(scaled_minmax_df.head())

print("Standard Scaler")
print(scaled_std_df.head())