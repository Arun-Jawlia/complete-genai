'''
Task 3: Distribution Plot 
Dateset Name: Auto Insurance
DatasetLink: https://www.kaggle.com/datasets/ranja7/vehicle-insurance-customer-data
'''

import seaborn as sns  
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("AutoInsurance.csv")
#histogram
plt.figure(figsize= (7,5))
sns.histplot(df["Income"])
plt.title("Histogram")
plt.show()

# kde 
plt.figure(figsize = (7,5))
sns.kdeplot(df["Income"], fill=True)
plt.title("KDE Plot")
plt.show()

# Rug 
plt.figure(figsize = (7,5))
sns.rugplot(df["Income"])
plt.title("Rug Plot")
plt.show()

# Hist +KDE
plt.figure(figsize = (7,5))
sns.histplot(df["Income"], kde=True)
plt.title("Histogram + KDE")
plt.show()