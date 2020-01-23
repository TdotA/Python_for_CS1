##########################################################################
# Conway's Game of Life
#
# This game was devised by the British mathematician John H. Conway.
# We are given a matrix whose elements are logical values True and
# False. The value True means that the cell is alive, while the value False
# means that the cell is dead. Every non-boundary cell has 8 neighbours:
# two horizontal, two vertical and four diagonal neighbours. The time runs
# in discrete steps. The current state of the world uniquely defines the
# next state of the world by the following rules:
# 
# - Any alive cell that has less than 2 alive neighbours dies (underpopulation).
# - Any alive cell that has 2 or 3 alive neighbours lives on.
# - Any alive cell that has more than 3 alive neighbours dies (overpopulation).
# - Any dead cell with exactly 3 alive neighbours becomes alive (reproduction).
# 
# Examples of matrices that represent a state of the world:
# 
#     world_1 = [
#         [False, False, False, False, False, False],
#         [False, False, False, True, False, False],
#         [False, True, False, False, True, False],
#         [False, True, False, False, True, False],
#         [False, False, True, False, False, False],
#         [False, False, False, False, False, False]
#     ]
# 
#     world_2 = [
#         [False, False, False, False],
#         [False, True, True, False],
#         [False, True, True, False],
#         [False, False, False, False]
#     ]
##########################################################################



##########################################################################
# Write a function alive(world, i, j) that returns the number of alive
# neighbours of cell in the $i$-ti row and $j$-th column in the given world.
#
# Example (the matrix world_1 is defines above):
# 
#     >>> alive(world_1, 2, 0)
#     2
# 
# Note: It is a custom in Python that indices start with the number 0.
##########################################################################



##########################################################################
# Write a function game(world) that returns the matrix which represents
# the next state of the world. (The rules for obtaining the new state are
# defined above.)
# 
# Example (matrix world_1 is defined above):
# 
#     >>> game(world_1)
#     [[False, False, False, False, False, False],
#      [False, False, False, False, False, False],
#      [False, False, True, True, True, False],
#      [False, True, True, True, False, False],
#      [False, False, False, False, False, False],
#      [False, False, False, False, False, False]]
##########################################################################



##########################################################################
# Write a function population(world, n) that makes n steps in the game
# and returns a list of numbers – the number of alive cells in each
# step of the game (including the initial state of the world).
#
# Example (the matrix world_1 is defined above):
# 
#     >>> population(world_1, 3)
#     [6, 6, 6, 6]
# 
# Hint: Write a helper function that returns the number of alive cells
# in the world.
##########################################################################



##########################################################################
# Below are two more worlds which you can use for testing your code.
##########################################################################
world_3 = [
    [False, False, False, False, False, False],
    [False, True, True, False, False, False],
    [False, True, True, False, False, False],
    [False, False, False, True, True, False],
    [False, False, False, True, True, False],
    [False, False, False, False, False, False]
]

world_4 = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]
