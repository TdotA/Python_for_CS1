import unittest

from geometry import *

class GeometryTest(unittest.TestCase):
    
    def test_vector_repr(self):
        self.assertEqual(repr(Vector(3, 2)), 'Vector(3, 2)')
        self.assertEqual(repr(Vector(1, 0.5)), 'Vector(1, 0.5)')
        self.assertEqual(repr(Vector(-1, 0.5)), 'Vector(-1, 0.5)')
        self.assertEqual(repr(Vector(1, -0.5)), 'Vector(1, -0.5)')

    def test_vector_str(self):
        self.assertEqual(str(Vector(3, 2)), '(3, 2)')
        self.assertEqual(str(Vector(1, 0.5)), '(1, 0.5)')
        self.assertEqual(str(Vector(-1, 0.5)), '(-1, 0.5)')
        self.assertEqual(str(Vector(1, -0.5)), '(1, -0.5)')

    def test_vector_abs(self):
        self.assertAlmostEqual(abs(Vector(1, 3)), 3.1622776601683795, places=10)
        self.assertAlmostEqual(abs(Vector(1, 0.5)), 1.118033988749895, places=10)
        self.assertAlmostEqual(abs(Vector(-10, 3)), 10.44030650891055, places=10)
        self.assertAlmostEqual(abs(Vector(1, -30)), 30.01666203960727, places=10)
        self.assertAlmostEqual(abs(Vector(-6, -5)), 7.810249675906654, places=10)

    def test_vector_sub(self):
        self.assertEqual(Vector(-1, 3) - Vector(2, 1), Vector(-3, 2))
        self.assertEqual(Vector(5, 3) - Vector(2, 1), Vector(3, 2))
        self.assertEqual(Vector(1, -3) - Vector(2, 1), Vector(-1, -4))
        self.assertEqual(Vector(1, 3) - Vector(-2, 1), Vector(3, 2))
        self.assertEqual(Vector(-1, 3) - Vector(2, -1), Vector(-3, 4))

    def test_vector_truediv(self):
        self.assertEqual(Vector(-1, 3) / 2, Vector(-0.5, 1.5))
        self.assertEqual(Vector(-1, 3) / 7, Vector(-0.14285714285714285, 0.42857142857142855))
        self.assertEqual(Vector(2, 3) / 0.3, Vector(6.666666666666667, 10.0))
        self.assertEqual(Vector(5, 7) / 11, Vector(0.4545454545454546, 0.6363636363636364))

    def test_vector_perpendicular_to(self):
        self.assertFalse(Vector(-1, 3).is_perpendicular_to(Vector(2, 1)))
        self.assertFalse(Vector(1, 3).is_perpendicular_to(Vector(3, 1)))
        self.assertTrue(Vector(-1, 3).is_perpendicular_to(Vector(-3, -1)))
        self.assertTrue(Vector(-2, 6).is_perpendicular_to(Vector(-3, -1)))
        self.assertTrue(Vector(-1, 3).is_perpendicular_to(Vector(3, 1)))
        self.assertTrue(Vector(-1, 3).is_perpendicular_to(Vector(6, 2)))

    def test_vector_rotated(self):
        self.assertEqual(Vector(1, 0).rotated(math.pi / 4), Vector(0.7071067811865476, 0.7071067811865475))
        self.assertEqual(Vector(0, 1).rotated(math.pi / 4), Vector(-0.7071067811865476, 0.7071067811865475))
        self.assertEqual(Vector(2, 0).rotated(math.pi / 4), Vector(1.4142135623730951, 1.4142135623730951))
        self.assertEqual(Vector(0, 2).rotated(math.pi / 4), Vector(-1.4142135623730951, 1.4142135623730951))
        self.assertEqual(Vector(1, 0).rotated(math.pi / 2), Vector(0.0, 1.0))
        self.assertEqual(Vector(1, 0).rotated(math.pi), Vector(-1.0, 0.0))
        self.assertEqual(Vector(1, 0).rotated(3 * math.pi / 2), Vector(0.0, -1.0))
        self.assertEqual(Vector(1, 0).rotated(2 * math.pi), Vector(1, 0))
        self.assertEqual(Vector(3, 2).rotated(0.5), Vector(1.6738966084627123, 3.1934417395933545))

    def test_line_projection_of(self):
        self.assertEqual(Line(Point(1, 1), Vector(0, 1)).projection_of(Point(3, 0)), Point(3.0, 1.0))
        self.assertEqual(Line(Point(0, 1), Vector(1, 2)).projection_of(Point(3, 4)), Point(1.2, 0.4))
        self.assertEqual(Line(Point(-2, -2), Vector(0.410958904109589, -1.09589041095890)).projection_of(Point(0, 4)), Point(1.72602739726027, -0.602739726027397))

    def test_line_intersection(self):
        self.assertEqual(Line(Point(3, 4), Vector(2, -1)).intersection(Line(Point(0, 1), Vector(1, 2))), Point(1.2, 0.4))
        self.assertEqual(Line(Point(3, 4), Vector(2, -1)).intersection(Line(Point(0, 1), Vector(-1, -2))), Point(1.2, 0.4))
        self.assertEqual(Line(Point(2, 1), Vector(-2, 4)).intersection(Line(Point(-3, 4), Vector(6, 2))), Point(-1.428571428571429, -0.714285714285714))
        self.assertEqual(Line(Point(2, 1), Vector(2, -4)).intersection(Line(Point(-2, 1), Vector(6, 2))), Point(-1.428571428571429, -0.714285714285714))

    def test_point_reflect_over_line(self):
        self.assertEqual(Point(3, 4).reflect_over_line(Line(Point(1, 1), Vector(0, 1))), Point(3, -2))
        self.assertEqual(Point(3, 4).reflect_over_line(Line(Point(0, 1), Vector(1, 2))), Point(-0.6, -3.2))
        self.assertEqual(Point(0, 4).reflect_over_line(Line(Point(-2, -2), Vector(0.410958904109589, -1.09589041095890))), Point(3.45205479452055, -5.20547945205479))


if __name__ == '__main__':
    unittest.main()
