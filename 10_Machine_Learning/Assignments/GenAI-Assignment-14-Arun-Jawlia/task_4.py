
'''
Task 4: Column Transformer
'''

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

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

preprocessor = ColumnTransformer(
    transformers = [
        (
            'categorical',
            OneHotEncoder(handle_unknown='ignore'),
            categorical_features
        )
    ]
)

X_transformed = preprocessor.fit_transform(df)

print("Orignal Shape", df.shape)
print("New Shape", X_transformed.shape)