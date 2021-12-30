import numpy as np
a = np.array([[1,2],[4,3]])
print("Shape ",a.shape)#This array attribute returns a tuple consisting of array dimensions
a1 = np.array([[1,2,3,4],[4,5,6,4]])
b1 = a1.reshape(4,2)
print("Reshape",b1)

x = np.array([10,20,30,40,50])
print(x.flags)
