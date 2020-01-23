##########################################################################
# Parentheses
##########################################################################



##########################################################################
# A parentheses expression is a string that contains only the characters
# '(' and ')'. The length or the expression is the length of the string.
#
# Write a function all_expressions(n) that takes the number n and returns
# a list of all parentheses expressions of length n.
#
# Example:
#
#     >>> all_expressions(5)
#     ['(((((', '(((()', '((()(', '((())', '(()((', '(()()', '(())(', '(()))',
#      '()(((', '()(()', '()()(', '()())', '())((', '())()', '()))(', '())))',
#      ')((((', ')((()', ')(()(', ')(())', ')()((', ')()()', ')())(', ')()))',
#      '))(((', '))(()', '))()(', '))())', ')))((', ')))()', '))))(', ')))))']
##########################################################################



##########################################################################
# Write a function is_validly_nested(s) that takes a string s and returns
# True if the string s represents a validy-nested parentheses expression.
# Otherwise, the function should return False.
#
# The empty string '' is a validly-nested parentheses expression. A string
# s is a validly-nested expression if removal of some substring '()' results
# in a validly-nested expression.
#
# Example:
#
#     >>> is_validly_nested('(())(()())()')
#     True
#     >>> is_validly_nested('(()))((())')
#     False
##########################################################################



##########################################################################
# Write a function valid_expressions(n) that takes a number n and returns
# a list of all validly-nested parentheses expressions of length n.
#
# Example:
#
#     >>> valid_expressions(6)
#     ['((()))', '(()())', '(())()', '()(())', '()()()']
#     >>> valid_expressions(5)
#     []
##########################################################################



##########################################################################
# A pair of ( and ) is of level 1 if it is NOT nested inside another
# pair of ( and ).
#
# A pair of ( and ) if of level k if k is the largest number such that
# this pair of parantheses is nested inside a pair of ( and ) of level
# k - 1.
#
# Write a function max_level(s) that takes a string s which represents a
# validly-nested parentheses expression. The function should return the
# largest level of ( and ) that can be found in this expression. 
#
# Example:
#
#     >>> max_level('()()()()()')
#     1
#     >>> max_level('(())(())()')
#     2
#     >>> max_level('(())((()))')
#     3
#     >>> max_level('')
#     0
##########################################################################



##########################################################################
# Write a function valid_level(n, k) that takes numbers n and k. The
# function should return a list of all validly-nested parentheses expressions
# of length n where the maximal level of some ( and ) is precisely k.
#
# Example:
#
#     >>> valid_level(6, 2)
#     ['(()())', '(())()', '()(())']
#     >>> valid_level(8, 3)
#     ['((()()))', '((())())', '((()))()', '(()(()))', '()((()))']
##########################################################################



