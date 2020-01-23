##########################################################################
# Write a function emphasise(title) that takes a string title and returns
# a new string where the title is emphasised, i.e., all letters are in
# uppercase and separated by spaces. Spaces in the string title should be
# treated in the same way as other characters (they become triple spaces).
# 
# Example:
#
#     >>> emphasise('Breaking news')
#     'B R E A K I N G   N E W S'
##########################################################################



##########################################################################
# Write a function emphasise_marked(title) which returns a new string
# in which only letters that are between characters * in the original title
# are converted to uppercase. Characters * should be removed from the
# resulting string.
#
# Example:
#
#     >>> emphasise_marked('Breaking *news* on Donald *Trump*')
#     'Breaking NEWS on Donald TRUMP'
##########################################################################



##########################################################################
# Write a function is_palindrome(s) that returns True if the string s is a
# palindrome and False if it is not.
#
# Example:
#
#     >>> is_palindrome('neradodaren')
#     True
#     >>> is_palindrome('math')
#     False
##########################################################################



##########################################################################
# We say that a string is almost a palindrome if we have to erase exactly
# one character from it to obtain a palindrome. The word kolo is almost a
# palindrome, because we only need to erase the letter k to obtain olo.
#
# Write a function almost_palindrome(s) that returns True if the string s
# is almost a palindrome.
#
# Example:
#
#     >>> almost_palindrome('kolo')
#     True
#     >>> almost_palindrome('famnit')
#     False
##########################################################################



##########################################################################
# We say that a string is a pseudo-palindrome if we need to add or erase
# exactly one letter or replace it with another one in order to obtain a
# palindrome. Examples:
#
# * robot (replace t with r)
# * jana (add letter j at the end)
#
# Write a function pseudo_palindrome(s) that returns true if and only if the
# string s is a pseudo-palindrome.
#
# Example:
#
#     >>> pseudo_palindrome('robot')
#     True
#     >>> pseudo_palindrome('famnit')
##########################################################################


