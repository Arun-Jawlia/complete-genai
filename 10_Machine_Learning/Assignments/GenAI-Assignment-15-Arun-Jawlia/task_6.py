
'''
Task 5: K-Nearest Neighbors (KNN)

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
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score,
    precision_score
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

df  = pd.read_csv('data_classification.csv')

# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())

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

model_logistic_Regresson = Pipeline(
    steps=[("features", features),("regressor", LogisticRegression())]
)

model_Gaussian_NB = Pipeline(
    steps=[("features", features),("regressor", GaussianNB())]
)

X = df.drop("Survived", axis= 1)
Y = df['Survived']
X_train, X_test, Y_train, Y_test  = train_test_split(X,Y, test_size=0.2)


k_values = [3,5, 7,9]

result = {}

for k in k_values:
    model = Pipeline(
        steps= [
            ('features',features), ('knn', KNeighborsClassifier(n_neighbors = k))
        ]
    )

    model.fit(X_train, Y_train)
    y_predict = model.predict(X_test)

    accuracy = accuracy_score(Y_test, y_predict)

    result[k] = accuracy


best_k_value = max(result,key= result.get)
best_knn_accuracy = result[best_k_value]

knn_model = Pipeline(
    steps= [
        ('features',features), ('knn', KNeighborsClassifier(n_neighbors = best_k_value))
    ]
)


model_logistic_Regresson.fit(X_train, Y_train)
model_Gaussian_NB.fit(X_train, Y_train)
knn_model.fit(X_train, Y_train)
logistic_pred = model_logistic_Regresson.predict(X_test)
gaussion_pred = model_Gaussian_NB.predict(X_test)
knn_pred = model_Gaussian_NB.predict(X_test)


logistic_metrics = {
    "Accuracy": accuracy_score(Y_test,logistic_pred),
    "Precision": precision_score(Y_test,logistic_pred),
    "Recall": recall_score(Y_test,logistic_pred),
    "F1 Score": f1_score(Y_test,logistic_pred)
}
gaussin_metrics = {
    "Accuracy": accuracy_score(Y_test,gaussion_pred),
    "Precision": precision_score(Y_test,gaussion_pred),
    "Recall": recall_score(Y_test,gaussion_pred),
    "F1 Score": f1_score(Y_test,gaussion_pred)
}
knn_metrics = {
    "Accuracy": accuracy_score(Y_test,knn_pred),
    "Precision": precision_score(Y_test,knn_pred),
    "Recall": recall_score(Y_test,knn_pred),
    "F1 Score": f1_score(Y_test,knn_pred)
}

print(logistic_metrics)
print(gaussin_metrics)
print(knn_metrics)

comparison = pd.DataFrame({
    "logistic":logistic_metrics,
    "gaussina": gaussin_metrics,
    "knn": knn_metrics
})

print(comparison)