# Importing Libraries
import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import math
# Dataset for qn 1 to 6
df =
pd.read_csv('https://raw.githubusercontent.com/gchoi/Dataset/master/ToyotaCorolla.csv')
np.random.seed(0)
n1 = 400
sample1 = np.random.choice(a = df['Age'], size = n1)
s1_mean = sample1.mean()
n2 = 500
sample2 = np.random.choice(a = df['Age'], size = n2)
s2_mean = sample2.mean()
pop_mean = df['Age'].mean()
print('Population mean: ',pop_mean)
print('Sample mean 1: ',s1_mean)
print('Sample mean 2: ',s2_mean)
