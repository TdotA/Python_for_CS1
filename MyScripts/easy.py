import math

def is_gaul(name):
    n=len(name)
    if name[n-2:n]=="ix":
        return True
    else:
        return False

#print('Funkcija 1: '+ str(is_gaul("Obelix")))

def contains_rec(a,b,c,d):
    if a>=c and d>=b:
        return True
    else:
        return False

#print('Funkcija 2: '+ str(contains_rec(6.9, 4.15,5.3,12.9)))

def contact_card(name):
    n=len(name)
    print('*'*(n+4))
    print('*'+' '*(n+2)+'*')
    print('* '+name+' *')
    print('*'+' '*(n+2)+'*')
    print('*'*(n+4))
    return 
#contact_card('Jelena Glisic')

def f_to_c(t):
    c=(t-32)*5/9
    return c

#print(f_to_c(77.5))

def sine_table(deg):
    i=0
    while i*deg < 360:
        print('sin(' + (str(i*deg)) +')' +' = ' + str(math.sin(math.radians(i*deg))))
        i=i+1

#sine_table(30)

def sums(n):
    i=1
    j=1
    s1=0
    s2=0
    s3=0
    while i <= n :
        while j <= i: 
            s1 = s1 + j 
            s2 = s2 + j**2
            s3 = s3 + j**3
            j = j+1
        print (str(s1) + ' ' + str(s2) + ' ' +str(s3) + '\n')
        i = i+1
#sums(5) 

def find_numbers():
    n=1000
    while n < 10000:
        a=n//1000
        b=(n//100)%10
        c=(n//10)%10
        d=n%10
        if (a-b)==(c+d):
            print n
        n= n+1

#find_numbers()

def combination_lock (a , b):
    a1=a//1000
    a2=(a//100)%10
    a3=(a//10)%10
    a4=a%10
    b1=b//1000
    b2=(b//100)%10
    b3=(b//10)%10
    b4=b%10
    first_clicks = min((math.sqrt((b1-a1)**2)),(min(b1,a1) + 10 - max(b1,a1)))
    second_clicks = min((math.sqrt((b2-a2)**2)),(min(b2,a2) + 10 - max(b2,a2)))
    third_clicks = min((math.sqrt((b3-a3)**2)),(min(b3,a3) + 10 - max(b3,a3)))
    fourth_clicks = min((math.sqrt((b4-a4)**2)),(min(b4,a4) + 10 - max(b4,a4)))
    minimum = first_clicks+second_clicks+third_clicks+fourth_clicks
    print minimum

#combination_lock(2222,3131)
    
def screen_size(diag,w,h):
    a= diag/(math.sqrt(1+((w**2)/(h**2))))
    b= diag/(math.sqrt(1+((h**2)/(w**2))))
    print(a,b)

screen_size(52,16,9)