# -*- coding: utf-8 -*-
"""SVMC_HEART_topfeatures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D-AhK3mTjL03Ne9tor2Y0ZYucHJcwowE
"""

from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

files.upload()

df = pd.read_csv("heart.csv")

df.head()

df.shape

df.isnull().sum()

x = df.drop(["target"] , axis=1)
x

y = df["target"]
y

# fetature selection
from sklearn.feature_selection import SelectKBest , f_classif

FIT_FEATURES = SelectKBest(score_func=f_classif)

FIT_FEATURES.fit(x , y)

score_col = pd.DataFrame(FIT_FEATURES.scores_, columns=["score value"])
score_col

col_name = pd.DataFrame(x.columns, columns=["Name"])
col_name

top_features = pd.concat([col_name,score_col] , axis=1)
top_features

top_features.nlargest(8,"score value")

top_x_features = x.drop(["age","trestbps","chol","fbs","restecg"], axis=1)
top_x_features

# for separate train and test data
from sklearn.model_selection import train_test_split
# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score, confusion_matrix
# svm model
from sklearn.svm import SVC

xTrain , xTest , yTrain , yTest = train_test_split(top_x_features , y , test_size=.2, random_state=1)

#linear model
model = SVC(C= .1, kernel='linear', gamma= 1)

model.fit(xTrain , yTrain)

predict = model.predict(xTest)

print(f"Train score : {model.score(xTrain , yTrain)}")
print(f"Test score : {model.score(xTest , yTest)}")

print("Confusion Matrix:\n",confusion_matrix(predict,yTest))

# rbf kernel
rbf_model = SVC( kernel='rbf')
rbf_model.fit(xTrain , yTrain)

rbf_predict = rbf_model.predict(xTest)

print(rbf_model.score(xTrain , yTrain))
print(rbf_model.score(xTest , yTest))

print("Confusion Matrix:\n",confusion_matrix(rbf_predict,yTest))

# poly kernel
poly_model = SVC(kernel='poly')
poly_model.fit(xTrain , yTrain)

print(poly_model.score(xTrain , yTrain))
print(poly_model.score(xTest , yTest))