
'''
Task 6: Normalization (MinMax Scaler)

Dataset Name: Sales Data
Link: https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

Target Column: Amount

'''

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

mm = MinMaxScaler()
ss = StandardScaler()

df  = pd.read_csv('data.csv')

print(df.head())
print(df.info())
print(df.tail())

# Convert Amount to Numeric
df['Amount'] = df['Amount'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)
# Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day Name'] = df['Date'].dt.day_name

numerical_features = [ 'Amount','Boxes Shipped']
categorical_features = ["Sales Person","Country","Product"]


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