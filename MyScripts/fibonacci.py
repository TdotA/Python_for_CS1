def fibonacci(n):
    if n == 1 :
        return 1
    elif n==0 :
        return 0 
    else:  
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(10))

def binomial(n,k):
    if n==k or k<=0:
        return 1 
    elif n<k:
        return 0
    else:
        return binomial(n-1, k) + binomial(n-1, k-1)
#print(binomial(100,20))

def rec_sum(l):
    if len(l) == 0:
        return 0
    first = l[0]
    rest = l[1:]
    return rec_sum(rest) + first
#print(rec_sum([1,2,3,4,5]))

def merge(l_1, l_2):
    l=[]
    j=0
    i=0
    while i< len(l_1) and j <len(l_2):
        if l_1[i]<=l_2[j]:
            l.append(l_1[i])
            i = i+1
        else:
            l.append(l_2[j])
            j = j+1
    l.extend(l_1[i:])
    l.extend(l_2[j:])
    return l

#print(merge([1,2,3],[4,5,6]))

def merge_sort(l):
    if len(l)<=1:
        return l
    return merge(merge_sort(l[:len(l)//2]), 
           merge_sort(l[len(l)//2:]))
#print(merge_sort([1,5,3]))

def n_queens(n, q):
    c = len(q)
    sols = []
    for r in range(0, n):
        if len(q) == n:
            return [q]  
    
        is_good = True
        for c2 in range(len(q)):
            r2 = q[c2]
            if r == r2 or abs(r - r2) == abs(c - c2):
                is_good = False
                break
        if is_good: 
            sols.extend(n_queens(n, q + [r]))
            
    return sols

print(n_queens(8, []))


