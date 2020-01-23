##########################################################################
# Dragan is a moderator of a less known forum which has a large number of
# registered users. Most of them post stupid content. If Dragan considers
# a post to be offensive, he immediately deletes it. If its not offensive
# but only extremely stupid, he does the following: He removes all vowels
# from the text and puts them (in the same relative order) at the end. For
# example, the message:
#
# Banana is the best. It is especially good in combination with Nutella.
#
# becomes
#
# Bnn s th bst. t s spclly gd n cmbntn wth Ntll.aaaieeIieeiaooioiaioiuea
#
# This way the text becomes hard to read and most users just ignore it. But
# if someone really wants to read the post, he can decode it with some effort.
#
# (The described transformation of text is called disemvoweling.)
##########################################################################



##########################################################################
# Write a function first_vowel(s) that takes a string s and returns the
# index of the first vowel in the string s. If there is no vowel in the
# string then the function should return -1.
#
# Example:
#
#     >>> first_vowel('Krščen matiček!')
#     4
##########################################################################



##########################################################################
# Write a function disemvowel(text) that takes a string text. The function
# should return a new string which is obtained by the disemvoweling (as
# described above).
#
# Example:
#
#     >>> disemvowel('Banana is good!')
#     'Bnn s gd!aaaioo'
##########################################################################



##########################################################################
# Sometimes we would like to decipher the text because we are interested
# in the content. This task is not easy, because we do not know where do
# the vowel actually belong. The string 'Bnn s gd!aaaioo' could be deciphered
# as 'Bnana sa igood!', as 'Baanani so god!' etc.
#
# Dragan entered characters '*' at positions where he thinks that the vowels
# should be. A star will not have any other role in the text. Also, the number
# of vowel will equal the number of stars and all vowels will be at the end.
#
# Write a function undo_disemvowel(s) which replaces the stars with vowels
# that are written at the end.
#
# Example:
#
#     >>> undo_disemvowel('B*n*n* *s g**d!aaaioo')
#     'Banana is good!'
##########################################################################


