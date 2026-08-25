#pylint: disable = all

# Pie Chart ( Market Share )

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate Sales.csv')

# Clean Amount Column
df['Amount'] = df['Amount'].str.strip("$")

df['Amount'] = df['Amount'].str.replace(",", '')

df['Amount'] = df['Amount'].astype("float").astype("int32")

dt = df.groupby('Country')['Amount'].sum()


# Plot Pie Chart
plt.figure(figsize=(12,6))

plt.title("Percentage Contribution of Countries in Total Sales")

plt.pie(dt, labels = dt.index, autopct='%0.1f%%')

plt.legend()

plt.show()