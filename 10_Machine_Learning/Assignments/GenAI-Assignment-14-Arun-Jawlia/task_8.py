
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("online_retail.csv")

print(df.head())
print(df.info())

# Target 
df['HighQuantity'] = (df['Quantity'] > 10).astype(int)
print(df["HighQuantity"].value_counts())

# Feature Engineering
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.month
df["Hour"] = df["InvoiceDate"].dt.hour
df["Weekday"] = df["InvoiceDate"].dt.dayofweek

X = df[
    [
        "UnitPrice",
        "CustomerID",
        "Country",
        "Month",
        "Hour",
        "Weekday"
    ]
]

y = df["HighQuantity"]

print(X.isnull().sum())

X['CustomerID'] = X['CustomerID'].fillna(X['CustomerID'].median())

print(X.isnull().sum())

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2, random_state=42
)

print(X_train.shape)
print(X_test.shape)

numerical_features = [
    "UnitPrice",
    "CustomerID",
    "Month",
    "Hour",
    "Weekday"
]

categorical_features = [
    "Country"
]

numeric_pipeline = Pipeline(
    steps=[
        (
            "scaler", 
            StandardScaler()
        )
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        (
            "encoder", 
            OneHotEncoder(handle_unknown="ignore")
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
        ("classifier", LogisticRegression(max_iter=1000))
    ]
)

model_pipeline.fit(X_train, y_train)

y_pred = model_pipeline.predict(X_test)

print("Accuracy :", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))