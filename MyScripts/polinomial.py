import math

def p(x):
    return x**5 - 5 * x**4 - 11 * x**3 + 55 * x**2 + 18 * x -90
a=1
b=2
pa=p(a)
pb=p(b)
i=0
while abs(a-b) > 10**-9:
   c = (a+b)/2
   pc = p(c)
   if pc == 0 :
       print('Zero is in: ' + str(c))
   elif pc > 0 :
       b = c
   else: 
       a = c
   print (str(i))
   i+=1
print ('Zero is in: ' + str(c))