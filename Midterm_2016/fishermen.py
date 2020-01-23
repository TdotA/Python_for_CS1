##########################################################################
# Fishermen
#
# To catch a fish you need appropriate bait. We are given a dictionary
# where keys are different types of baits and the values are sets of
# fish which eat the given bait. Moreover, we have a dictionary where
# keys are names of fishermen and their corresponding values are baits
# that are carried by the fishermen.
#
# Here are examples of such dictionaries:
##########################################################################

baits_example = {
    'fruit fly': {'carp', 'catfish'}, 'caterpillar': {'trout', 'pike'},
    'mosquito': {'common nase', 'catfish'}, 'worm': {'carp'}
}

fishermen_example = {
    'Franci': {'fruit fly', 'caterpillar'}, 'Alenka': {'mosquito'},
    'Anja': {'fruit fly'}, 'Borut': {'fruit fly', 'worm'}
}


##########################################################################
# Write a function fish_dictionary(baits) that gets a dictionary of baits
# (as described above). The function should return a new dictionary where
# keys are fish and the corresponding values are baits which are eaten by
# the fish.
#
# Example:
# 
#     >>> fish_dictionary(baits_example)
#     {'trout': {'caterpillar'}, 'catfish': {'fruit fly', 'mosquito'},
#      'carp': {'fruit fly', 'worm'}, 'pike': {'caterpillar'},
#      'common nase': {'mosquito'}}
##########################################################################



##########################################################################
# Write a function elusive_fish(fish, fishermen) that takes a dictionary
# of fish and a dictionary of fishermen. The function should return the
# set of those fish which the fishermen are not able to catch.
#
# Example:
# 
#     >>> elusive_fish({'trout': {'green fly'}, 'carp': {'caterpillar', 'fruit fly'}},
#                      {'Franci': {'fruit fly', 'caterpillar'}, 'Borut': {'fruit fly'}})
#     {'trout'}
##########################################################################



##########################################################################
# Naive fish is a fish which will eat every bait. Write a function
# naive_fish(baits) that gets a dictionary of baits and returns the set
# of naive fish.
#
# Example:
# 
#     >>> naive_fish({'fruit fly': {'carp', 'catfish'}, 'caterpillar': {'trout', 'carp'}})
#     {'carp'}
##########################################################################



##########################################################################
# The Fisheries Society organizes a fishing weekend. They only have one
# van and there are (as usual) too many candidates. Therefore, they may
# not let some of the fishermen in the van. They have the following rule:
# A new person who arrives at the meeting point will be accepted if he
# carries some new kind of bait.
# 
# Write a function fishing_weekend(fishermen, order) which takes a
# dictionary of fishermen and a list which describes the order of arrivals
# of the fishermen. The function should return a set of fishermen who will
# be accepted.
#
# Examples:
# 
#     >>> fishing_weekend({'Franci': {'fruit fly', 'caterpillar'}, 'Borut': {'fruit fly'}}, ['Franci', 'Borut'])
#     {'Franci'}
#
#     >>> fishing_weekend({'Franci': {'fruit fly', 'caterpillar'}, 'Borut': {'fruit fly'}}, ['Borut', 'Franci'])
#     {'Franci', 'Borut'}
#
#     >>> fishing_weekend({'Andreja': set(), 'Franci': {'fruit fly', 'caterpillar'}, 'Alenka': {'mosquito'},
#                          'Anja': {'fruit fly'}, 'Borut': {'fruit fly', 'worm'}},
#                         ['Franci', 'Anja', 'Alenka', 'Andreja', 'Borut'])
#     {'Borut', 'Franci', 'Alenka'}
##########################################################################


