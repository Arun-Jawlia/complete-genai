
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
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.impute import SimpleImputer

df = pd.read_csv("data.csv")

print(df.shape)
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
df.drop("Date", axis=1, inplace=True)

# Categories feature
numerical_features = [ 'Year', "Month", 'Day','Boxes Shipped']
categorical_features = ["Sales Person","Country","Product","Day Name"]

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

model.fit(X_train, Y_train)

Y_predict = model.predict(X_test)
print(mean_absolute_error(Y_test,  Y_predict))
print(mean_squared_error(Y_test, Y_predict))
print(r2_score(Y_test,Y_predict))