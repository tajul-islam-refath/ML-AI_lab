# -*- coding: utf-8 -*-
"""Linear_Regression_Class_Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e-3yDE464mntYTKb8EC9WV512SItGnQA
"""

import numpy as np
import pandas as pd

df=pd.read_csv('USA_Housing.csv')

df.head()

df.info()

df=df.drop('Address',axis=1)

df.head()

df.isnull().sum()

X=df.drop('Price', axis=1)
y=df['Price']

X.head()

y.head()

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101) #42

from sklearn.linear_model import LinearRegression

ln=LinearRegression()

ln.fit(X_train,y_train)

print(ln.score(X_train,y_train))

print(ln.intercept_) #C -2628711.599679018

coeff_df=pd.DataFrame(ln.coef_,X.columns,columns=['Coefficient'])
coeff_df

pred=ln.predict(X_test)

import matplotlib.pyplot as plt

plt.scatter(y_test,pred)

test=ln.score(X_test,y_test)
print(test)

from sklearn.metrics import r2_score

r2=r2_score(y_test,pred)
print(r2)

ln.fit(X_test,y_test)

print(ln.score(X_test,y_test))

print(ln.intercept_)

coeff_df=pd.DataFrame(ln.coef_,X.columns,columns=['Coefficient'])
coeff_df

