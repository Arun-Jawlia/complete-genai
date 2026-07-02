'''
Part 6: Data Cleaning
'''

import pandas as pd

df = pd.read_csv('unclean.csv')

print(df.shape)

print(df.head())

print(df.dtypes)

print(df.info())

# print(df.columns)
df = df[['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']]

print(df.describe())

print(df.duplicated().sum())

print(df.drop_duplicates())

print(df.isnull().sum())

# Age Column has 86 null values
print(df['Age'].isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df['Age'].isnull().sum())

# Cabin has 327 Missing Value
print(df['Cabin'].isnull().sum())

df['Cabin'] = df['Cabin'].fillna('Unknown')

print(df['Cabin'].isnull().sum())


# Fare has 1 missing value
print(df['Fare'].isnull().sum())

df['Fare'] = df['Fare'].fillna(df['Fare'].mean())

print(df['Fare'].isnull().sum())

print(df.info())

print(df.isnull().sum())