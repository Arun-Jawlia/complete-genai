import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("online_retail.csv")


print(df.head())

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Extract useful date features
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Day"] = df["InvoiceDate"].dt.day
df["Hour"] = df["InvoiceDate"].dt.hour

# Drop original date column
df.drop("InvoiceDate", axis=1, inplace=True)

# Label Encoding
le = LabelEncoder()

categorical_cols = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Country"
]

for col in categorical_cols:
    df[col] = le.fit_transform(df[col].astype(str))

# Separate Features and Target
X = df.drop("Quantity", axis=1)
Y = df["Quantity"]

print(df.head())


print("Features Shape :", X.shape)
print("Target Shape   :", Y.shape)