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
