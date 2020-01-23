def findDivisors(n):
    l =[]
    for i in range(1, n//2):
        if n % i == 0:
            l.append(i)
            l.append(n/i)
    return l

def is_abudant(n):
    x = []
    for i in range(1,n):
        l = findDivisors(i)
        if sum(l) > i:
            x.append(i)
    return x
c = is_abudant(28123//2)
for i in range (24,28123)
        