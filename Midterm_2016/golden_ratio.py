##########################################################################
# Golden Ratio
#
# We say that numbers $a$ and $b$ are in the golden ratio if
# $a / b = (a + b) / a$, which is equivalent to saying that  $a / b$
# equals the number $\phi = (1 + \sqrt{5}) / 2$.
# 
# The approximation of the number $\phi$ can be calculated by using
# the sequence $\phi_0, \phi_1, \phi_2, \dots$, where $\phi_0 = 1$ and
# $\phi_{n + 1} = 1 + (1 / \phi_n)$.
##########################################################################



##########################################################################
# Write a function next_approx(x) that from a given number x returns
# the next approximation of $\phi$.
#
# Examples:
#
#     >>> next_approx(2)
#     1.5
#
#     >>> next_approx(1.5)
#     1.6666666666666667
##########################################################################



##########################################################################
# Write a function approx(k) that determines the k-th approximation of the
# number $\phi$. For the initial approximation (i.e., $k = 0$) take the
# value $1$.
#
# Example:
#
#     >>> approx(5)
#     1.625
##########################################################################



##########################################################################
# Write a function good_approx(eps) that returns the first approximation
# which from the previous one differs by less than eps.
#
# Example:
#
#     >>> good_approx(0.001)
#     1.6181818181818182
##########################################################################



##########################################################################
# Write a function close_approx(eps) that returns the smallest k for which
# $phi_k$ differs from $(1 + \sqrt{5}) / 2$ by less than eps.
# 
# Example:
#
#     >>> close_approx(0.0001)
#     10
##########################################################################


