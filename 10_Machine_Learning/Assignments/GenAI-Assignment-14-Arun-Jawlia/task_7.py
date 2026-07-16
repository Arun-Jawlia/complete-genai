
'''
Task 7: Create a preprocessing pipeline

Dataset Name: Sales Data
Link: https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

Target Column: Amount

'''

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

df  = pd.read_csv('data.csv')

print(df.head())
print(df.info())

# Convert Amount to Numeric
df['Amount'] = df['Amount'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)
# Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day Name'] = df['Date'].dt.day_name


numerical_features = [ 'Amount','Boxes Shipped']
categorical_features = ["Sales Person","Country","Product"]

numerical_pipeline = Pipeline(
    steps = [
        (
            "imputer", SimpleImputer(strategy='median')
        ),
        (
            'scaler', StandardScaler()
        )
    ]
)
categorical_pipeline = Pipeline(
    steps = [
        (
            "imputer", SimpleImputer(strategy='most_frequent')
        ),
        (
            'encoder',OneHotEncoder(handle_unknown='ignore')
        )
    ]
)

preprocessor = ColumnTransformer(
    transformers = [
        (
            'numerical',
            numerical_pipeline,
            numerical_features
        ),
        (
            'categorical',
            categorical_pipeline,
            categorical_features
        )
    ]
)

X = preprocessor.fit_transform(df)

print("Original Shape :", df.shape)
print("Processed Shape :", X.shape)