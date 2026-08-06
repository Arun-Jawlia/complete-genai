
'''
Task 1: Relational Plot

Dateset Name: Auto Insurance
DatasetLink: https://www.kaggle.com/datasets/ranja7/vehicle-insurance-customer-data

'''
import pandas as pd
import seaborn as sns  
import matplotlib.pyplot as plt 

df = pd.read_csv("AutoInsurance.csv")
print(df.head())
print(df.info())

# Relational plot
sns.relplot(data=df, x='Income', y='Total Claim Amount', hue='Response', kind='line')
plt.show()

# Scatter Plot
sns.relplot(data=df, x= 'Income', y= 'Total Claim Amount', hue= 'Response', kind='scatter')
plt.show()
