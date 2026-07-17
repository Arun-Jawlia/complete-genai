
# PART 1 Regression Algorithm
# Task 1: Regression Evaluation Metrics
'''
Dataset Name: Sales Data
Link: https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

Target Column: Amount

'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    root_mean_squared_error
)

df  = pd.read_csv('data_regression.csv')

print(df.head())
print(df.shape)
print(df.info())

# Convert Amount to Numeric
df['Amount'] = df['Amount'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)
# Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day Name'] = df['Date'].dt.day_name
df.drop("Date", axis=1, inplace=True)

# Categories feature
numerical_features = [ 'Year', "Month", 'Day','Boxes Shipped']
categorical_features = ["Sales Person","Country","Product","Day Name"]

print(df.isnull().sum()) # No null values
print(df.duplicated().sum()) # No Duplicates

# pipeline
Numeric_Pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy='median')),
        ("scaling",StandardScaler())
    ]
)

Categorical_Pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy='most_frequent')),
        ("encoder",OneHotEncoder(handle_unknown="ignore"))
    ]
)
# Combine Pipeline Transformer
features = ColumnTransformer(
    transformers=[
        ("numeric transformation", Numeric_Pipeline, numerical_features),
        ("categorical transformation", Categorical_Pipeline, categorical_features)
    ]
)

model = Pipeline(
    steps=[("features", features),("regressor", LinearRegression())]
)


print(model)

X = df.drop("Amount", axis= 1)
Y = df['Amount']

X_train, X_test, Y_train, Y_test  = train_test_split(X,Y, test_size=0.2)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

model.fit(X_train, Y_train)

Y_predict = model.predict(X_test)

print("Mean Absolute error", mean_absolute_error(Y_test, Y_predict))
print("Mean sqaured error", mean_squared_error(Y_test, Y_predict))
print("Root Mean Squared error",root_mean_squared_error(Y_test, Y_predict))