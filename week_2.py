# -*- coding: utf-8 -*-
"""Week_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gj0grtku0FSZF-wBBaPfJfwTBG76nGzA
"""

#Data exploration and pre-processing in Python.
import pandas as pd
data=pd.read_csv("/content/drive/MyDrive/Titanic.csv")

data

data1=pd.read_excel("/content/drive/MyDrive/WORKSHOP.xlsx")

data1

data

res=data.pivot(index="PassengerId" , columns="Survived" , values="Pclass")

res

