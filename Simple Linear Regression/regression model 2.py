import numpy as np
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
height = np.array([43,21,25,42,57,59]).reshape(-1,1)
weight = np.array([99,65,79,75,87,81])
lr.fit(height,weight)
print('Intercept: ',lr.intercept_)
print('Co-efficient: ',lr.coef_)
from sklearn.metrics import r2_score
print('R2 Score: ',r2_score(height,weight) )
from sklearn.metrics import mean_absolute_error as mas
print('Mean Absolute Error : ',mas(height,weight))
from sklearn.metrics import mean_squared_error as mse
print('Mean Squared Value: ',mse(height,weight))
