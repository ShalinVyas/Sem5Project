# -*- coding: utf-8 -*-
"""logs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bjcsYGx1Kjagx4pIWPFlp8zaGRrkcvos

# Import Library
"""

import pandas as pd
import numpy as np
import missingno as msno

"""# Load File"""

from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv("log2.csv")

df

df["Level"]

msno.matrix(df)

df=df.fillna(0)

df=df.replace("nan","0")

datatype=df.dtypes

datatype

df=df.drop(["Processor ID","Processor Time","Task Category"],axis=1)

df["Source"].unique()

import matplotlib.pyplot as plt
import seaborn as sns

def resizeplot(l,a,d):
    plt.figure(figsize=(l,a),dpi=d)

resizeplot(10,6,100)
plt.bar(df['Source'],df['Source'].count())
plt. show()

sns.histplot(df['Source'],kde=True)

x=df["Date and Time"]

x

y=df["Source"]

plt.pie(y)
plt.title("Apps Used")

df.groupby(["Date and Time"]).sum().plot(kind='pie',y='Source',autopct='%1.0f%%')

resizeplot(10,6,100)
df[['Source']].plot()

