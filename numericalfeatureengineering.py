# -*- coding: utf-8 -*-
"""NumericalFeatureEngineering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bngw6kGB2nE8r8ijGho6d8rpnkj4wRmf
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.stats as spstats

df=pd.read_csv('Pokemon.csv',encoding='utf-8')
df.head()

dfa=df[['HP','Attack','Defense',]].head()

#MINMAXSCALER
from sklearn.preprocessing import MinMaxScaler
mmS=MinMaxScaler(feature_range=(0,1))
rescale=mmS.fit_transform(dfa)
rescale

#Normalisation
from sklearn.preprocessing import Normalizer
norm=Normalizer()
norm.fit_transform(dfa)

