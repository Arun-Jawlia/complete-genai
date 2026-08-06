'''
Task 6: Categorical Plot
Dateset Name: Auto Insurance

DatasetLink: https://www.kaggle.com/datasets/ranja7/vehicle-insurance-customer-data
'''

import matplotlib.pyplot as plt 
import seaborn as sns  
import pandas as pd

df = pd.read_csv("AutoInsurance.csv")
# Bar
plt.figure(figsize=(7,5))
sns.barplot(data =df,x="Coverage",y ="Total Claim Amount")
plt.show()
# BoxPlot
plt.figure(figsize=(7,5))
sns.boxplot( data= df, x= "Coverage", y = "Total Claim Amount")
plt.show()

#Violin Plot
plt.figure(figsize=(7,5))
sns.violinplot(data=df, x="Coverage",y="Total Claim Amount")
plt.show()

# Count
plt.figure(figsize=(7,5))
sns.countplot( data = df, x="Coverage")
plt.show()