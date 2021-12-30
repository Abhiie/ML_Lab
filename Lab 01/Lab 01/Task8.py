import numpy as np
print("Column:")
a_2d = np.arange(6).reshape(2, 3)
print(a_2d)

print("Converted into row:")
a_2d_T = a_2d.T
print(a_2d_T)
