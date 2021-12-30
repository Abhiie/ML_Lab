import numpy as np


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print("Before Random.randint\n",arr)
arr = np.random.randint(10,90,(4,5)) # random numpy array of shape (4,5)
print("After Random.randint \n", arr)