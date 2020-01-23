def is_nondecreasing(s):
    first = s[0]
    rest = s[1:]
    if len(rest) == 0: 
        return True
    if first > rest[0]:
        return False
    return is_nondecreasing(rest) 
#print(is_nondecreasing([1,2,13, 2]))

def addone(s): 
    l = []
    for i in s: 
        i = i+s.index(i) + 1
        l.append(i)
    return l

def lean(s):
    
    if len(s) == 0:
        return s
    first = s[0]
    l = [first]
    rest = addone(s[1:]) 
    return l + rest 
print(lean([1,2,3]))

