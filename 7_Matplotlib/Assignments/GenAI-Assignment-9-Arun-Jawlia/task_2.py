#pylint: disable = all
# Task 1: Line Plot ( Sales Trend )

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate Sales.csv')

# Clean Amount Column
df['Amount'] = df['Amount'].str.strip("$")

df['Amount'] = df['Amount'].str.replace(",", '')

df['Amount'] = df['Amount'].astype("float").astype("int32")

df['Boxes Shipped'] = df['Boxes Shipped'].astype('int32')

x = df['Boxes Shipped'] 
y = df['Amount']

# Create Scatter  Plot
plt.figure(figsize = ( 10, 5))

plt.title("Distribution of Amount as Per Total Boxes Shipped")

plt.xlabel("Number of Boxes")

plt.ylabel("Amounnt")

plt.scatter(x, y, marker = 'o',  )

plt.grid()

plt.show()