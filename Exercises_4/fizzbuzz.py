##########################################################################
# FizzBuzz 
#
# FizzBuzz is a popular game among children. Children pronounce numbers
# 1, 2, 3, ... If the number is divisible by 3 then they should say ‘Fizz!’
# instead of the number. If it is divisible by 5 then they should say
# ‘Buzz!’. If it is divisible by 3 and 5 then they should say ‘Fizz buzz!’.
##########################################################################



##########################################################################
# Write a function fizzbuzz(n) that takes a natural number n as the
# argument. The function should return a list of numbers from 1 to n, where:
# 
# * the multiples of 3 are replaced with string 'Fizz',
# * the multiples of 5 are replaced with string 'Buzz',
# * the multiples of 15 are replaced with string 'FizzBuzz'.
# 
# Example:
# 
#     >>> fizzbuzz(15)
#     [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz',
#      13, 14, 'FizzBuzz']
##########################################################################



##########################################################################
# Write a function store_fizzbuzz(file_name, n) where the arguments are
# a string file_name which contains the name of a file and a natural
# number n. The function should store the elements of the list returned by
# fizzbuzz(n) to the file named file_name. Each element should be in its
# own line.
# 
# Example: After the call store_fizzbuzz('fizzbuzz.txt', 5) the file
# fizzbuzz.txt should contain:
# 
#     1
#     2
#     Fizz
#     4
#     Buzz
##########################################################################



##########################################################################
# Write a function detect_errors(l) that takes a list l as the argument.
# This list is a FizzBuzz sequence, but it may contain errors.
# The function should return a list with those indices of the list l where
# errors occured. The elements of this list should be sorted.
#
# Example:
# 
#     >>> detect_errors([1, 2, 3, 'Fizz', 'Buzz', 7, 'Fizz', 8])
#     [2, 3, 5, 6]
##########################################################################



##########################################################################
# Write a function buzzfizz(n) which should return the same result as the
# fizzbuzz function. The function buzzfizz should be defined recursively.
# 
# In this task you should not use for or while loop. Also, you are not
# allowed to call the fizzbuzz function :-)
#
# Example:
#
#     >>> buzzfizz(15)
#     [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz',
#      13, 14, 'FizzBuzz']
##########################################################################

def buzzfizz(n): 
    
    if n == 0:
        return []
    if n % 3 == 0 and n % 5 == 0:
        lis = buzzfizz(n-1)
        lis.append('FizzBuzz')
        return lis
    elif n % 3 == 0:
        lis = buzzfizz(n-1)
        lis.append('Fizz')
        return lis
    elif n % 5 == 0:
        lis = buzzfizz(n-1)
        lis.append('Buzz')
        return lis
    else:
        lis = buzzfizz(n-1)
        lis.append(n)
        return lis

    
print(buzzfizz(13))
