'''
Part 2 : Date Preprocessing and Cleaning ( Kaggle Dataset)
Task 5: Understanding the Data
'''

import pandas as pd

df = pd.read_csv('unclean.csv')

print(df.shape)

print(df.head())

print(df.info())

print(df.dtypes)

print(df.columns)

numerical_columns = ['PassengerId', 'Survived', 'Pclass','Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin',]

numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

categorical_columns = ["Name",'Sex', 'Embarked']

categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns

print(list(numerical_cols))

print(list(categorical_cols))

print(df['PassengerId'].isnull().sum())
print(df['Survived'].isnull().sum())
print(df['Pclass'].isnull().sum())
print(df['Age'].isnull().sum())
print(df['SibSp'].isnull().sum())
print(df['Ticket'].isnull().sum())
print(df['Parch'].isnull().sum())
print(df['Fare'].isnull().sum())
print(df['Cabin'].isnull().sum())
print(df['Sex'].isnull().sum())
print(df['Embarked'].isnull().sum())