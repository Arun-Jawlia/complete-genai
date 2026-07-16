
'''
Dataset Name: Sales Data
Link: https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

Target Column: Amount

'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
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

X = df.drop("Amount", axis = 1)
y = df["Amount"]

print(X.isnull().sum()) # No null values


X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2, random_state=42
)

print(X_train.shape)
print(X_test.shape)

# pipeline
numeric_pipeline = Pipeline(
    steps=[
        (
            "imputer", SimpleImputer(strategy='median')
        ),
        (
            "scaler",StandardScaler()
        )
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        (
            "imputer", SimpleImputer(strategy='most_frequent')
        ),
        (
            "encoder",OneHotEncoder(handle_unknown="ignore")
        )
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("numerical", numeric_pipeline, numerical_features),
        ("categorical", categorical_pipeline, categorical_features)
    ]
)

model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)

model = model_pipeline.fit(X_train, y_train)
y_predicted = model.predict(X_test)

print("Accuracy :", mean_absolute_error(y_test, y_predicted))
