# a) Fill the missing values with ‘0’
# b) Fill the missing values with mean value
# c) Fill the missing values with median value
# d) Fill the missing values with previous value
# e) Fill the missing values with next value
# f) Fill the missing values with linear interpolation
ac = df['age'].head(20)
print('Dataset:\n',ac)
ac.fillna('0')
ac.fillna(ac.mean())
ac.fillna(ac.median())
ac.fillna(method='pad')
ac.fillna(method='bfill')
ac.interpolate(method='linear',limit_direction = 'forward')
