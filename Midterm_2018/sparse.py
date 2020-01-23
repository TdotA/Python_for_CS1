##########################################################################
# Sparse matrix
##########################################################################

m_1 = [
    [0, 0, 0,  0],
    [0, 1, 0, -1],
    [0, 2, 0,  0]    
]

m_2 = [
    [0,  3, 0, 0],
    [5,  0, 0, 1],
    [0, -2, 0, 0]    
]

##########################################################################
# The sparse representation of a matrix m is a tuple (n, m, v) where
# n and m are dimensions of the matrix and v is a dictionary that contains
# all items (i, j): a, where i and j are the coordinates and a is the
# element in position (i, j) in the matrix. The dictionary v contains only
# those elements that are non-zero.
#
# For example, for the above matrix m_1 the sparse representation is:
#
#     (3, 4, {(1, 3): -1, (1, 1): 1, (2, 1): 2})
#
# Write a function to_sparse(mat) that takes a matrix mat of integers as
# the argument and returns its sparse representation.
#
# Example:
#
#     >>> to_sparse(m_1)
#     (3, 4, {(1, 3): -1, (1, 1): 1, (2, 1): 2})
##########################################################################



##########################################################################
# Write a function sparse_sum(mat1, mat2) that takes 2 sparse matrices
# (they will be of the same dimensions) and returns their sum (in the form
# of a sparse matrix).
#
# Example:
#
#     >>> sparse_sum(to_sparse(m_1), to_sparse(m_2))
#     (3, 4, {(0, 1): 3, (1, 0): 5, (1, 1): 1})
##########################################################################



##########################################################################
# Write a function row_sums(mat) that takes a sparse matrix as the only
# argument and returns the list that contains row-sums, i.e., the list
#
#     [s_0, s_1, ..., s_{m-1}]
#
# where s_i equals the sum of all elements in row i.
#
# Example:
#
#     >>> row_sums(to_sparse(m_1))
#     [0, 3, 0, -1]
##########################################################################



##########################################################################
# Write a function transpose(mat) that takes a sparse matrix as the only
# argument and returns the transpose of the matrix mat (also in the sparse
# representation).
#
# The transpose of matrix m_1 is:
#
#     [[0,  0, 0],
#      [0,  1, 2],
#      [0,  0, 0],
#      [0, -1, 0]]
#
# Example:
#
#     >>> transpose(to_sparse(m_1))
#     (4, 3, {(1, 2): 2, (3, 1): -1, (1, 1): 1})
##########################################################################



