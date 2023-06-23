sorted = df.sort_values('Age')
sorted.plot(x='Age',y='Price',kind='line',marker='o',linewidth=2.5,color='vio
let')
plt.show()
