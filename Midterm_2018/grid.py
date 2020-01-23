##########################################################################
# The Grid
##########################################################################



##########################################################################
# A grid is a n x m matrix, where each cell is either a '.' (free space) or
# a '#' (a wall). An example (7 x 10 grid):
#
#     ##########
#     #...#....#
#     #...#....#
#     #........#
#     #...#....#
#     #...#....#
#     ##########
#
# In Python it can be represented as a list of strings (each string is one
# row of the grid):
#
# ['##########', '#...#....#', '#...#....#', '#........#', '#...#....#',
#  '#...#....#', '##########']
#
# Write a function load_grid(file_name) that will get a name of a file
# containing the description of a grid. The function should return the
# list of strings.
#
# The first row of the file contains three integers: n, m and k.
# Integers n and m are dimensions of the grid. The boundary of the grid
# will always contain '#'. The number k is the number of additional
# walls ('#' fields). The next k lines of the file contain integers r_i and
# c_i where (r_i, c_i) is the position of a '#' in the grid.
#
# Example (file grid.txt is enclosed):
#
#     >>> load_grid('grid.txt')
#     ['##########', '#...#....#', '#...#....#', '#........#', '#...#....#',
#      '#...#....#', '##########']
##########################################################################



##########################################################################
# There is an ant standing on one free spot in the grid. Ant's position
# can be given as a tuple of two numbers (r, c), where
#
#  * r is the row number (0 <= r < n), and
#  * c is the column number (0 <= c < m).
# 
# Write a function final_ant(grid, p, s), where:
#
#  * grid is a grid as described above (list of strings),
#  * p is a pair of two numbers (i.e. the position of the ant), and
#  * s is a string that contains characters 'L', 'U', 'R' and 'D'.
#
# The function should return the final position of the ant. The string
# s describes the movement of the ant (a sequence of steps). Charaters
# have the following meaning:
#
#  * 'U' .. up
#  * 'D' .. down
#  * 'L' .. left
#  * 'R' .. right
#
# The ant will make a step in the given direction, unless there is a
# wall ('#' field). In that case the ant will remain at its current
# position.
#
# If the initial position of the ant is invalid (the ant is not on the
# grid or it is standing in a wall) the function should return None.
# 
# Example:
#
#     >>> g = load_grid('grid.txt')
#     >>> final_ant(g, (1, 2), 'RRRDRDRRRRRDLLDLLLL')
#     (5, 5)
#     >>> print(final_ant(g, (4, 4), 'RRDLLUUR'))
#     None
##########################################################################


    
##########################################################################
# Write a function initial_ant(grid, f, s) where:
#
#  * grid is a grid as described above (list of strings),
#  * f is a pair of two numbers (i.e. the final position of the ant), and
#  * s is a string that contains characters 'L', 'U', 'R' and 'D'.
#
# The function should return a list [p_0, p_1, p_2, ..., p_k] that contains
# all possible valid initial positions of the ant such that after the
# sequence of moves s the ant will be in position f.
#
# If the final position f is invalid the function should return None.
# The list of positions should be sorted (see the example below).
#
# Example:
#
#     >>> g = load_grid('grid.txt')
#     >>> initial_ant(g, (5, 5), 'RRRDRDRRRRRDLLDLLLL')
#     [(1, 1), (1, 2), (1, 3), (1, 5), (1, 6), (1, 7), (1, 8),
#      (2, 1), (2, 2), (2, 3), (2, 5), (2, 6), (2, 7), (2, 8),
#      (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
#      (4, 5), (4, 6), (4, 7), (4, 8), (5, 5), (5, 6), (5, 7), (5, 8)]
#     >>> print(initial_ant(g, (4, 4), 'RRDLLUUR'))
#     None
##########################################################################



##########################################################################
# Write a function reduce_walk(grid, p, s)) where arguments have the
# same meaning as in the function final_ant. The function should return
# the reduction of the string s, i.e. a string will all redundant steps
# removed. Redundant steps are those that can not be made becase a wall
# is in way.
#
# If the initial position of the ant is invalid (the ant is not on the
# grid or it is standing in a wall) the function should return None.
# 
# Example:
#
#     >>> g = load_grid('grid.txt')
#     >>> reduce_walk(g, (1, 2), 'RRRDRDRRRRRDLLDLLLL')
#     'RDDRRRRRDLLDL'
#     >>> print(reduce_walk(g, (4, 4), 'RRDLLUUR'))
#     None
##########################################################################



