##########################################################################
# If you read The Adventures of Asterix comic book then you know that
# a Gaulish name ends in 'ix'. Write a function is_gaul(name) that takes
# a name and returns True if and only if the name is Gaulish.
#
# Example:
#
#     >>> is_gaul('Obelix')
#     True
#     >>> is_gaul('Zlatko')
#     False
##########################################################################



##########################################################################
# A snail travels $a$ centimeters to the east, $b$ centimeters to the south,
# $c$ centimeters to the west and $d$ centimeters to the north. Because he
# is a slobbery animal, he leaves a trail behind him. Write a function
# contains_rectangle(a, b, c, d) that takes numbers a, b, c and d and returns
# True if and only if the trail contains a square.
#
# Example:
# 
#     >>> contains_rectangle(5.5, 4, 6.11, 7.1)
#     False
#     >>> contains_rectangle(6.9, 4.15, 5.3, 12.9)
#     True
##########################################################################



##########################################################################
# Write a function contact_card(name) that takes a string name and prints
# the framed name to the screen. The frame is composed of characters '*'
# as shown in the example below.
#
# Example:
#
#     >>> contact_card('Janez Vajkard Valvasor')
#     **************************
#     *                        *
#     * Janez Vajkard Valvasor *
#     *                        *
#     **************************
##########################################################################



##########################################################################
# Write a function fahrenheit_to_celsius(temperature) that takes as an
# argument the floating-point number temperature which represents the
# temperature in degrees Fahrenheit. The function should return the
# temperature in degrees Celsius.
#
# Example:
#
#     >>> fahrenheit_to_celsius(77.5)
#     25.27777777777778
##########################################################################



##########################################################################
# Write a function sine_table(step) which takes a number step and prints
# a table of sine as shown below. The function sine has to be evaluated
# at those values 0, step, 2*step, … which are less than 360. The angle is
# given in angular degrees.
#
# Example:
#
#     >>> sine_table(30)
#     sin(  0) = 0.0
#     sin( 30) = 0.4782539786213182
#     sin( 60) = 0.8400259231507714
#     sin( 90) = 0.9972037971811801
#     sin(120) = 0.9115058523116732
#     sin(150) = 0.6038044103254774
#     sin(180) = 0.14904226617617428
#     sin(210) = -0.34202014332566866
#     sin(240) = -0.749781202967734
#     sin(270) = -0.9749279121818236
#     sin(300) = -0.962624246950012
#     sin(330) = -0.7158668492597189
##########################################################################



##########################################################################
# Write a function sums(n) that takes an integer and prints a table with
# the sums 1 + 2 + ⋯ + i, 1² + 2² + ⋯ + i² and 1³ + 2³ + ⋯ + i³ for all
# i from 1 to n as shown in the example below.
# 
# Example:
# 
#     >>> sums(5)
#     1 1 1
#     3 5 9
#     6 14 36
#     10 30 100
#     15 55 225
##########################################################################



##########################################################################
# Write a function find_numbers() that prints all those 4-digit numbers 
# for which the difference of the first two digits equals the sum of the
# last two. For example, one of those numbers is 7313, because
# 7 - 3 = 1 + 3 = 4.
##########################################################################



##########################################################################
# We have a bicycle combination lock with four rotating discs. Each disc
# contains digits 0, 1, 2, …, 9 in that order. Digits 0 and 9 are also
# adjacent. For an example see figure (our lock has 4 discs, not only 3):
# https://en.wikipedia.org/wiki/Combination_lock#/media/File:Combination_unlocked.png.
#
# Whenever we rotate one of the discs to either of its two adjacent numbers
# it produces the "Click!" sound. Write a function combination_lock(a, b)
# that takes two 4-digit integers a and b and returns the minimum number of
# "Click!" sounds we hear when we move from combination a to b.
#
# Example:
#
#     >>> combination_lock(2222, 3131)
#     4
##########################################################################



##########################################################################
# Television screens are usually measured diagonally because this is the
# way screens were originally measured. From the length of the diagonal
# and the ratio between the two sides we want to compute its side lengths.
# Write a function screen_size(diag, w, h) that takes three numbers:
# diag is the length of the diagonal; w and h give the ratio between the
# width and the height of the screen. The function should return two
# numbers: the width and the height of the screen.
#
# Example:
#
#     >>> screen_size(52.0, 16, 9)
#     (45.0, 25.0)
###########################################################################


