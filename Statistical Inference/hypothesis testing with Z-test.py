pmean = 6
smean = 5.43
sd = 2.44
n = 100
z = abs((smean-pmean)/(sd/math.sqrt(n)))
if(z > 1.96):
print('Reject H0 for 95% confidence level')
else:
print('Accept H0 for 95% confidence level')
if(z > 2.57):
print('Reject H0 for 99% confidence level')
else:
print('Accept H0 for 99% confidence level')
print('Z value :',z)
