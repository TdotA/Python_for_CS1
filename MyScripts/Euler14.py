def collatz_sequence(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    # Added line
       num_seq.append(x)    
    return len(num_seq)

m = 0  
n = 1000000  
x = 0
while n >= 1 :
    if collatz_sequence(n) > m:
        m = collatz_sequence(n)
        x = n
    n = n-1
print(x)
