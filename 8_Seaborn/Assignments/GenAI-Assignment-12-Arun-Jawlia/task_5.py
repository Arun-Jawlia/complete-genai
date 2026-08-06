'''
Task 5: Matrix Plot

Dateset Name: Auto Insurance
DatasetLink: https://www.kaggle.com/datasets/ranja7/vehicle-insurance-customer-data
'''

import seaborn as sns  
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("AutoInsurance.csv")

sns.pairplot(df[["Income","Customer Lifetime Value","Monthly Premium Auto","Total Claim Amount"]])
plt.show()


plt.figure(figsize=(8,6))
corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()