import unittest
import intersect

class Test_intersect(unittest.TestCase):
    def test_x_constant(self):
        px = 1
	py = 1
	radius = 1
	lpx = 1
	lpy = 8
	result1_x = 1.0
	result1_y = 2.0
	result2_x = 1.0
	result2_y = 0.0
	expected_result = sorted([[result1_x, result1_y], [result2_x, result2_y]]) 
	result = sorted(intersect.getIntersectingPoints(px, py, radius, lpx, lpy))
	self.assertEqual(expected_result, result)

    def test_y_constant(self):
        px = 1
	py = 1
	radius = 2
	lpx = 5
	lpy = 1
	result1_x = 3.0
	result1_y = 1.0
	result2_x = -1.0
	result2_y = 1.0
	expected_result = sorted([[result1_x, result1_y], [result2_x, result2_y]]) 
	result = sorted(intersect.getIntersectingPoints(px, py, radius, lpx, lpy))
	self.assertEqual(expected_result, result)

    def testdistance(self):
        point1_x = -2
	point1_y = 1
	point2_x = 1
	point2_y = 5
	expected_distance = 5
	self.assertEqual(expected_distance, intersect.distanceBetweenPoints(point1_x, point1_y, point2_x, point2_y))

    def testdistance_zero(self):
        point1_x = 1
	point1_y = 1
	point2_x = 1
	point2_y = 1
	expected_distance = 0
	self.assertEqual(expected_distance, intersect.distanceBetweenPoints(point1_x, point1_y, point2_x, point2_y))
