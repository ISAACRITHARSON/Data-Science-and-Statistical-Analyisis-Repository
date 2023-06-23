# calculate Zscore
import scipy.stats as stats
zscore = stats.zscore(t['Age'])
print('Zscores:\n',zscore)
# remove the outlier
filter = t[(zscore<3) & (zscore>-3)].drop_duplicates()
filter
# Boxplot
filter[['Age']].boxplot()
plt.show()
