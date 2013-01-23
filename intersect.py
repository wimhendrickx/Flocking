import math

def getIntersectingPoints(circlecenter_x, circlecenter_y, radius, point_x, point_y):
    """
    find the intersecting points between the circle and the line through the circle center and one other point
    """
    dx = point_x - circlecenter_x
    dy = point_y - circlecenter_y
    A = dx*dx + dy*dy
    #B = 2*(dx*(circlecenter_x - circlecenter_x) + dy*(circlecenter_y - circlecenter_y))
    B = 0 # the previous formula evaluates to 0
    #C = (circlecenter_x - circlecenter_x) * (circlecenter_x - circlecenter_x) + (circlecenter_y - circlecenter_y) * (circlecenter_y - circlecenter_y) - radius * radius
    C = - radius * radius # simplify previous line

    det = B * B - 4 * A * C

    if det < 0.0000001 or det < 0:
	#no points
        points = []
    elif det == 0:
        #one point
	t = -B/(2*A)
	new_point_x = point_x + t*dx
	new_point_y = point_y + t*dy
	points = [[new_point_x, new_point_y],]
    else:
	#two points
	t = float((-B + math.sqrt(det)) / (2*A))
	new_point1_x = point_x + t*dx
	new_point1_y = point_y + t*dy
	t2 = float((-B - math.sqrt(det)) / (2*A))
	new_point2_x = point_x + t2*dx
	new_point2_y = point_y + t2*dy
	points =[[new_point1_x, new_point1_y], [new_point2_x, new_point2_y]]

    return points

def getnearestPoint(ref_point_x, ref_point_y, point1_x, point1_y, point2_x, point2_y):
    dist1 = distanceBetweenPoints(ref_point_x, ref_point_y, point1_x, point1_y)
    dist2 = distanceBetweenPoints(ref_point_x, ref_point_y, point2_x, point2_y)
    if dist1 == dist2:
	point = []
    elif dist1 < dist2:
        point = [point1_x, point1_y]
    else:
        point = [point2_x, point2_y]
    return point

def distanceBetweenPoints(point1_x, point1_y, point2_x, point2_y):
    pass
