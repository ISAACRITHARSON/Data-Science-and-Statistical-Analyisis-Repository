actual = np.array([10,-5,3,9,11,-4.7])
predicted = np.array([9,-4.2,3,8.6,10.5,-4.25])
# MAE
from sklearn.metrics import mean_absolute_error
print('Mean Absolute Error: ',mean_absolute_error(actual,predicted))
#MSE
from sklearn.metrics import mean_squared_error
print('Mean squared error: ',mean_squared_error(actual,predicted))
#R2 Score
from sklearn.metrics import r2_score
print('R2 Score: ',r2_score(actual,predicted))
