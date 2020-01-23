##########################################################################
# Abbreviations 
#
# We are given a phrase from which we want to form an abbreviation. An
# abbreviation can be obtain from taking the first few letters of each
# word in the phrase and concatenating them together. For example, from
# 'RAdio Detection And Ranging' we get 'RADAR'.
##########################################################################



##########################################################################
# Write a function abbrev(phrase, m, d) which gets a phrase (as a list of
# words) and integers m and d. The function should return a set of all
# abbreviations which are at least d characters long such that from each
# word we take between 0 and m letters.
#
# Example:
# 
#     >>> abbrev(['Large', 'Hadron', 'Collider'], 2, 3)
#     {'LaH', 'LHa', 'LHaC', 'HaC', 'LHaCo', 'LaC', 'LaHa', 'LaHCo', 'LaHC',
#      'HaCo', 'LaHaCo', 'LCo', 'LHC', 'LaHaC', 'LaCo', 'HCo', 'LHCo'}
#     >>> abbrev(['Large', 'Hadron', 'Collider'], 2, 4)
#     {'LHaC', 'LHaCo', 'LaHa', 'LaHCo', 'LaHC', 'HaCo', 'LaHaCo', 'LaHaC',
#      'LaCo', 'LHCo'}
##########################################################################

def all_abbrev(phrase, m):
    if len(phrase) == 0: 
        return ['']
    l = []
    for rest in all_abbrev(phrase[1:], m):
        for i in range(m +1): 
            l.append(phrase[0][:i] + rest)
    return l       


def abbrev(phrase, m ,d): 
    l = []
    f = all_abbrev(phrase, m)
    for i in f: 
        if len(i) >= d: 
            l.append(i) 
        else: 
            continue
    return set(l) 

#print(abbrev(['Large', 'Hadron', 'Collider'], 2, 3))

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        

           
