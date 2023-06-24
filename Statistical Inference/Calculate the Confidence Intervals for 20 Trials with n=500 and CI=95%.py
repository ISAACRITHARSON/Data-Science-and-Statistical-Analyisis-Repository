employee = pd.DataFrame([['E001',34,123,350,12],
['E002',40,114,450,16],
['E003',37,135,169,14],
['E004',89,139,189,8],
['E005',44,117,183,20]],
columns=['Employee
id','Age','Sales','Income','Experience'])
cl = 0.95
n = 500
for i in range(1,21):
sample = np.random.choice(a = df['Age'], size = n)
mean = sample.mean()
error = st.sem(sample)
dof = sample.size - 1
ci_20 = st.t.interval(cl,dof,mean,error)
print(f'Confidence Interval for {i} trial:{ci_20}\n')
