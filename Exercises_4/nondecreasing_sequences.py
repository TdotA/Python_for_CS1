##########################################################################
# Nondecreasing sequences 
#
# A finite sequence of integers $a_1, a_2, \ldots, a_n$ ($n \ge 1$)
# is _nondecreasing_ if $a_i \le a_{i+1}$ for all $i=1, \ldots, n-1$.
# Such a sequence can be represented with a list. For example
# 
#     [-3, -1, 0, 5, 7, 8]
# 
# is a nondecreasing sequence.
# 
# You must solve those tasks with recursion (for and while loops are
# not allowed)!
##########################################################################



##########################################################################
# Write a function is_nondecreasing(s) that takes a finite sequence of
# integers and returns True if the sequence is nondecreasing, otherwise
# False.
#
# Example:
# 
#     >>> is_nondecreasing([1, 2, 3])
#     True
#     >>> is_nondecreasing([-1, 3, 2])
#     False
##########################################################################

def is_nondecreasing (s):
    if len(s) == 1 :
        return True 
    if s[-1] >= s[-2] :
        return is_nondecreasing(s[:-1])
    else : 
        return False
print(is_nondecreasing([1, 2, 2]))
##########################################################################
# A given sequence of integers $a_1, a_2, \ldots, a_n$ can be _leaned_,
# so that we obtain the sequence $a_1, a_2 + 1, a_3 + 2, \ldots, a_n + (n-1)$.
# 
# Write a function lean(s) which takes the sequence s as the argument.
# The function shuld return the corresponding leaned sequence.
#
# Example:
# 
#     >>> lean([2, 4, 1])
#     [2, 5, 3]
#     >>> lean([4, 0, 5, 5])
#     [4, 1, 7, 8]
##########################################################################
def lean(s):
    n = len(s)
    if n == 1:
        return s 
    s[-1]= s[-1] + n-1
    l = lean(s[:-1])
    l.append(s[-1])
    return l 


#print(lean([2, 4, 1, 2]))
    


##########################################################################
# The function lean has the property that it can turn a sequence which
# is not nondecreasing into a nondecreasing sequence.
# 
# Write a function make_nondecreasing(s) that takes a sequence of integers
# and uses the function lean on it for as many times as it is needed for
# the sequence to become nondecreasing. If the sequence s is nondecreasing
# at the beginning, the function should return it unchanged.
#
# Example:
# 
#     >>> make_nondecreasing([1, 3, 2, 4])
#     [1, 4, 4, 7]
#     >>> make_nondecreasing([1, 3, 0, 0])
#     [1, 6, 6, 9]
#     >>> make_nondecreasing([0, 0, 1, 1])
#     [0, 0, 1, 1]
##########################################################################


def make_nondecreasing(s):
    if is_nondecreasing(s) == False: 
        return make_nondecreasing(lean(s))
    else : 
        return s
print(make_nondecreasing([1,3,2,4]))