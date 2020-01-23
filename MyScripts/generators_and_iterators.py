fruit = ['banana', 'apple', 'pear', 'plum', 'watermelon']
"""
def iter(x): 
    return x.__iter__()

it = iter(fruit)
while True:
    try: 
        x = next(it)
    except StopIteration:
        break 
    print(x)
    """
class Collatz:
    def __init__(self,n):
        self.n = n
        self.burned_out = False

    def __iter__(self):
        return self 

    def __next__(self):
        if self.burned_out: 
            raise StopIteration
        ret = self.n
        if self.n % 2 == 0:
            self.n = self.n //2
        else: 
            self.n = 3 * self.n +1 
        if ret == 1: 
            self.burned_out = True
        return ret

#for x in Collatz(133331): 
#    print(x)

def collatz_degree(n): 
    count = 0 
    for x in Collatz(n):
        count = count + 1 
    return count

def collatz_peak(n): 
    peak = 1 
    for x in Collatz(n):
        peak = max(peak, x)
    return peak 




m = 1
for i in range(2, 10000): 
    if collatz_degree(i) > collatz_degree(m):
        m = i  
print(collatz_peak(97))


        