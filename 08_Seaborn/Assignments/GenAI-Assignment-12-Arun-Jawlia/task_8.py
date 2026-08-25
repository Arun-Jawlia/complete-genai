'''
Task 8: Multi plots and Figure Level plots
Dateset Name: Auto Insurance

DatasetLink: https://www.kaggle.com/datasets/ranja7/vehicle-insurance-customer-data
'''

import seaborn as sns  
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("AutoInsurance.csv")

#facet plot
g = sns.FacetGrid(df, col="Gender", height=5)
g.map_dataframe(sns.scatterplot,x="Income", y="Total Claim Amount")
plt.show()

g = sns.FacetGrid(df,row="Response",height=4)
g.map_dataframe(sns.scatterplot,x="Income",y="Total Claim Amount")
plt.show()


# Relplot
sns.relplot(data=df,x="Income",y="Total Claim Amount",hue="Response",col="Gender",kind="scatter")
plt.show()


# catplot
sns.catplot(data=df,x="Coverage",y="Total Claim Amount",kind="box",hue="Response")
plt.show()

# displot

sns.displot(data=df,x="Income",hue="Response",kde=True)
plt.show()