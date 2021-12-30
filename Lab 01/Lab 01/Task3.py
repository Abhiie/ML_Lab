import numpy as np
arr = np.random.randint(10,90,(4,5))
print('Original matrix 4 x 5')
print(arr)
print('Transposed matrix 5 x 4')
print(arr.T)
#Determinant
n_array = np.array([[2, 3], [4, 5]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print("\nDeterminant of given 2X2 matrix:")
print(int(det))