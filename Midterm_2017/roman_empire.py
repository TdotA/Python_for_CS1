##########################################################################
# Roman empire strikes back
#
# Functions that convert an integer to a Roman numeral and vice versa
# are already provided. You are encouraged to use them in your solutions
# to the tasks below.
##########################################################################

def to_roman(n):
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']
    o = n % 10
    t = (n // 10) % 10
    h = (n // 100) % 10
    m = (n // 1000) % 10
    return thousands[m] + hundreds[h] + tens[t] + ones[o]

all_numbers = {}
for i in range(1, 4000):
    s = to_roman(i)
    all_numbers[s] = i

def to_arabic(s):
    if s in all_numbers:
        return all_numbers[s]
    else:
        return None


##########################################################################
# Write a function letter_dict(n) that takes an integer n and returns
# a dictionary that contains as keys all letters that appear in the Roman
# numeral representation of n. Corresponding values should be frequencies
# of those letters. Example:
#
#     >>> letter_dict(2017)
#     {'M': 2, 'I': 2, 'X': 1, 'V': 1}
#
# Note: The Roman numeral representation of 2017 is 'MMXVII'.
##########################################################################



##########################################################################
# Write a function count_letters(a, b) that takes two integer a and b.
# You may assume that $a \leq b$. Suppose that you have written down
# on a piece of paper the Roman numeral representation of numbers
# $a, a+1, \ldots, b$. The function should return a dictionary of
# frequencies of letters of all numerals combined. Example:
#
#     >>> count_letters(10, 50)
#     {'I': 56, 'V': 20, 'X': 74, 'L': 11}
##########################################################################



##########################################################################
# Write a function letter_dict_rec(s, d) that gets a string s and a
# dictionary d as arguments. The function should increases the frequencies
# of those letters in the dictionary d that appear in the string s.
# It may also add keys to d if this is needed. Moreover, you are not
# allowed to use *for* or *while* loop in the solution. Example:
#
#     >>> d = {'banana': 7, 'X': 3}
#     >>> letter_dict_rec('MMXVII', d)
#     >>> d
#     {'M': 2, 'I': 2, 'X': 4, 'V': 1, 'banana': 7}
##########################################################################



##########################################################################
# Write a function count_letters_rec(a, b) that does the same thing as
# the function count_letters except that you are not allowed to use *for*
# or *while* loop in the solution. You may call the function letter_dict_rec
# and you may also define helper functions. Example:
#
#     >>> count_letters_rec(10, 50)
#     {'I': 56, 'V': 20, 'X': 74, 'L': 11}
##########################################################################



