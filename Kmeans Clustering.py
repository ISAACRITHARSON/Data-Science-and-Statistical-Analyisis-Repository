import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Mall_Customers.csv - Mall_Customers.csv.csv')
x = df[['Annual Income (k$)','Spending Score (1-100)']].values
wcss_list = []
for i in range(1,11):
kmeans = KMeans(n_clusters=i,init='k-means++',random_state=12)
kmeans.fit(x)
wcss_list.append(kmeans.inertia_)
plt.plot(range(1,11),wcss_list)
plt.title('The Elbow method')
plt.xlabel('No.of.clusters')
plt.ylabel('wcss list')
plt.show()
kmeans = KMeans(n_clusters=7)
y_predict = kmeans.fit_predict(x)
plt.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')
plt.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s = 100, c = 'green', label = 'Cluster 2')
plt.scatter(x[y_predict== 2, 0], x[y_predict == 2, 1], s = 100, c = 'red', label = 'Cluster 3')
plt.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(x[y_predict == 4, 0], x[y_predict == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label =
'Centroid')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
centers = kmeans.cluster_centers_
print('Cluster centroids: \n',centers)
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
# Calculate Silhoutte Score
s_score = silhouette_score(x, kmeans.labels_, metric='euclidean')
# Calculate Davies-Bouldin Index
d_score = davies_bouldin_score(x, kmeans.labels_)
# Print the score
print('Silhouetter Score: %.3f' % s_score)
print('Davies-Bouldin Index: %.3f' % d_score)
