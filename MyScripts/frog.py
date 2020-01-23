import math 
def is_inside(point, rectangle):
    if point[0] >= min(rectangle[0], rectangle[2]) and point[0] <= max(rectangle[0], rectangle[2]) and point[1] >= min(rectangle[1], rectangle[3]) and point[1] <= max(rectangle[1], rectangle[3]): 
        return True
    else :
        return False
#print(is_inside((1, 1), (0, 2, 2, 0)))

def path(lx, ly):
    l = []
    for i in range(len(lx)) :
    
        p =(lx[i], ly[i])
        l.append(p)
        
    return l

#print(path([0, 0, 1, 2], [0, 1, 2, 1]))

def longest_jump(p) :
    d = 0
    for i in range(1, len(p)) :
        jump = 0
        jump += ((p[i-1][0]-p[i][0])**2+(p[i-1][1]-p[i][1])**2)**(1/2)
        d = max(d, jump)
    return d

#print(longest_jump([(0, 0), (0, 1), (1, 2), (2, 1)]))

def inside_pond(p, pond):
    lis = []
    for el in p: 
        if is_inside(el, pond) == True:
            lis.append(el)
        else:
            pass
    return lis
print(inside_pond([(0, 1), (1, 2), (2, 1), (1, 1), (0, 0), (-1, 1)], (0, 0, 1, 1)))