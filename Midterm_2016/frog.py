##########################################################################
# The Frog 
##########################################################################



##########################################################################
# Write a function is_inside(point, rectangle) that for a given point
# returns True if the point is inside the rectangle (or on its boundary),
# and False otherwise. The point is given as a pair (x, y) and the
# rectangle is given as a tuple (x1, y1, x2, y2), where (x1, y1) and
# (x2, y2) are coordinates of two opposite vertices.
#
# Example:
#
#     >>> inside((1, 1), (0, 2, 2, 0))
#     True
#     >>> inside((2, 1), (0, 0, 1, 1))
#     False
##########################################################################



##########################################################################
# The frog is located on an Euclidean plane and it is jumping around.
# For each position of the frog we wrote down its x-coordinate in a list
# and also its y-coordinate in a different list.
# 
# Write a function path(lx, ly) that gets two lists – the x-coordinates
# and the y-coordinates of the frog. The function should return a list
# of points that describes the movement of the frog. You can assume that
# lists lx and ly will have equal lengths.
#
# Example:
#
#     >>> path([0, 0, 1, 2], [0, 1, 2, 1])
#     [(0, 0), (0, 1), (1, 2), (2, 1)]
##########################################################################



##########################################################################
# Write a function longest_jump(p) that gets a list which describes the
# path made by a frog. The function should return the length of the longest
# jump. If the frog did not make any jump, the function should return None.
#
# Example:
# 
#     >>> longest_jump([(0, 0), (0, 1), (1, 2), (2, 1)])
#     1.4142135623730951
##########################################################################



##########################################################################
# There is a rectangular pond in the plane. Write a function
# inside_pond(p, pond) that gets a list p which represents the path of a
# frog and a tuple pond which describes the pond (the pond is a rectangle
# and it is described as in the first subtask). The function should
# return a list of those positions on the path for which the frog was
# inside (or on the boundary of) the pond.
#
# Example:
# 
#     >>> inside_pond([(0, 1), (1, 2), (2, 1), (1, 1), (0, 0), (-1, 1)], (0, 0, 1, 1))
#     [(0, 1), (1, 1), (0, 0)]
##########################################################################


