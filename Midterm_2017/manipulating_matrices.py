##########################################################################
# Manipulating matrices 
#
# Matrices are usually represented as lists of lists. You may assume that
# throughout this task all matrices will be valid (i.e., all sublists
# will be of equal length). You can find an example below.
##########################################################################

my_matrix = [
    [ 5,  4,  6, -3],
    [ 4,  7, 10,  9],
    [12,  6, 11,  5],
    [ 2, -2,  1,  3],
    [ 1,  7, -1,  5],    
]

##########################################################################
# Write a function extract_column(m, i) that takes two arguments: a matrix
# m and an index i. The function shuld return a list that represents i-th
# column of the matrix m. (Indices are 0-based.) Example:
# 
#     >>> extract_column(my_matrix, 2)
#     [6, 10, 11, 1, -1]
##########################################################################



##########################################################################
# Write a function modify_column(m, i, l) that takes three arguments:
# a matrix m, an index i and a list l. The function should replace values
# in the i-th column of the matrix by values from the list l. If the list
# is shorter than the height of the matrix, then the remaining elements
# should not be modified. If the list is longer, then the redundant elements
# should be ignored. Example:
# 
#     >>> modify_column(my_matrix, 2, [2, -5, 6])
#     >>> my_matrix
#     [[5, 4, 2, -3], [4, 7, -5, 9], [12, 6, 6, 5], [2, -2, 1, 3], [1, 7, -1, 5]]
#     >>> modify_column(my_matrix, 0, [1, 2, -3, -4, -5, -6, -7])
#     >>> my_matrix
#     [[1, 4, 2, -3], [2, 7, -5, 9], [-3, 6, 6, 5], [-4, -2, 1, 3], [-5, 7, -1, 5]]
##########################################################################



##########################################################################
# Write a function sort_columns(m) that takes a matrix and sorts the elements
# in each column of the matrix. The elements should be ordered in the increasing
# order. The function should modify the matrix m. Example:
# 
#     >>> sort_columns(my_matrix)
#     >>> my_matrix
#     [[1, -2, -1, -3], [2, 4, 1, 3], [4, 6, 6, 5], [5, 7, 10, 5], [12, 7, 11, 9]]
##########################################################################



##########################################################################
# Write a function snake(n) that takes an integer n an returns a new
# $n \times n$ matrix that "contains a snake", i.e., the first row of
# the matrix contains numbers $1, 2, \ldots, n$, the second row contains
# numbers $2n, 2n-1, \ldots, n+1$ etc. See also the example below.
# Example:
# 
#     >>> snake(5)
#     [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15],
#      [20, 19, 18, 17, 16], [21, 22, 23, 24, 25]]
##########################################################################


