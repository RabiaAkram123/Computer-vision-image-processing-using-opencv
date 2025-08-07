# ######### 2d matrix manipulation#########
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("2nd row:", A[1])        # Index 1 = second row
print("2nd column:", A[:, 1])  # Index 1 = second column
print('specific value',A[1,0])
A[1][2]=8
print(A)
##############3D MATRIX##################
import numpy as np

A = np.array([
    [[1, 2], 
     [3, 4]],   # Matrix 1
    [[5, 6],
     [7, 8]]    # Matrix 2
])

print("Dimensio",A.ndim)
print("Shape of A:", A.shape) 
print("Size of A:", A.size)
print("Data type of A:", A.dtype)
print(A[0,1]) # accessing 2nd row of 1st matrix
print(A[0][:,1]) # accessing 2nd column of 1st matrix[0][1][1]=10  # modify
print(A)
print('specifiv value;',A[1,1,1])
############4d MATRIX##################
B = np.array([
    [[[1, 2],
      [3, 4]],   # Matrix 1
     [[5, 6], 
      [7, 8]]],  # Matrix 2
    [[[9, 10],
      [11, 12]], # Matrix 3
     [[13, 14],
      [15, 16]]] # Matrix 4
])
print("Dimensio",B.ndim)
print("Shape of B:", B.shape)
print("Size of B:", B.size)
print("Data type of B:", B.dtype)
print(B[0,0,1])  # accessing 2nd row of 1st matrix
print(B[0][0][:,1])  # accessing 2nd column of 1st
print(B[1,1,1,1])
B[0][1][1][1]=20  # modify
print(B)