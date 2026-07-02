'''
# Task 9: Bivariate Analysis
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Bank_Data.csv")

print(df.head())

# Separate columns
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

print(numerical_cols)

# Numerical vs Numerical
sns.scatterplot(data = df , x='Age', y ='Balance')
plt.title("Distributioni of Between age and population")
plt.show()


data = ['Age', 'Balance']
sns.heatmap(
    df[data].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.show()


# Categorical vs Numerical
sns.barplot(data = df , x='Marital', y ='Age')
plt.show()

sns.boxplot(data = df , x='Marital', y ='Age')
plt.show()


# Others
sns.regplot(
    x=df[numerical_cols[0]],
    y=df[numerical_cols[1]]
)

plt.show()