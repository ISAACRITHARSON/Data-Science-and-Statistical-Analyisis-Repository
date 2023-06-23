Q1 = t['Age'].quantile(.25)
Q3 = t['Age'].quantile(.75)
IQR = Q3 - Q1
print('IQR: ',IQR)
l = Q1 - 1.5*IQR
h = Q3 + 1.5*IQR
outlier = t[(t['Age']>l)&(t['Age']<h)]
outlier
