##########################################################################
# Geometry 
#
# In this exercise you will implement classes Vector, Point and Line
# that represent vector, point and line in the Euclidean plane. Some
# of the methods are already implemented. You will add more functionality.
##########################################################################

import math

# Constants
EPS = 1e-12

# Helper functions
def eq(a, b, eps=EPS):
    return abs(a - b) < eps

class Vector:
    """
    Vector in the Euclidean plane.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        Return True if the two vectors are equal.
        """
        return eq(self.x, other.x) and eq(self.y, other.y)

    def __add__(self, other):
        """
        Return the sum of vectors self and other.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def dot_product(self, other):
        """
        Return the dot product of vectors self and other.
        """
        return self.x * other.x + self.y * other.y

    def __mul__(self, other):
        """
        Return the dot product of vectors self and other if other is also a vector.
        Otherwise, return the product of vector self by the scalar other (if other is a scalar).
        """
        if type(other) == Vector:
            return self.dot_product(other)
        else:
            return Vector(self.x * other, self.y * other)

    def normalized(self):
        """
        Return the normalized vector.
        """
        return self / abs(self)


class Point:
    """
    Point in the Euclidean plane.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        """
        Return True if the two points are equal.
        """
        return eq(self.x, other.x) and eq(self.y, other.y)

    def __sub__(self, other):
        """
        Return the vector that that starts at other and ends at self.
        """
        return Vector(self.x - other.x, self.y - other.y)

    def translated(self, v):
        """
        Return the point that is obtained as translation of self by the vector v.
        """
        return Point(self.x + v.x, self.y + v.y)

    def __add__(self, v):
        """
        Return the point that is obtained as translation of self by the vector v.
        """
        return self.translated(v)

    def distance_to(self, other):
        """
        Return the distance from point self to the object other. The object other can
        be of class Point or of class Line.
        """
        if type(other) == Point:
            return abs(self - other)
        elif type(other) == Line:
            return abs(other.signed_distance(self))
        else:
            raise TypeError("operation unsupported for types: '{0}' and '{1}'".format(type(self), type(other)))


class Line:
    """
    Line in the Euclidean plane.
    
    The line is represented by a point and a normal vector.
    """

    def __init__(self, point, normal):
        self.point = point
        self.normal = normal

    def __repr__(self):
        return 'Line({0}, {1})'.format(self.point, self.normal)
    
    def coefficients(self):
        """
        Return the coefficients a, b and c from the equation :math:`a x + b y = c`.
        """
        a, b = self.normal.x, self.normal.y
        c = self.normal.dot_product(self.point)
        return a, b, c

    def __str__(self):
        a, b, c = self.coefficients()
        return '{0} x + {1} y = {2}'.format(a, b, c)

    def direction_vector(self):
        """
        Return a vector that lies on the line self.
        """
        a, b = self.normal.x, self.normal.y
        return Vector(-b, a)

    def perpendicular_line(self, point=None):
        """
        Return a line that is perpendicular to line self. If the argument point is
        given then the line goes through the provided point.
        """
        if point is None:
            point = self.point
        return Line(point, self.direction_vector())

    def signed_distance(self, point):
        """
        Return the signed distance from point point to line self.
        """
        return self.normal.normalized() * (point - self.point)


##########################################################################
# Add the method __repr__(self) to the class Vector.
#
# Example:
# 
#     >>> v = Vector(3, 2)
#     >>> v
#     Vector(3, 2)
##########################################################################
class Vector(Vector):
    def __repr__(self):
        return 'Vector({0},{1})'.format(self.x, self.y)



##########################################################################
# Add the method __str__(self) to the class Vector.
# 
# Example:
#
#     >>> v = Vector(3, 2)
#     >>> print(v)
#     (3, 2)
##########################################################################
class Vector(Vector):
    def __str__(self):
        return '({0},{1})'.format(self.x, self.y)



