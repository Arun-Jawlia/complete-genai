'''
Task 7: Feature Engineering
'''

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

df = pd.read_csv('Bank_Data.csv')

print(df.head())

# print(df.info())
le = LabelEncoder()
oe = OrdinalEncoder()
ohe = OneHotEncoder()

# Label Encoding on Binary Cols
df["Default"] = le.fit_transform(df["Default"])
df["Housing"] = le.fit_transform(df["Housing"])
df["Loan"] = le.fit_transform(df["Loan"])
df["TARGET"] = le.fit_transform(df["TARGET"])

# Ordinal Encoder 
education_order = [['unknown', 'primary', 'secondary', 'tertiary']]
oe = OrdinalEncoder(categories = education_order)
df[['Education']] = oe.fit_transform(df[['Education']])

# Nominal Encoding
nominal_cols = ['Job', 'Marital','contact', 'Month', 'poutcome']
ohe = OneHotEncoder(sparse_output=False, handle_unknown = 'ignore')
encoded = ohe.fit_transform(df[nominal_cols])
encoded_df = pd.DataFrame(
    encoded,
    columns=ohe.get_feature_names_out(nominal_cols)
)

df = df.drop(columns=nominal_cols)

df = pd.concat(
    [df, encoded_df],
    axis=1
)

print(df.head())

X = df.drop("TARGET", axis=1)
Y = df["TARGET"]

print("Features Shape :", X.shape)
print("Target Shape   :", Y.shape)