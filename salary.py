
import pandas as p
import joblib as jp
import numpy


db = p.read_csv("SalaryData-Copy1.csv")

x = db[db.columns[0]]

y = db[db.columns[1]]

x = x.values
x = x.reshape(-1,1)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x,y)


jp.dump(model, "Saalry2.pk1")
