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

    def test_distance(self):
        point1_x = -2
	point1_y = 1
	point2_x = 1
	point2_y = 5
	expected_distance = 5
	self.assertEqual(expected_distance, intersect.distanceBetweenPoints(point1_x, point1_y, point2_x, point2_y))

    def test_distance_zero(self):
        point1_x = 1
	point1_y = 1
	point2_x = 1
	point2_y = 1
	expected_distance = 0
	self.assertEqual(expected_distance, intersect.distanceBetweenPoints(point1_x, point1_y, point2_x, point2_y))

    def test_getnearestPoint(self):
	ref_point_x = 1
	ref_point_y = 1
        point1_x = 2
	point1_y = 2
	point2_x = 3
	point2_y = 3
	expected_point = [point1_x, point1_y]
	self.assertEqual(expected_point, intersect.getnearestPoint(ref_point_x, ref_point_y, point1_x, point1_y, point2_x, point2_y))

    def test_getnearestPoint_equal(self):
	ref_point_x = 1
	ref_point_y = 1
        point1_x = 2
	point1_y = 2
	point2_x = point1_x
	point2_y = point1_y
	expected_point = []
	self.assertEqual(expected_point, intersect.getnearestPoint(ref_point_x, ref_point_y, point1_x, point1_y, point2_x, point2_y))

    def test_getIntersectingPoints_notequalfromstartpoint(self):
        self.assertNotEqual([1, 1],intersect.getIntersectingPoints(1,1,3,100,100))

    def test__getIntersectingPoints_find1point(self):
        #afstand tussen de punten zou 295.169442863 zijn < g_flapperafstand
        self.assertEqual(2,len(intersect.getIntersectingPoints(546,565,50,283.0,412.0)))

    def test_isIntersectingCircles_false(self):
        self.assertFalse(intersect.isIntersectingCircles(1,1,2,8,8,3))

    def test_isIntersectingCircles_(self):
        self.assertTrue(intersect.isIntersectingCircles(1,1,5,8,8,5))

    def test_isIntersectingCircles_circlestouch(self):
        self.assertTrue(intersect.isIntersectingCircles(1,1,2,3,1,2)) 
    
    def test_isIntersectingCircles_circlescross_1(self):
        self.assertFalse(intersect.isIntersectingCircles(30,35,3,40,45,3))   
