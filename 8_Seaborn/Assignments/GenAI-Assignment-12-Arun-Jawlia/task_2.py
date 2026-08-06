'''
Task 2: Line Plot as Scatter and Facet

Dateset Name: Auto Insurance
DatasetLink: https://www.kaggle.com/datasets/ranja7/vehicle-insurance-customer-data

'''
import seaborn as sns  
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("AutoInsurance.csv")

# Line plot as Scatter
sns.lineplot(data=df, x ='Months Since Policy Inception', y='Total Claim Amount')
plt.show()

# Line plot as Facet
sns.relplot(data=df , x= 'Months Since Policy Inception', y='Total Claim Amount', kind='scatter')
plt.show()

# Line plot as Facet by Gender
sns.relplot(data=df , x = 'Months Since Policy Inception', y='Total Claim Amount',col='Gender', kind='scatter')
plt.show()
