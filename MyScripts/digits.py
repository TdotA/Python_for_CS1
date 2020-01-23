import math

n = int(input('Enter the number: '))

sum = 0 

while n>0 :
    digit = n % 10
    n = n // 10
    sum = sum + digit
    
print (str(sum))