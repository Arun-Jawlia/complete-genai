
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
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

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
    print(f"model with k: {k} and accuracte :{accuracy}")

print(result)

best_k_value = max(result,key= result.get)
best_knn_accuracy = result[best_k_value]
print("Best K:",best_k_value)
print("Best KNN Accuracy:",best_knn_accuracy)