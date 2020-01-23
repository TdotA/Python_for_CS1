import math

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:   
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

i= 600851475143

while i > i**0.5 : 
    if 600851475143 % i == 0:
        if  is_prime(i) == True:
            print(i)
            break 
    else:
        i = i-2
