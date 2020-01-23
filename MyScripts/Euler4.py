def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
m = 0
for i in range (100, 1000):
    for j in range (100, 1000):
        k = j*i
        if is_palindrome(str(k)) == True:
            m = max(m, k) 
        else: 
            pass
print(m)