##########################################################################
# In the class Vector write a method __abs__(self) that returns the
# length of the vector self.
#
# Example:
# 
#     >>> v = Vector(1, 3)
#     >>> abs(v)
#     3.1622776601683795
##########################################################################
class Vector(Vector):
    def __abs__():
        return abs(sqrt((self.x**2 + self.y**2)))



##########################################################################
# In the class Vector write a method __sub__(self, other) that returns
# the vector difference of vectors self and other.
#
# Example:
# 
#     >>> v = Vector(-1, 3)
#     >>> u = Vector(2, 1)
#     >>> u - v
#     Vector(-3, 2)
##########################################################################
class Vector(Vector):
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)



##########################################################################
# In the class Vector write a method __truediv__(self, scalar) that
# returns the product of vector self by the scalar 1 / scalar.
#
# Example:
# 
#     >>> Vector(-1, 3) / 2
#     Vector(-0.5, 1.5)
##########################################################################
class Vector(Vector):
    def __truediv__(self, scalar):
        return Vector(self.x/scalar , self.y/scalar)


##########################################################################
# In the class Vector write a method is_perpendicular_to(self, other)
# that returns True if vector self is perpendicular to vector other.
# Otherwise, the function should return False.
#
# Example:
# 
#     >>> v = Vector(-1, 3)
#     >>> u = Vector(2, 1)
#     >>> v.is_perpendicular_to(u)
#     False
##########################################################################
class Vector(Vector):
    def is_perpendicular(self, other): 
        if self.dot_product(other) == 0:
            return True
        else:
            return False



##########################################################################
# In the class Vector write a method rotated(self, alpha) that returns
# a new vector which is obtained from self by rotating it by the angle
# alpha (in radians).a
#
# Example:
# 
#     >>> Vector(1, 0).rotated(math.pi / 4)
#     Vector(0.7071067811865476, 0.7071067811865475)
##########################################################################
class Vector(Vector):
    def rotated(self, alpha):
        return Vector(self.x * math.cos(alpha) - self.y * math.sin(alpha), self.x * math.sin(alpha) + self.y * math.cos(alpha))



##########################################################################
# In the class Line write a method projection_of(self, point) that returns
# the projection of the point point on the line self.
#
# Example:
# 
#     >>> p = Line(Point(1, 1), Vector(0, 1))
#     >>> p.projection_of(Point(3, 0))
#     Point(3, 1)
##########################################################################


##########################################################################
# In the class Line write a method intersection(self, other) that returns
# the point which is obtaned as intersection of lines self and other.
#
# Example:
# 
#     >>> p = Line(Point(3, 4), Vector(2, -1))
#     >>> q = Line(Point(0, 1), Vector(1, 2))
#     >>> p.intersection(q)
#     Point(1.2, 0.4)
##########################################################################
class Line(Line):
    def intersection(self,other):
        a,b,c = self.coefficients()
        d,e,f = other.coefficients()
        x = (b*f-e*c)/(-e*a +b*d)
        return Point(x,(a*x-c)/(-b))

class Line(Line):
    def projection_of(self, point):
        c = self.perpendicular_line(point)
        return self.intersection(c)

p = Line(Point(1, 1), Vector(0, 1))
print(p.projection_of(Point(3, 0)))



##########################################################################
# In the class Point write a method reflect_over_line(self, line) that
# returns the mirror image of the point self over the line line.
#
# Example:
# 
#     >>> p = Line(Point(1, 1), Vector(0, 1))
#     >>> Point(3, 4).reflect_over_line(p)
#     Point(3, -2)
##########################################################################
class Point(Point):
    def reflect_over_line(self, line): 
        c = line.perpendicular_line(self) 
        x = line.intersection(c)
        f,e = self.x - x.x , self.y - x.y 
        return Point(x.x - f, x.y - e)

p = Line(Point(1, 1), Vector(0, 1))

print(Point(3, 4).reflect_over_line(p))
