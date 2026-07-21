
'''
Task 4: Naive Bayes Classifier

Dataset Name: Titanic Data set
Link: https://www.kaggle.com/datasets/brendan45774/test-file

Target Column: Survived

'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

df  = pd.read_csv('data_classification.csv')

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

print(df.isnull().sum()) # NO null values

df = df.drop(columns=['Cabin', 'PassengerId'], axis = 1)
missing_percentage = (
    df.isnull().sum()
    / len(df)
) * 100
print(df.isnull().sum())
print(missing_percentage)

print(df.duplicated().sum()) # NO Duplicates
print(df.columns)

numerical_features = ["Pclass","Age","SibSp","Parch","Fare"]
categorical_features = ["Sex","Embarked"]

# pipeline
numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy='median')),
        ("scaling",StandardScaler())
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy='most_frequent')),
        ("encoder",OneHotEncoder(handle_unknown="ignore"))
    ]
)



# Combine Pipeline Transformer
features = ColumnTransformer(
    transformers=[
        ("numeric transformation", numeric_pipeline, numerical_features),
        ("categorical transformation", categorical_pipeline, categorical_features)
    ]
)

gaussian_model = Pipeline(
    steps=[("features", features),("regressor", GaussianNB())]
)

X = df.drop("Survived", axis= 1)
Y = df['Survived']

X_train, X_test, Y_train, Y_test  = train_test_split(X,Y, test_size=0.2)



gaussian_model.fit(X_train, Y_train)

y_predict = gaussian_model.predict(X_test)
print("Actual value" ,Y_test.head())
print("Predicted values" ,y_predict[:5])

print("Naive Bayes Accuracy:",accuracy_score(Y_test, y_predict))