'''
# Task 8: Univariate Analysis
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("housing.csv")

print(df.head())

print(df.info())

# Separate columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
categorical_cols = df.select_dtypes(exclude=[np.number]).columns

print("Numerical Columns" ,numerical_cols)
print("Categorical Columns" ,categorical_cols)


print('Value Counts', df['ocean_proximity'].value_counts())
# Univariate Analysis
# Use Count plt for Catgorical Columns
# There is only category
plt.figure(figsize=(10,3))
sns.countplot(data = df, x='ocean_proximity')
plt.show()


# Plot distribution of Numerical Columns ( histogram + KDE )
plt.figure(figsize=(10,3))
sns.histplot(data = df, x='longitude', kde=True)
plt.show()

plt.figure(figsize=(10,3))
sns.histplot(data = df, x='latitude', kde=True)
plt.show()

plt.figure(figsize=(10,3))
sns.histplot(data = df, x='housing_median_age', kde=True)
plt.show()

plt.figure(figsize=(10,3))
sns.histplot(data = df, x='total_rooms', kde=True)
plt.show()

plt.figure(figsize=(10,3))
sns.histplot(data = df, x='total_bedrooms', kde=True)
plt.show()

plt.figure(figsize=(10,3))
sns.histplot(data = df, x='population', kde=True)
plt.show()

plt.figure(figsize=(10,3))
sns.histplot(data = df, x='households', kde=True)
plt.show()

plt.figure(figsize=(10,3))
sns.histplot(data = df, x='median_income', kde=True)
plt.show()

plt.figure(figsize=(10,3))
sns.histplot(data = df, x='median_house_value', kde=True)
plt.show()


#Outliers detection for Numerical Cols
plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='longitude')
plt.show()

plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='latitude')
plt.show()

plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='housing_median_age')
plt.show()

plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='total_rooms')
plt.show()

plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='total_bedrooms')
plt.show()

plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='population')
plt.show()

plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='households')
plt.show()

plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='median_income')
plt.show()

plt.figure(figsize=(10,3))
sns.boxplot(data = df, x='median_house_value')
plt.show()