import math 

for i in range(20, math.factorial(20)):
    if i % 20 == 0 and i % 19 == 0 and i % 18 == 0 and i % 17 == 0 and i % 16 == 0 and i % 14 == 0 and i % 13 == 0 and i % 11 == 0:
        print(i)
        break 
     