##########################################################################
# Calories 
#
# Tina keeps a diary of calories she consumed. After each meal she writes
# down its calorie content (an integer). She keeps this data in a file.
# For each day there is one line in the file. Within each line the values
# are seperated with commas. Example:
# 
#     550,745,625,200
#     850,1250
#     40,650,743
##########################################################################



##########################################################################
# Write a function determine_calories(s) that takes a string that contains
# a list of calories. This string contains integers that are seperated with
# commas. The function should return a list with corresponding integer
# values extracted from the string. Example:
# 
#     >>> determine_calories('10,4,7')
#     [10, 4, 7]
##########################################################################
def determine_calories(s):
    l = s.split(',')
    for i in range(len(l)):
        l[i] = int(l[i])
    return l 
#print(determine_calories('10,4,7'))


##########################################################################
# Write a function calories_per_day(file_name) that takes a file name.
# This input file is formatted as described above. The function should
# determine Tina's calorie content for each day. The function should return
# a list of integer values. Example (assume that the example above is
# stored in a file named tina_calories.txt):
# 
#     >>> calories_per_day('tina_calories.txt')
#     [2120, 2100, 1433]
# 
# For each line in the input file (that represents one day) add one integer
# value to the list. This integer values should be the sum of calories for
# that day.
##########################################################################
def calories_per_day(file_name):
    lis = []
    f = open(file_name, 'r')
    for line in f:
        l = determine_calories(line)
        lis.append(sum(l))
    f.close()
    return lis
print(calories_per_day('calories.txt'))

##########################################################################
# Write a function calorie_sum(input_file_name, output_file_name) that
# takes names of two files. The input file is Tina's diary. For each line
# in the input file the function has to print the sum of consumed calories
# for that day to the output file. Each number in the output file has to
# be printed in a single line.
# 
# After the function call `calorie_sum('tina_calories.txt', 'tina_sums.txt')`
# assuming the content of file tina_calories.txt is the same as above, the
# file tina_sums.txt contain the following lines:
# 
#     2120
#     2100
#     1433
##########################################################################



##########################################################################
# Write a function calorie_average(input_file_name, output_file_name)
# that takes names of two files as arguments. The function should print
# one line to the output file for each line in the input file. That line
# should contain its sequential number (starting with 1) and the average
# calorie value of a meal consumed by Tina on that day. The average must
# be rounded off to two decimal places.
# 
# The last (additional) line should contain the average daily intake
# (also rounded off to two decimal places). 
# 
# After the call `calorie_average('tina_calories.txt', 'tina_averages.txt')`
# with the above data the file tina_averages.txt contains:
# 
#     1 530.00
#     2 1050.00
#     3 477.67
#     1884.33
##########################################################################


