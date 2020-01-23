def find_div(x) :
    divisors = [] 
    for i in range(1, int(x**0.5)):
        if x % i == 0 and i!= x/i: 
            divisors.append(i)
            divisors.append(x/i)
        elif i == x/i:
            divisors.append(i)
        else:
            continue
    return len(divisors)

n = 1
div = find_div(n)
while div <= 500:
    k = n*(n+1)/2
    n = n+1
    div = find_div(k)   
print(k) 


