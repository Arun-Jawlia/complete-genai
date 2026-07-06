'''
# Task 9: Bivariate Analysis
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("housing.csv")

print(df.head())

# Separate columns
numerical_cols = [
    "longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income","median_house_value"
]
categorical_cols = df.select_dtypes(exclude=[np.number]).columns

print("Numerical Columns" ,numerical_cols)
print("Categorical Columns" ,categorical_cols)

# Numerical vs Numerical

# Median Income vs Median House Valie
plt.figure(figsize=(8,5))
sns.scatterplot(data=df,x="median_income",y="median_house_value")
plt.title("Median Income vs Median House Value")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df,x="median_income",y="median_house_value",hue="housing_median_age")
plt.title("Income vs House Value")
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(df[numerical_cols].corr(),annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


# Categorical vs Categorical
plt.figure(figsize=(8,5))
sns.countplot(data=df,x="ocean_proximity")
plt.xticks(rotation=20)
plt.title("Count Plot")
plt.show()


# Categorical vs Numerical
plt.figure(figsize=(8,5))
sns.barplot(data=df,x="ocean_proximity",y="median_house_value")
plt.xticks(rotation=20)
plt.title("Average House Value by Ocean Proximity")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df,x="ocean_proximity",y="median_house_value")
plt.xticks(rotation=20)
plt.title("Box Plot")
plt.show()


