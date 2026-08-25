'''
Task 7: Regression Plots
Dateset Name: Auto Insurance
DatasetLink: https://www.kaggle.com/datasets/ranja7/vehicle-insurance-customer-data
'''

import seaborn as sns  
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("AutoInsurance.csv")

# regression plot between two num columns
plt.figure(figsize=(8,5))
sns.regplot(data=df, x="Income", y="Total Claim Amount")
plt.title("Regression Plot")
plt.show()

# implot with hue
sns.lmplot(data=df, x="Income",y="Total Claim Amount", hue="Response")
plt.show()
