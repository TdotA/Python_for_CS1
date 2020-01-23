##########################################################################
# Armoured strings 
##########################################################################



##########################################################################
# Write a function count_angles(s) that counts the number of angle brackets,
# i.e., '<' and '>', in the given string s.
#
# Example:
# 
#     >>> count_angles('<abc>>')
#     3
#     >>> count_angles('a>>  x<Y>x  <<b')
#     6
#     >>> count_angles('How many > and < are in this string?')
#     2
##########################################################################

def count_angles(s):
    sum = 0
    for c in s: 
        if c == '<' or c == '>':
            sum = sum + 1 
        else:
            continue
    return sum

#print(count_angles('How many > and < are in this string?'))

##########################################################################
# We say that a string is armoured if starts with a '<', ends with a
# '>', and contains no other angle bracket besides those two. For example,
# the string '<The sun is shining.>' is an armoured string.
# 
# Write a function is_armoured(s) which return True if the string s is
# armoured, and False otherwise.
#
# Example:
# 
#     >>> is_armoured('<The sun is shining.>')
#     True
#     >>> is_armoured('<   <3   >')
#     False
#     >>> is_armoured('The sun is shining.')
#     False
##########################################################################

def is_armoured(s):
    if count_angles(s) == 2 and s[0] == '<' and s[-1] == '>' :
        return True
    else:
        return False 

#print(is_armoured('<The sun is shining.<'))
##########################################################################
# Write a function glue(s1, s2) that takes two armoured strings and glues
# them together so that the results is an armoured string. (See the example
# below.)
#
# Example:
# 
#     >>> glue('<123>', '<456>')
#     '<123456>'
#     >>> glue('<muca>', '<copatarica>')
#     '<mucacopatarica>'
##########################################################################

def glue(s1, s2):
    c ='' 
    for i in s1:
        if i == '>':
            break
        else:
            c = c+ i
    for j in s2:
        if j == '<':
            continue
        else:
            c = c + j
    return c 

print(glue('<123>', '<456>'))
##########################################################################
# Write a function break_to_pieces(s, l) that takes an armoured string s
# and a list of non-negative numbers l. The function should break the string
# s into pieces such that those pieces have lengths (angle brackets not
# considered) given by the list l.
#
#  Example:
# 
#     >>> break_to_pieces('<Zunaj sije sonce.>', [2, 7, 8])
#     ['<Zu>', '<naj sij>', '<e sonce.>']
#     >>> break_to_pieces('<muca copatarica>', [4, 0, 11])
#     ['<muca>', '<>', '< copatarica>']
# 
# Note: You can assume that the sum of numbers in the list l equals the
# length of the armoured string s (angle brackets not considered).
##########################################################################



