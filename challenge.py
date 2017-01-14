#!/usr/bin/python

# Challenge dataset for regression 
# Used OLS and SGD with KFold cross_validation, approx 85% accuracy

import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
import csv 
import numpy as np 

with open('challenge_dataset.txt', 'r') as inputs:
	lines = (line.strip().split(',') for line in inputs)
	with open('challenge.csv', 'w') as outputs: 
		writer = csv.writer(outputs)
		writer.writerow(('ind', 'dep'))
		writer.writerows(lines)
	
data = pd.read_csv('challenge.csv')

x = np.array(data[['ind']])
y = np.array(data[['dep']])

kf = KFold(n_splits = 5, shuffle = True)

for train_index, test_index in kf.split(x):
	x_train, x_test = x[train_index], x[test_index]
	y_train, y_test = y[train_index], y[test_index]

reg = LinearRegression(normalize = True)
reg2 = SGDRegressor(loss = 'squared_loss', n_iter = 50)
reg.fit(x_train, y_train)
reg2.fit(x_train, y_train)
pred = reg.predict(x_test)
pred2 = reg2.predict(x_test)
print r2_score(pred, y_test)
print r2_score(pred2, y_test)


plt.plot(x_test, y_test, 'o')
plt.plot(x_test, pred)
plt.show()