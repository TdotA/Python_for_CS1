def identity(n):
    matrix = []
    for i in range (n):
        line = []
        matrix.append(line)
        for j in range (n):
            if j == i:
                line.append(1)
            else:
                line.append(0)
    print(matrix)
#identity(3)

def matrix_fcn(n,m): #utility function; returns a n*m zero matrix
    matrix=[]
    for i in range (n):
        line = []
        matrix.append(line)
        for j in range (m):
            line.append(0)
    return matrix
#matrix_fcn(3,3)

def transpose(mat):
    trans = matrix_fcn(len(mat[0]), len(mat))
    for i in range (len(mat)):  
       for j in range (len(mat[i])):
            trans[j][i] = mat[i][j]
    print(trans)
#transpose([[1, 2], [3, 4], [5,6]])

def multiply_vec(mat, v):
    result = []
    for i in mat:
        s = 0
        for j in range(len(i)):
           s += i[j]*v[j]
        result.append(s)
    return result
#print(multiply_vec([[1, 1/2], [1/2, 1/3]], [1, 1]))

def addition(mat1, mat2):
    result = matrix_fcn((max(len(mat1), len(mat2))), (max(len(mat1[0]), len(mat2[0]))))
    for i in range(max(len(mat1), len(mat2))):
        for j in range(min(len(mat1[i]), len(mat2[i]))):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result
#print(addition([[1, 0, 0], [0, 1, 0]], [[0, 2], [0, 3]]))

def multiply_mat(mat1, mat2): 
    result = matrix_fcn((max(len(mat1), len(mat2))), (max(len(mat1[0]), len(mat2[0]))))
    for i in range (max(len(mat1), len(mat2))):
        print(i)
        for j in range(min(len(mat1[i]), len(mat2[i]))):
            
    return result
print(multiply_mat([[1, 2], [3, 4]], [[0, 1], [0, 0]]))
#    [[0, 1], [0, 3]]
        