# -*- coding: utf-8 -*-
"""KNNC_play.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ayeV2a4fYdb2kRLCsfZJlYg7sU-RB-I8
"""

# first feature 
weather = ["Sunny" , "Sunny" , "Overcast" , "Rainy" , "Rainy" , "Rainy" , "Overcast" , "Sunny" , "Sunny" , "Rainy" , 
           "Sunny" , "Overcast" ,"Overcast" , "Rainy"]

# second feature
temp = ["Hot" , "Hot", "Hot" , "Mild" , "Cool" , "Cool" , "Cool" , "Mild" , "Cool", "Mild" , "Mild" , "Mild" , "Hot" , "Mild" ]

#label
play = ["No" , "No" , "Yes" , "Yes" , "Yes" , "No", "Yes" ,"No" ,"Yes" , "Yes" , "Yes" , "Yes" , "Yes" , "No"]

#import label encoder
from sklearn import preprocessing

#create an object
le = preprocessing.LabelEncoder()

#convert string to number
weather_en = le.fit_transform(weather)
weather_en

temp_en = le.fit_transform(temp)
label_en = le.fit_transform(play)

# zip weather and temp
featurs = list(zip(weather_en, temp_en))
featurs

#import knn algo
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)

model.fit(featurs , label_en)

predict = model.predict([[0 , 2]])
predict