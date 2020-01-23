##########################################################################
# Write a function in_union(x, y, circles) which returns True if the
# point $(x, y)$ lies in at least one of the circles from the list
# circles. Otherwise, the function must return False.
#
# The list circles is comprised of triples of the form $(x_i, y_i, r_i)$.
# Each triple represents a circle with centre at $(x_i, y_i)$ and
# radius $r_i$.
#
# Example:
#
#     >>> circles = [(0, 0, 1), (1, 0, 0.5), (2.5, 1, 1.5)]
#     >>> in_union(3, 1, circles)
#     True
#     >>> in_union(0.75, 0, circles)
#     True
#     >>> in_union(0.75, 1, circles)
#     False
##########################################################################



##########################################################################
# Write a function in_intersection(x, y, circles) which returns True if
# the point $(x, y)$ lies in the intersection of all circles from the list
# circles. Otherwise, the function must return False.
#
# Example:
#
#     >>> circles = [(0, 0, 1), (1, 0, 0.5), (0, 1.5, 1.5)]
#     >>> in_intersection(0.8, 0.3, circles)
#     True
#     >>> in_intersection(0.75, 0, circles)
#     False
##########################################################################



##########################################################################
# Write a function bounding_box(circles) which finds the smallest rectangle
# that contains the union of circles from the list circles. Function should
# return a tuple of the form $(x_min, y_min, x_max, y_max)$, i.e., the
# coordinates of the bottom left corners followed by coordinates of the
# top right cornes.
#
# Example:
#
#     >>> circles = [(0, 0, 1), (1, 0, 0.5), (0, 1.5, 1.5)]
#     >>> bounding_box(circles)
#     (-1.5, -1, 1.5, 3)
##########################################################################



##########################################################################
# Write a function approximate_area(circles, n) which determines the area 
# of the union of circles using the Monte Carlo method:
#
# The function randomly picks n points in the bounding box of the union
# of circles. Then it counts the number of those points that lie in at
# least one of those circles. The approximate area can be obtain as the
# product of area of the bounding box and the ratio between the number
# of points inside the union and number n.
##########################################################################


