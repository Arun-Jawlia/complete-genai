'''
# Task 8: Univariate Analysis
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

# Univariate Analysis
sns.histplot(data = df , x='Age')
plt.title("Distributioni of Between age and population")
plt.show()

sns.kdeplot(data = df , x='Balance')
plt.title("Distributioni of Between age and population")
plt.show()


print(categorical_cols)

# Count plot for Categorical Columns
sns.countplot(data = df, x ='Marital')
plt.show()

sns.countplot(data = df, x ='Education')
plt.show()


# Outliers detection

sns.boxplot(data = df, x ='Education')
plt.show()

sns.boxplot(data = df, x ='Marital')
plt.show()