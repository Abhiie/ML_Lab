import numpy as np
import pandas as pd
import seaborn as sns
data = pd.read_csv('Exercise-CarData.csv')
print(data.head)
data = data.iloc[:,:-1]
data.head()
corr = data.corr()
corr.head()
print(corr)
print(sns.heatmap(corr))
