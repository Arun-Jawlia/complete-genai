#pylint: disable = all
# Task 1: Line Plot ( Sales Trend )

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate Sales.csv')

# Date Column
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

df['Date']= df['Date'].dt.month_name()

df['Date']= df['Date'].astype("category")


# Clean Amount Column
df['Amount'] = df['Amount'].str.strip("$")

df['Amount'] = df['Amount'].str.replace(",", '')

df['Amount'] = df['Amount'].astype("float").astype("int32")


sales_info = df.groupby('Date')['Amount'].sum()

sales_info.index = pd.CategoricalIndex(sales_info.index, categories=['January', 'February','March',"April", "May", "June", "July", "August"], ordered=True)

sales_info = sales_info.sort_index()
print(sales_info)

# Create Line Plot
plt.figure(figsize = ( 10, 5))

plt.title("Distribution of Montly Sales Trend")

plt.xlabel("Months")

plt.ylabel("Total Sales")

plt.plot(sales_info.index, sales_info.values, marker = 'o',  )

plt.grid()

plt.show()