from medium import list_to_str
def emphasise(title):
    emphasised = ''
    for char in title: 
        emphasised = emphasised + char.upper() + ' '
    return emphasised
#print(emphasise('jjajjj'))  

#def emphasise_marked(text):
#    for char in text: 
#        if char == "*":
#            while list(text) 
#print(emphasise_marked('Breaking *news* on Donald *Trump*'))

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
#print (is_palindrome('nino'))

def almost_palindrome(s):
    for char in s: 
        if is_palindrome(s.replace(char,'')) == True:
            return True
    
    return False
#print(almost_palindrome('nino'))

def pseudo_palindrome(s):
    for c in 'ab':
        y = []
        list_s = list(s)
        if is_palindrome(c + s) == True:
            return True
        else:
            for char in s:
                replaced = s.replace(char, c)
                deleted = s.replace(char, '')
                index = list_s.index(char)
                list_s = list_s.insert(index, c)
                y = y + list_s
                y1 = join(y)
                if  (is_palindrome(n) == True) or is_palindrome(x) == True or is_palindrome(y1) == True:
                    return True
    return False  
print (pseudo_palindrome('jana'))
print (pseudo_palindrome('robot'))
print (pseudo_palindrome('anja'))


