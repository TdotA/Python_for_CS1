##########################################################################
# The Fence
#
# We have a fence that is made of n wooden boards that are nailed
# together. In addition, we are given a list of characters that represent
# different colors; for example ['W', 'R', 'B']. (Suppose that 'W' stands
# for white, 'B' for blue and 'R' for red.) 
#
# Our task is to color the fence.
##########################################################################



##########################################################################
# Write a function all_colorings(n, c) that takes an integer n which is
# the length of the fence (i.e. the number of wooden boards) and a list
# of characters c (i.e. the list of possible colors). The functions should
# return a list of strings where each string represents one possible
# coloring of the fence. The elements of the list may be in ANY order.
#
# Examples:
#
#     >>> all_colorings(4, ['W', 'R', 'B'])
#     ['WWWW', 'WWWR', 'WWWB', 'WWRW', 'WWRR', 'WWRB', 'WWBW', 'WWBR', 
#      'WWBB', 'WRWW', 'WRWR', 'WRWB', 'WRRW', 'WRRR', 'WRRB', 'WRBW', 
#                 <<< 49 elements were omitted >>>
#      'BRWB', 'BRRW', 'BRRR', 'BRRB', 'BRBW', 'BRBR', 'BRBB', 'BBWW', 
#      'BBWR', 'BBWB', 'BBRW', 'BBRR', 'BBRB', 'BBBW', 'BBBR', 'BBBB']
#     >>> len(all_colorings(4, ['W', 'R', 'B']))
#     81
#     >>> all_colorings(3, ['W', 'R'])
#     ['WWW', 'WWR', 'WRW', 'WRR', 'RWW', 'RWR', 'RRW', 'RRR']
#
# Hint: Can you use recursion?
##########################################################################
def all_colorings(n , c):
    if n == 0: 
        return ['']
    l = []
    l_rest = all_colorings(n-1, c)
    for color in c: 
        for rest in l_rest:
            l.append(color + rest)
    return l 




##########################################################################
# Write a function proper_colorings(n, c) which is similar to the previous
# one, except that no two consecutive boards are allowed to have the same
# color. For example, 'WRBW' is a proper coloring; 'BRRW' is NOT allowed
# (the 2nd and the 3rd board are both of color 'R'). The elements of the
# list may be in ANY order.
#
# Examples:
#
#     >>> proper_colorings(4, ['W', 'R', 'B'])
#     ['WRWR', 'WRWB', 'WRBW', 'WRBR', 'WBWR', 'WBWB', 'WBRW', 'WBRB', 
#      'RWRW', 'RWRB', 'RWBW', 'RWBR', 'RBWR', 'RBWB', 'RBRW', 'RBRB', 
#      'BWRW', 'BWRB', 'BWBW', 'BWBR', 'BRWR', 'BRWB', 'BRBW', 'BRBR']
#     >>> len(proper_colorings(4, ['W', 'R', 'B']))
#     24
#     >>> proper_colorings(3, ['W', 'R'])
#     ['WRW', 'RWR']
##########################################################################
def is_valid(s): 
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

def proper_colorings(n,c):
    l = []
    for coloring in all_colorings(n,c):
        if is_valid(coloring): 
            l.append(coloring)
    return l 


##########################################################################
# It turns out that we often do not have unlimited amount of paint.
# Suppose that we have enough paint to color 2 boards with color 'W',
# 3 boards with color 'R' and 1 board with color 'B'. We can give this
# information as a list of pairs:
#
#     [('W', 2), ('R', 3), ('B', 1)]
#
# Write a function proper_limited(n, c) that takes two arguments: n is
# the length of the fence and c is a list of pairs (as described above).
# The function should return a list of all proper colorings where you
# also have to take into account that you only have a limited amound of
# paint. The elements of the list may be in ANY order.
#
# Example:
#     >>> proper_limited(5, [('W', 2), ('R', 3), ('B', 1)])
#     ['RWBRW', 'WRBRW', 'RBWRW', 'BRWRW', 'RWRBW', 'WRBWR', 'RWBWR',
#      'WBRWR', 'RBRWR', 'BWRWR', 'RWRWR', 'WRWBR', 'RWRBR', 'RWRWB',
#      'WRWRB']
##########################################################################
def is_limited(s, c): 
    count= {}
    for x in s:
        if not x in count:
            count[x] = 1
        else:
            count[x] = count[x] + 1
    for color, limit in c: 
        if count.get(color, 0) > limit: 
            return False
    return True 

def proper_limited(n, c):
    c2 = [p[0] for p in c]
    colorings = proper_colorings(n,c2) 
    l = [] 
    for coloring in colorings:
        if is_limited(coloring, c): 
            l.append(coloring)
    return l































