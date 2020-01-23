##########################################################################
# RPN calculator 
#
# When we try to evaluate an arithemtic expressions using a calculator we
# have to take the parentheses in consideration. It turns out that we do
# not need to use parentheses at all if we use the reverse Polish notation
# (abbrev. RPN).
#
# See: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# In this notation operators are now written between the numbers but after
# them. Instead of '4 + 5' we write '4 5 +'. If we want to evaluate
# '(2 + 4) * 3', we write '2 4 + 3 *'. When we evaluate '2 4 +', we get 6
# as the result and the expression becomes '6 3 *'. The final result is 18.
# 
# In general, we put the numbers on a stack while the operator takes the
# top two numbers from the stack and replaces them with the result of the
# operation.
##########################################################################

operators = ['+', '*']


##########################################################################
# Write a function evaluate(a, b, op) that takes two strings a and b that
# represent two integers and an operator op that is either '+' or '*'
# (multiplication). The function should return a string which contains
# the result of the operation on arguments a and b.
#
# Example:
# 
#     >>> evaluate('10', '5', '+')
#     '15'
#     >>> evaluate('5', '3', '*')
#     '15'
##########################################################################



##########################################################################
# Write a function rpn(s) that takes a string that contains a valid
# RPN expression and returns the result.
# 
# Example:
#
#     >>> rpn('10 5 + 3 7 * +')
#     36
##########################################################################



##########################################################################
# Write a function standard_notation(s) that takes a string which contains
# an expression in the RPN notation. The function should return a string
# that contains the same expression in the standard notation. Use a pair of
# parentheses for each operator (even if they are unnecessary).
# 
# Example:
# 
#     >>> standard_notation('2 4 +')
#     '(2 + 4)'
#     >>> standard_notation('2 4 + 3 *')
#     '((2 + 4) * 3)'
#     >>> standard_notation('10 5 + 3 7 * +')
#     '((10 + 5) + (3 * 7))'
# 
# Hint: Can you solve this task with a minimal modification of the
# function rpn?
##########################################################################


