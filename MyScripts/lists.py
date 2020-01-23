circles = [(0,0 ,1), (1, 0, 0.5), (0, 1.5, 1.5)]
def in_union(x, y, circles):
    for i in circles:
        if ((x-i[0])**2 + (y - i[1])**2 )<= i[2]**2:
            return True 
            break
    return False
#print (in_union(3, 1, circles)) 

def in_intersection(x, y, circles):
    c = 0 
    for i in circles:
        if ((x-i[0])**2 + (y - i[1])**2 )<= i[2]**2:
            c+= 1
    if c == 3:
        return True
    else: 
        return False
#print (in_intersection(0.8, 0.3, circles))
def bounding_box (circles) :
    line_ya = max((circles[0][2] + circles[0][1]), (circles[1][2] + circles[1][1]), (circles[2][2] + circles[2][1]))
    line_yb = min((circles[0][1] - circles[0][2]), (circles[1][1] - circles[1][2]), (circles[2][1] - circles[2][2]))
    line_xa = max((circles[0][2] + circles[0][0]), (circles[1][2] + circles[1][0]), (circles[2][2] + circles[2][0]))
    line_xb = min((circles[0][0] - circles[0][2]), (circles[1][0] - circles[1][2]), (circles[2][0] - circles[2][2]))
    print (str(line_xb) + ',' + str(line_yb) + ';'+ str(line_xa) + ',' + str(line_ya))


def approximate_area(circles, n):
    x1 = max((circles[0][2] + circles[0][0]), (circles[1][2] + circles[1][0]), (circles[2][2] + circles[2][0]))
    x2 = min((circles[0][0] - circles[0][2]), (circles[1][0] - circles[1][2]), (circles[2][0] - circles[2][2]))
    y1 = max((circles[0][2] + circles[0][1]), (circles[1][2] + circles[1][1]), (circles[2][2] + circles[2][1]))
    y2 = min((circles[0][1] - circles[0][2]), (circles[1][1] - circles[1][2]), (circles[2][1] - circles[2][2]))
    points_inside = 0
    for i in range(n):
        x = random.uniform(x2, x1)
        y = random.uniform(y2, y1)
        if in_union(x, y, circles):
            points_inside += 1
    area = abs(x1-x2) * abs(y1-y2)
    print(str(area*points_inside/n))
approximate_area(circles, 1000000)

