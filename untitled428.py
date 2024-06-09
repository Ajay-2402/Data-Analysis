unzip "/content/archive (2).zip"

import pandas as pd

df = pd.read_csv("/content/adult.csv")

df.head()

df.describe()

df['age'].max()

df['age'].min()

df['age'].mean()

df['age'].median()

df['age'].mode()

df['age'].var()

df['age'].skew()

list1 = [1,2,3,5,6,6,7,5,5,10]

(6+6)//2

"""#Machine Learning"""

import pandas as pd

data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8, 120.2, 180.3, 240.1, 75.4, 198.4, 134.3, 95.2, 150.5, 45.1, 205.7, 123.4, 160.8, 112.9, 140.3, 87.6],
    'Sales': [22.1, 10.4, 9.3, 18.5, 12.9, 15.5, 22.4, 24.0, 14.3, 23.7, 19.6, 11.6, 18.8, 9.5, 25.1, 16.8, 20.2, 14.7, 18.1, 10.9]
}

df = pd.DataFrame(data)
df

df.head()

df.tail()

df.info()

df.shape

df.describe()

df.plot(x="TV",y="Sales",kind="scatter")

import pandas as pd

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029],
    'Price_of_Petrol': [45, 49, 53, 55, 60, 70, 75, 80, 83, 85, 88, 90, 92, 95, 96,97,98,99,105,107]
}

df = pd.DataFrame(data)
print(df)

df.head()

df.plot(x="Price_of_Petrol",y="Year",kind="scatter")

df.head(3)

import numpy as np

# [[[[1]]]]

X = df[['Year']]
y = df[['Price_of_Petrol']]

X

y

pip install scikit-learn

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X,y)

reg.predict([[2035]])

X = df[['Price_of_Petrol']]
y = df[['Year']]

reg = LinearRegression()

reg.fit(y,X)

int(reg.predict([[2050]]))

1+1

print("hello")

name = "krishna"

if name == "krishna":
  print(True)
else:
  print(False)

