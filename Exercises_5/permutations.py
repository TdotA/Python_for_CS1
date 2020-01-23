##########################################################################
# Permutations 
#
# A dictionary may represent a permutation of integers from $1$ to $n$.
# For instance, a permutation that maps $1$ to $3$, $3$ to $1$ and fixes
# number $2$ can be represented by the dictionary `{1: 3, 2: 2, 3: 1}`.
##########################################################################



##########################################################################
# Write a function image(permutation, x) that takes a dictionary
# `permutation` which represents a permutation and a number `x`. The function
# should return the image of `x` under `permutation`. Example:
# 
#     >>> image({1: 3, 2: 4, 3: 2, 4: 1}, 4)
#     1
##########################################################################



##########################################################################
# Write a function images(permutation, x, n) that returns a sequence
# of images that are obtained from `x` by using `permutation` on it
# `n` times. Example:
# 
#     >>> images({1: 3, 2: 4, 3: 2, 4: 1}, 1, 2)
#     [1, 3, 2]
##########################################################################



##########################################################################
# Write a function cycle(permutation, x) that finds and returns the
# cycle that starts with the number `x`. Example:
# 
#     >>> cycle({1: 3, 2: 2, 3: 1}, 1)
#     [1, 3]
#     >>> cycle({1: 3, 2: 2, 3: 1}, 2)
#     [2]
##########################################################################



##########################################################################
# Write a function cycles(permutation) that returns the list of disjoint
# cycles of a given permutation. Each cycle should start with its smallest
# element. Cycles should be ordered lexicographically. Example:
# 
#     >>> cycles({1: 3, 2: 2, 3: 1})
#     [[1, 3], [2]]
##########################################################################



##########################################################################
# Write a function is_permutation(dictionary) that returns `True` if
# the given dictionary represents a permutation and `False` otherwise.
# Example:
# 
#     >>> is_permutation({1: 3, 2: 5, 5: 1})
#     False
##########################################################################


