##########################################################################
# In Python, we usually represent matrices as lists of lists. The $2 \times 2$
# Hilbert matrix (see https://en.wikipedia.org/wiki/Hilbert_matrix) can
# therefore be represented as
#
#     [[1, 1/2], [1/2, 1/3]].
# 
# Assume that all matrices contain at least one element and that all
# sublists are of equal length. However, you may not assume that all
# of them are square matrices.
#
# A matrix can be built using nested list comprehensions:
#
#     sample_matrix = [[i**2 + 3*j for i in range(8)] for j in range(8)]
##########################################################################



##########################################################################
# Write a function identity(n) that returns the $n \times n$ identity
# matrix.
#
# Example:
# 
#     >>> identity(3)
#     [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
##########################################################################



##########################################################################
# Write a function transpose(mat) that creates and returns a new matrix
# that is the transpose of a given matrix mat.
#
# Example:
# 
#     >>> transpose([[1, 2], [3, 4]])
#     [[1, 3], [2, 4]]
##########################################################################



##########################################################################
# Write a function multiply_vec(mat, v) that takes a matrix mat and
# a vector v and returns a vector that is obtained by multiplying mat
# and v. The vector v is represented as a list of numbers.
#
# Example:
# 
#     >>> multiply_vec([[1, 1/2], [1/2, 1/3]], [1, 1])
#     [1.5, 0.8333333333333333]
##########################################################################



##########################################################################
# Write a function addition(mat1, mat2) that creates and returns a
# matrix that is the sum of matrices mat1 and mat2.
#
# Example:
# 
#     >>> addition([[1, 0], [0, 1]], [[0, 2], [0, 0]])
#     [[1, 2], [0, 1]]
##########################################################################



##########################################################################
# Write a function multiply_mat(mat1, mat2) that creates and returns
# a new matrix that is obtained by matrix multiplication of mat1 and
# mat2.
#
# Example:
# 
#     >>> multiply_mat([[1, 2], [3, 4]], [[0, 1], [0, 0]])
#     [[0, 1], [0, 3]]
##########################################################################


