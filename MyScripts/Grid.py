def matrix_fcn(n,m): #utility function; returns a n*m zero matrix
    matrix=[]
    for i in range (n):
        line = []
        matrix.append(line)
        for j in range (m):
            line.append('#')
    return matrix

def load_grid(file_name):
    f = open(file_name,"r")
    data = f.readlines()
    column = ""
    grid = []
    dims = data[0].split(" ")
    n = int(dims[1])
    m = int(dims[0])
    k = int(dims[2])
    for i in range(n):
        column += "."
    for x in range(m):
        grid.append(column)
    grid[0] = grid[0].replace(".","#")
    grid[m-1] = grid[m-1].replace(".","#")
    for i in range(1,m-1):
        grid[i] = grid[i].replace(".","#",1)
        grid[i] = grid[i][::-1]
        grid[i] = grid[i].replace(".","#",1)
    for i in range(1,k+1):
        nums = data[i].split(" ")
        x = int(nums[0])
        y = int(nums[1])
        list_x = list(grid[x])
        list_x[y-1] = "#"
        grid[x] = ''.join(list_x)

            
    f.close()
    return grid

#print(load_grid('grid.txt'))

def final_ant(grid, p, s):
    for element in grid:
        grid[grid.index(element)] = list(element)
    p1 = list(p)
    for c in s: 
        if c == 'L' and grid[p1[0]][p1[1]-1] != '#':
            p1[1] = p1[1] - 1
        elif c == 'L' and grid[p1[0]][p1[1]-1] == '#':
            pass
        elif c == 'U' and grid[p1[0]-1][p1[1]] != '#' :
            p1[0] = p1[0]+1
        elif c == 'U' and grid[p1[0]-1][p1[1]] == '#' :
            pass
        elif c == 'R' and grid[p1[0]][p1[1]+1] != '#' :
            p1[1]=p1[1]+1
        elif c == 'R' and grid[p1[0]][p1[1]+1] == '#' :
            pass
        elif c == 'D' and grid[p1[0]+1][p1[1]] != '#' :
            p1[0] = p1[0]+1
        elif c == 'D' and grid[p1[0]+1][p1[1]] == '#' :
            pass
    return p1[0],p1[1]
x = load_grid('grid.txt')
#print(final_ant(x, (3,3), 'LR'))

def initial_ant(grid, p, s):
    return None

def reduce_steps(grid, p, s):
    for element in grid:
        grid[grid.index(element)] = list(element)
    p1 = list(p)
    s1 = list(s)
    for c in s1: 
        if c == 'L' and grid[p1[0]][p1[1]-1] != '#':
            p1[1] = p1[1] - 1
        elif c == 'L' and grid[p1[0]][p1[1]-1] == '#':
            del s1[s1.index(c)]
        elif c == 'U' and grid[p1[0]-1][p1[1]] != '#' :
            p1[0] = p1[0]+1
        elif c == 'U' and grid[p1[0]-1][p1[1]] == '#' :
            del s1[s1.index(c)]
        elif c == 'R' and grid[p1[0]][p1[1]+1] != '#' :
            p1[1]=p1[1]+1
        elif c == 'R' and grid[p1[0]][p1[1]+1] == '#' :
            del s1[s1.index(c)]
        elif c == 'D' and grid[p1[0]+1][p1[1]] != '#' :
            p1[0] = p1[0]+1
        elif c == 'D' and grid[p1[0]+1][p1[1]] == '#' :
            del s1[s1.index(c)]
    return ''.join(s1)
x = load_grid('grid.txt')
print(reduce_steps(x,(3,3),'LLLLLLLLL'))
    