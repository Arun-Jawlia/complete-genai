'''
Task 4: Bivariate Distribution Plot
Dateset Name: Auto Insurance

DatasetLink: https://www.kaggle.com/datasets/ranja7/vehicle-insurance-customer-data
'''

import seaborn as sns  
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("AutoInsurance.csv")

plt.figure(figsize=(8,6))
sns.histplot(data=df, x = "Income",y = "Total Claim Amount", bins=30)
plt.title(" bivariate Histogram")
plt.show()

plt.figure(figsize=(8,6))
sns.kdeplot(data= df, x ="Income", y="Total Claim Amount", fill=True, cmap="Blues")
plt.title(" bivariate KDE")
plt.show()