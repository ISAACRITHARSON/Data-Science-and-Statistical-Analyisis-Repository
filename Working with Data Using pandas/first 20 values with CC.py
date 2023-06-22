c = df[df['CC']==2000].head(20)
c.insert(10,'Horse Power',c['HP']*2)
c.head()
