
'''
Task 4: Column Transformer ( Recommended way)

Dataset Name: Sales Data
Link: https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

Target Column: Amount

'''


import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

df  = pd.read_csv('data.csv')

print(df.head())
print(df.info())

target_column = ['Amount']
numerical_features = ['Amount','Boxes Shipped']
categorical_features = ["Sales Person","Country","Product"]

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