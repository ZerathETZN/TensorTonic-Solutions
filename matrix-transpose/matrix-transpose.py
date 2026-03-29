import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    M,N = A.shape
    result = np.zeros((N,M), dtype = A.dtype)
    for i in range(M):
        for j in range(N):
            result[j,i] = A[i,j]
        
    return result
    pass

A = [[1, 2, 3], [4, 5, 6]]
matrix_transpose(A)
A = [[1, 2], [3, 4]]
matrix_transpose(A)
A = [[1, 2, 3, 4]]
matrix_transpose(A)
