import math 
def area(n,a):
    area = (a**2 * n )/4* math.tan(math.pi/n)
    return area
#print(str(area(4,2)))
#print(str(area(3,2)))
#print(str(area(6,2)))

def is_leap_year (y):
    if (y % 4) == 0 :
        if (y % 100) == 0 : 
            if (y % 400) == 0 :
                return True 
            else :
                return False
        else :
            return True
    else:
        return False 

#print(str(is_leap_year(2000)))
#print(str(is_leap_year(1900)))

def cake(m , f, s):
    mf = f // 2
    mm = m // 0.8
    ms = s // 1.5

    return min(mf,mm, ms)
#print(str(cake(5, 7, 3.5)))



def is_prime (n):
    i = 2
    if n == 2 :
        return True
    else: 
        while i <= math.floor(math.sqrt(n))  :
            if (n % i) == 0 :
                return (False)
                break
            elif n % i != 0 and i == n-1:
                return True
                break
            else :
                i+=1
#print (is_prime(17))
#print (is_prime(16))

def nth_prime (n):
    if n == 1:
        return 2
    count = 1
    i = 3
    while count <= n:
        if is_prime(i) == True :
            count = count + 1
            if count == n :
                return i 
        
        i+=2
    
#print(str(nth_prime(10))) 


def next_prime(n):
    i = n + 1
    while is_prime(i) == False :
        if i % 2 == 0 :
            i+=1
        else :
            i+=2
    return i  
#print (str(next_prime(20)))