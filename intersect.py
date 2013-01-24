import math

def getIntersectingPoints(point_x, point_y, radius, circlecenter_x, circlecenter_y):
    """
    find the intersecting points between the circle and the line through the circle center and one other point
    """
    dx = point_x - circlecenter_x
    dy = point_y - circlecenter_y
    A = dx*dx + dy*dy
    #B = 2*(dx*(circlecenter_x - circlecenter_x) + dy*(circlecenter_y - circlecenter_y))
    B = 0 # the previous formula evaluates to 0
    #C = (circlecenter_x - circlecenter_x) ** 2 + (circlecenter_y - circlecenter_y) ** 2 - radius * radius
    C = - radius * radius # simplify previous line

    det = B ** 2 - 4 * A * C

##    print('getIntersectingPoints: %s' % (det))
    
    points = []
    if det < 0.0000001 or det < 0:
	#no points
        pass
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

	if ((point_x < new_point1_x and new_point1_x < circlecenter_x) or (point_x > new_point1_x and new_point1_x > circlecenter_x)) and ((point_y < new_point1_y and new_point1_y < circlecenter_y) or (point_y > new_point1_y and new_point1_y > circlecenter_y)):
            points.append([new_point1_x, new_point1_y])
        if ((point_x < new_point2_x and new_point2_x < circlecenter_x) or (point_x > new_point2_x and new_point2_x > circlecenter_x)) and ((point_y < new_point2_y and new_point2_y < circlecenter_y) or (point_y > new_point2_y and new_point2_y > circlecenter_y)):
            points.append([new_point2_x, new_point2_y])
##	points =[[new_point1_x, new_point1_y], [new_point2_x, new_point2_y]]

##    print ('getIntersectingPoints: %s' % (points))
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
    dist = math.sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)
    return dist

def getIntersectingPointsOnSegment():
    pass
