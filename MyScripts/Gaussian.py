from fractions import Fraction

def fraction_to_str(f):
    if f.denominator == 1:
        return '{0}'.format(f.numerator)
    return '{0}{1}'.format(f.numerator, f.denominator)

def display(A,b):
    n = len(A)
    for i in range (n):
        line = ''
        for j in range(n):
            line = line + '{0:>6}'.format(fraction_to_str(A[i][j]))
        line = line + '|' + '{0:>6}'.format(fraction_to_str(b[i]))
        print(line)

def solve_system(A, b):
    n = len(A)
    b = [Fraction(x) for x in b]
    A = [[Fraction(x) for x in line] for line in A]

    for i in range(n - 1): 
        i0 = i
        while A[i0][i] == 0: 
            i0 = i0 + 1
        for k in range(i, n):
            A[i][k], A[i0][k] = A[i0][k], A[i][k]
        b[i], b[i0] = b[i0], b[i]
        for j in range (i+1,n):
            k = -A[j][i]/A[i][i]
            for l in range(i, n):
                A[j][l] = A[j][l] + k* A[i][l]
            b[j]= b[j] + k*b[i]
    x = [0 for i in range(n)]
    for j in range(n-1,-1,-1):
        x[j] = (b[j] - sum([A[j][i] * x[i] for i in range(j+1,n)]))/A[j][j]
    return x
    
A = [
    [1,2, 0, 0],
    [2,0,-1,0],
    [1,1,0,1],
    [2,0,-2,-1]
]
b = [1,0,2,-1]

display(A,b)
print(solve_system(A,b))