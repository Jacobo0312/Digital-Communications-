import numpy as np

matrixA=np.array([[1,1,1,0,0], [1,0,0,1,0],[0,1,0,0,1]]);
matrixB=np.array([[0],[1],[1],[1],[1]]);

print("MatrixA:")
print(matrixA);
print("MatrixB:")
print(matrixB);


def binaryOperationProduct(a,b):
    if a==1 and b==1:
        return 1
    elif a==1 and b==0:
        return 0
    elif a==0 and b==1:
        return 0
    else:
        return 0


def binaryOperationSum(a,b):
    if a==1 and b==1:
        return 0
    elif a==1 and b==0:
        return 1
    elif a==0 and b==1:
        return 1
    else:
        return 0



def multiply_matrix(A,B):
    C=np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                x=binaryOperationProduct(A[i][k],B[k][j])
                C[i][j]=binaryOperationSum(C[i][j],x)   
    return C



print("Multiply:")
print(multiply_matrix(matrixA,matrixB));
