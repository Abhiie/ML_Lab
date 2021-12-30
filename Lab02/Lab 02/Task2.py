# Step 1: Import Libraries

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Step 2: Load Data

datasets = pd.read_csv('Exercise-CarData.csv')
print("\nData :\n", datasets)
X = datasets.iloc[:, :-1].values
Y = datasets.iloc[:, -1].values
X_new = datasets.iloc[:,1:3].values
print("\n\nX  transformation : \n", X_new)
#scaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_new)
print("\n\nScaling X : \n", X_scaled)
#standard
std = StandardScaler()
X_std = std.fit_transform(X_new)
print("\n\nStandardization X : \n", X_std)