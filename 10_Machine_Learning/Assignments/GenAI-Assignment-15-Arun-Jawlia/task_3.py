
# PART 2 Classification ALgorithms
'''
# Task3: Logistic Regression
Dataset Name: Titanic Data set
Link: https://www.kaggle.com/datasets/brendan45774/test-file

Target Column: Survived

'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score

df  = pd.read_csv('data_classification.csv')

print(df.head())
print(df.shape)

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
num_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy='median')),
        ("scaling",StandardScaler())
    ]
)

cat_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy='most_frequent')),
        ("encoder",OneHotEncoder(handle_unknown="ignore"))
    ]
)


# Combine Pipeline Transformer
preprocessor = ColumnTransformer(
    transformers=[
        ("numeric transformation", num_pipeline, numerical_features),
        ("categorical transformation", cat_pipeline, categorical_features)
    ]
)

logistic_model = Pipeline(
    steps=[("features", preprocessor),("regressor", LogisticRegression())]
)

X = df.drop("Survived", axis= 1)
Y = df['Survived']

X_train, X_test, Y_train, Y_test  = train_test_split(X,Y, test_size=0.2)

print(X_train.shape)
print(X_test.shape)
logistic_model.fit(X_train, Y_train)

y_predict = logistic_model.predict(X_test)

print("Actual value" ,Y_test.head())
print("Predicted values" ,y_predict[:5])
print("Naive Bayes Accuracy:",accuracy_score(Y_test, y_predict))