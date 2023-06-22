print('Count : ',df.isnull().sum().sum())
null = df['CC'].fillna(0)
null.head(13)
