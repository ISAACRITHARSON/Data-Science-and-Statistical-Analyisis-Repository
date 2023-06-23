miss = df['age'].head(20).isnull().sum()
print('No.of.Missing values: ','**',miss,'**')
df['age'].head(20).dropna()
