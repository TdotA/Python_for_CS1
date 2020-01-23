from functions import is_prime 
c=1
while c < 10002:
    i = 3
    if c == 10001:
        break
    while i < 10**10:
        if is_prime(i) == True:
            c+=1
            i+=2
        else:
            i+=2
print(str(i))