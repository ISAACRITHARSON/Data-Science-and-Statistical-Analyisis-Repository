import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Movies.csv - Movies.csv.csv')
movies=df.iloc[:, 1:2]
movies['title']= movies['title'].str.strip()
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
tfidf_matrix = tf.fit_transform(movies['title'])
print(tfidf_matrix.shape)
from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim.shape)
# Build a 1-dimensional array with movie titles
titles = movies['title']
indices = pd.Series(movies.index, index=movies['title'])
title=input("Enter the movie related to recommend:")
num=int(input("No. of recommendations:"))
idx = indices[title]
sim_scores = list(enumerate(cosine_sim[idx]))
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
sim_scores = sim_scores[1:num+1]
movie_indices = [i[0] for i in sim_scores]
scores=[i[1] for i in sim_scores]
print("Recommending movies similar to " + title + "...")
print("-------")
for rec in range(num):
print("Recommended: " + titles[movie_indices[rec]] + " (score:" + str(scores[rec]) + ")")
