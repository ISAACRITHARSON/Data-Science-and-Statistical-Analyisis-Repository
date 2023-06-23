t = pd.read_excel('/content/Employee Table.xlsx')
drop = t.drop(['BMI','Sales'],axis=1)
drop
