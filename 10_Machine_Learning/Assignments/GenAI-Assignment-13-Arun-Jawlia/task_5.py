'''
Part 2 : Date Preprocessing and Cleaning ( Kaggle Dataset)
Task 5: Understanding the Data
'''

import pandas as pd

df = pd.read_csv('housing.csv')

print( "Shapee",df.shape)

print("Top 5 Rows" ,df.head())

print( "Overall Datatypes",df.info())

print("Datatypes" ,df.dtypes)

print("Columns" ,df.columns)

numerical_columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value',]

numerical_cols = df.select_dtypes(include=[float]).columns

categorical_columns = ["ocean_proximity"]

categorical_cols = df.select_dtypes(include=['object', 'category',]).columns

print(list(numerical_cols))

print(list(categorical_cols))

print(df['longitude'].isnull().sum())
print(df['latitude'].isnull().sum())
print(df['housing_median_age'].isnull().sum())
print(df['total_rooms'].isnull().sum())
print(df['total_bedrooms'].isnull().sum())
print(df['population'].isnull().sum())
print(df['households'].isnull().sum())
print(df['median_income'].isnull().sum())
print(df['median_house_value'].isnull().sum())
print(df['ocean_proximity'].isnull().sum())


# Only total_bedrooms has 207 null values