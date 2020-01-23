##########################################################################
# Basketball
#
# Everybody likes to watch NBA games, especially if players like Goran
# Dragić or Luka Dončić are playing. NBA games take place at night which
# can be a problem if you have to go to work early in the morning.
# However, this is not a problem that we will be able to solve.
##########################################################################



##########################################################################
# Write a function read_data(file_name) which takes a string file_name
# and reads the data from the file with that name. The file contains
# several lines each of which contains two numbers. The first number is
# the number on the player's shirt and the second number is either 1, 2,
# or 3 (the points scored by that player). The file could contain for
# example:
#
#     77 3
#     77 2
#     41 2
#     77 3
#     41 1
#     41 1
#     7 2
#     77 2
#     7 2
#
# The function should return a list of pairs (see example below).
#
# Example (supposed that the data is stored in a file named 'nba.txt'):
#
#     >>> read_data('nba.txt') 
#     [(77, 3), (77, 2), (41, 2), (77, 3), (41, 1), (41, 1), (7, 2),
#      (77, 2), (7, 2)]
##########################################################################
def read_data(file_name):
    f = open(file_name, 'r')
    l = f.readlines()
    s = [] 
    for line in l:
        line.strip()
        l1= line.split(' ')
        a, b = int(l1[0]), int(l1[1])
        s.append((a,b))
    return s
#print(read_data('nba.txt'))


##########################################################################
# Write a function make_dictionary(data) which takes a list of pairs
# as returned by the above function and return a dictionary where keys
# are player's shirt numbers and values are triples (one, two, three),
# where one is the number of scored 1-point throws, two is the number of
# scored 2-point throws, and three is the number of scored 3-point throws.
#
# Example:
#
#     >>> make_dictionary(read_data('nba.txt'))
#     {77: (0, 2, 2), 41: (2, 1, 0), 7: (0, 2, 0)}
##########################################################################
def make_dictionary(data):
    dir = {}
    for i in data:
        if not i[0] in dir:
            dir.get(i[0])
            if i[1] == 1:
                dir[i[0]] = [1,0,0]
            if i[1] == 2:
                dir[i[0]] = [0,1,0]
            if i[1] == 3:
                dir[i[0]] = [0,0,1]
        else: 
            if i[1] == 1:
                dir[i[0]][0] += 1
            if i[1] == 2:
                dir[i[0]][1] += 1
            if i[1] == 3:
                dir[i[0]][2] += 1
    for x in dir:
        dir[x] = tuple(dir[x])
    return dir
#print(make_dictionary(read_data('nba.txt')))


##########################################################################
# Write a function called total_points_scored(d) which takes a dictionary
# as returned by the function make_dictionary (see above) and creates
# and returns a new dictionary where: keys are the same as in d, and their
# corresponding values are the total points scored by that player.
#
# Example:
#
#     >>> total_points_scored({77: (0, 2, 2), 41: (2, 1, 0), 7: (0, 2, 0)})
#     {77: 10, 41: 4, 7: 4}
##########################################################################

def total_points_scored(d):
    dir ={} 
    for i in d:
        if not i in dir: 
            dir.get(i)
            dir[i] = d[i][0] + 2*d[i][1] + 3 * d[i][2]
    return dir
print(total_points_scored({77: (0, 2, 2), 41: (2, 1, 0), 7: (0, 2, 0)}))
##########################################################################
# Write a function called save_scored(d, names, file_name) which takes
# three arguments: the argument d is a dictinary (in the format returned
# by function make_dictonary); names is another dictionary where key
# are player's shirt numbers and their values are string that contain
# their names; file_name is a file that should be created by the function
# and will contain one line for each player. The line should contain the
# player's name and the number of points he scored. If the name of a player
# is missing in the dictionary names, then you should print '???'.
#
# Example:
#
#     >>> d = make_dictionary(read_data('nba.txt'))
#     >>> names = {41: 'Dirk Nowitzki', 77: 'Luka Dončić'}
#     >>> save_scored(d, names, 'results.txt')
#
# The file 'results.txt' should now contain the following three lines:
#
#     Luka Dončić 10
#     Dirk Nowitzki 4
#     ??? 4
#
# The players can be listed in ANY order.
##########################################################################


