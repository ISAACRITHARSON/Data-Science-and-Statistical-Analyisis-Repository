import pandas as pd
sn=pd.read_csv('https://raw.githubusercontent.com/shivang98/Social-Network-ad
s-Boost/master/Social_Network_Ads.csv')
X = sn.drop(['Gender','EstimatedSalary'],axis = 1)
y = sn['EstimatedSalary']
from sklearn.model_selection import train_test_split as tts
X_train , X_test , y_train , y_test = tts(X ,y , test_size = 0.2,
random_state = 0)
from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
model1.fit(X_train,y_train)
y_pred = model1.predict(X_test)
print('Intercept: ',model1.intercept_)
print('Co-efficient: ',model1.coef_)
from sklearn.metrics import r2_score
print('R2 Score: ',r2_score(y_test,y_pred) )
from sklearn.metrics import mean_absolute_error as mas
print('Mean Absolute Error : ',mas(y_test,y_pred))
from sklearn.metrics import mean_squared_error as mse
print('Mean Squared Value: ',mse(y_test,y_pred))
