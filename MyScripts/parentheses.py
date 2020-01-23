def permute_string(str):
    if len(str) == 0:
	    return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

def all_expressions(n):
    list_n = []
    for i in range (0, n+1):
        line =''
        line = line + i*')' + (n-i) * '('
        list_n.append(line)
    list_f = []
    for element in list_n: 
        list_f = list_f + permute_string(element)
    return list_f

print(all_expressions(3))

def is_validly_nested(string): 
    sub = '()'
    while string != '':
        if sub in string: 
            string = string.replace(sub, '')
        else :
            return False
    return True
#print(is_validly_nested('((()))'))

def all_valid (n) : 
    x = all_expressions(n)
    final = []
    for element in x: 
        if is_validly_nested(element) == True:
            final.append(element)
        else :
            pass
    return final


#print(all_valid(6))

def max_level(string):
    level = 0
    sub = '()'
    while sub in string :
        string = string.replace(sub, '')
        if is_validly_nested(string) == True  :
            level = level+1
        else:
            pass
    return level
#print (max_level('()()'))

def valid_level (n,k):
    x = all_valid(n)
    final = []
    for element in x :
        if max_level(element) == k :
            final.append(element)
        else: 
            pass
    return final
#print(valid_level(6,2))