#pylint: disable = all
# Task 3: Bar Plot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate Sales.csv')

print(df.head())

# Clean Amount Column
df['Amount'] = df['Amount'].str.strip("$")

df['Amount'] = df['Amount'].str.replace(",", '')

df['Amount'] = df['Amount'].astype("float").astype("int32")

data = df.groupby("Country")['Amount'].sum()

print(data)

x = data.index
y = data.values

# Create Vertical Bar  Plot
plt.figure(figsize = ( 10, 5))

plt.title("Distribution of Amount as Per Country")

plt.xlabel("Country")

plt.ylabel("Amount")

plt.bar(x, y, width = 0.5)

plt.grid()

plt.show()

# ------------------------------------
# Create Horizontal Bar  Plot
plt.figure(figsize = ( 10, 5))

plt.title("Distribution of Amount as Per Country")

plt.xlabel("Country")

plt.ylabel("Amount")

plt.barh(x, y, width = 0.5)

plt.grid()

plt.show()