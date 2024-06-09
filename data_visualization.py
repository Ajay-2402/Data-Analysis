# -*- coding: utf-8 -*-
"""Data Visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/Ajay-2402/5a0ca99f6d89e0d618078258fb7551a6/untitled427.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

!unzip "/content/archive (2).zip"

df = pd.read_csv("/content/adult.csv")

df.head(3)

print("Number of rows in dataframe-->",df.shape[0])
print("Number of columns in dataframe-->",df.shape[1])

df.drop_duplicates(inplace=True)

df.head()

df.isna().sum()

df.isna().sum().sum()

df.describe()

df['age'].min()

df['age'].max()

df.info()

df.head()

df_object = df.select_dtypes("object")

df_object

df.select_dtypes(exclude = "object")

import seaborn as sns

sns.countplot(df_object['workclass'])

sns.countplot(df_object, x="workclass")

plt.figure(figsize=(10,5))
sns.countplot(df_object, x="workclass")
plt.xticks(rotation=90)

df_object.columns

len(df_object.columns)

plt.figure(figsize=(18,30))
for i in range(len(df_object.columns)):
  plt.subplot(5,2,i+1)
  sns.countplot(df_object[df_object.columns[i]])
  plt.title(f"CountPlot of {df_object.columns[i]}")
  plt.xticks(rotation=90)
  plt.tight_layout()

df_int = df.select_dtypes(exclude = "object")

df_int

sns.distplot(df_int['age'])

df_int.columns

plt.figure(figsize=(18,30))
for i in range(len(df_int.columns)):
  plt.subplot(5,2,i+1)
  sns.distplot(df_int[df_int.columns[i]])
  plt.title(f"distplot of {df_int.columns[i]}")
  plt.xticks(rotation=90)
  plt.tight_layout()

df

sns.stripplot(x=df['income'],y=df['age'])

sns.stripplot(x=df['income'],y=df['education'])

