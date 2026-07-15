
'''
Task 4: Column Transformer
'''

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

df  = pd.read_csv('online_retail.csv')

print(df.head())

print(df.info())

numerical_features = ['Quantity', 'UnitPrice', 'CustomerID']

categorical_features = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "InvoiceDate",
    "Country"
]

numerical_pipeline = Pipeline(
    steps = [
        (
            'scaler',
            StandardScaler()
        )
    ]
)
categorical_pipeline = Pipeline(
    steps = [
        (
            'encoder',
            OneHotEncoder(
                handle_unknown='ignore'
            )
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