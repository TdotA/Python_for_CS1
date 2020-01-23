##########################################################################
# Love is the Ruin of Us All 
#
# The social network of infatuation can be represented by a dictionary
# which maps a person's name to a set of people who are infatuated by
# that person (one person can have a crush on many other people). For
# instance, the dictionary
# 
#     s = {'Ana': {'Bine', 'Cene'},
#          'Bine': set(),
#          'Cene': {'Bine'},
#          'Davorka': {'Davorka'},
#          'Eva': {'Bine'}}
# 
# tells us that Ana has a crush on Bine and Cene. Bine is not infatuated
# with anyone. Cene loves Bine, Davorka only loves herself, and Eva loves
# Bine.
##########################################################################



##########################################################################
# Write a function narcissists(d) that takes a dictionary of infatuation
# and returns the _set_ of people who love themselves. Example (`s` is
# the above dictionary):
# 
#     >>> narcissists(s)
#     {'Davorka'}
##########################################################################



##########################################################################
# Write a function loved_ones(d) that takes a dictionary of infatuation
# and returns the _set_ of those people who are loved by at least one 
# person. Example (`s` is the above dictionary):
# 
#     >>> loved_ones(s)
#     {'Bine', 'Davorka', 'Cene'}
##########################################################################



##########################################################################
# Write a function couples(d) that takes a dictionary of infatuation
# and returns the _set_ of couples who could be happily in love. Each couple
# should occur only once in the set. The two names should be ordered
# lexicographically. For instance, if Bine and Ana are happily in love
# then the pair `('Ana', 'Bine')` should be included. Example (`s` is the
# above dictionary):
# 
#     >>> couples(s)
#     {('Ana', 'Cene')}
##########################################################################



##########################################################################
# Write a function compliant_people(name, d) that takes a person's name
# and a dictionary of infatuation and returns the _set_ of people that are
# overly compliant to that person. They are overly compliant because they
# have a crush on that person or they have a crush on a person who is
# compliant to that person.
#  
# For example, if the dictionary is
# 
#     s2 = {'Ana': {'Bine', 'Cene'},
#           'Bine': {'Ana'},
#           'Cene': {'Bine'},
#           'Davorka': {'Davorka'},
#           'Eva': {'Bine'}}
# 
# then Ana is compliant to Cene because she has a crush on him. Bine is
# also compliant to Cene because he has a crush on Ana. Moreover, Eva is
# compliant to Cene because she has a crush on Bine. Cene is compliant to
# himself because he has a crush on Bine. Example:
# 
#     >>> compliant_people('Cene', s2)
#     {'Ana', 'Bine', 'Cene', 'Eva'}
##########################################################################


