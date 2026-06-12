#pylint: disable = all
# Task 4: Multiple Bar Plot

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Chocolate Sales.csv')

print(df.head())

# Date Co
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

df['Date']= df['Date'].dt.month_name()

df['Date']= df['Date'].astype("category")

# Clean Amount Column
df['Amount'] = df['Amount'].str.strip("$")

df['Amount'] = df['Amount'].str.replace(",", '')

df['Amount'] = df['Amount'].astype("float").astype("int32")


s1 = df[(df['Product'] == 'Mint Chip Choco')]
s2 = df[(df['Product'] == 'Peanut Butter Cubes')]
s3 = df[(df['Product'] == '85% Dark Bars')]


d1 = s1.groupby('Date')['Amount'].sum()
d2 = s2.groupby('Date')['Amount'].sum()
d3 = s3.groupby('Date')['Amount'].sum()

d1.index = pd.CategoricalIndex(d1.index, categories=['January', "February", "March", 'April', 'May', 'June', "July", 'August'], ordered=True)
d2.index = pd.CategoricalIndex(d2.index, categories=['January', "February", "March", 'April', 'May', 'June', "July", 'August'], ordered=True)
d3.index = pd.CategoricalIndex(d3.index, categories=['January', "February", "March", 'April', 'May', 'June', "July", 'August'], ordered=True)

d1.index = d1.index.sort_values()
d2.index = d2.index.sort_values()
d3.index = d3.index.sort_values()

x=['January', 'February', 'March', 'April', 'May', 'June','July', 'August']

# Create Multi Bar  Plot
plt.figure(figsize=(12,4))

plt.title("Product and Amount Distribution ")

plt.xlabel("Month Name")

plt.ylabel("Products")

plt.bar(np.arange(d1.shape[0]) - 0.2, d1.values, color='green', label = 'Mint Chip Choco', width = 0.2)
plt.bar(np.arange(d2.shape[0]), d2.values, color='blue', label = 'Penaut Butter', width=0.2)
plt.bar(np.arange(d3.shape[0]) + 0.2, d3.values, color='red', label = '85% Dark Bars', width=0.2)
plt.xticks(np.arange(d1.shape[0]) - 0.2, x)

plt.legend()

# plt.grid()

plt.show()