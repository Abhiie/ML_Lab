import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
df = pd.read_csv("Exercise-CarData.csv")
df.head()
df.dropna(inplace=True)
df.isnull().sum();
print(df.isnull().sum())