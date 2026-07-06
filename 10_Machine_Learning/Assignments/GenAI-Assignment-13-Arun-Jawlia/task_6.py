'''
Part 6: Data Cleaning
'''

import pandas as pd

df = pd.read_csv('housing.csv')

print( "Shapee",df.shape)

print("Top 5 Rows" ,df.head())

print( "Overall Datatypes",df.info())

print("Datatypes" ,df.dtypes)

print("Columns" ,df.columns)

# print(df.columns)
df = df[['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value', 'ocean_proximity']]

print(df.describe())

print(df.duplicated().sum())

print(df.drop_duplicates())

print(df.isnull().sum())

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


# Analysis 
# Only total_bedrooms has 207 null values and we can fill with median

df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())

print("Total Bedroom handled missing value using median", df['total_bedrooms'].isnull().sum())

print(df.info())