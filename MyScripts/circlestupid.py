import random 

n = 10000000
points_inside = 0
i = 0
while i < n:
    
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x**2 + y**2)  <= 1 :
        points_inside += 1
    i +=1
#print('Number of dots inside the circle is: ' + str(points_inside))
print(str(4 * points_inside/n))