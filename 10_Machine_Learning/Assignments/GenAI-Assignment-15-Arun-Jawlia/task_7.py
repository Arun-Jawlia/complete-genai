
'''
Task 6: Overfitting and Underfitting

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
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

df  = pd.read_csv('data_classification.csv')

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

print(df.isnull().sum())

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

X = df.drop("Survived", axis= 1)
Y = df['Survived']
X_train, X_test, Y_train, Y_test  = train_test_split(X,Y, test_size=0.2)

underfitting_model = Pipeline([
    ('features', features),
    ('classifier', DecisionTreeClassifier(max_depth=1, random_state=42))
])

# Underfit model
Underfit_model = underfitting_model.fit(X_train, Y_train)
train_predict = Underfit_model.predict(X_train)
train_accuracy = accuracy_score(Y_train, train_predict)

test_predict = underfitting_model.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_predict)
print("Training Accuracy for Underfitting Model", train_accuracy)
print("Testing Accuracy for Underfitting Model", test_accuracy)

# Overfitting model
overfitting_model = Pipeline([
    ('features', features),
    ('classifier', DecisionTreeClassifier(random_state=42))
])


Overfitting_model = overfitting_model.fit(X_train, Y_train)
train_predict = overfitting_model.predict(X_train)
train_accuracy = accuracy_score(Y_train, train_predict)

test_predict = overfitting_model.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_predict)
print("Training Accuracy for Overfitting Model", train_accuracy)
print("Testing Accuracy for Overfitting Model", test_accuracy)



'''
For Logistic regression:
model is simple. if its accuracy is much lower than expected, it may be underfitting becuase it can't caputre complex relation

for Gaussian NB: it assume feature independence, it may underfit if features are correlated

for KNN: small k can overfit by memorizing training data, Large K can underfit. the selected k balance bias and variance to make generalized model

'''