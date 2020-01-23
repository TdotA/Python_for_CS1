# Project Sudoku

def load_sudoku(file_name):
    m = []
    with open(file_name) as f:
        for i in range(9):
            line = list(f.readline().strip())
            for j in range(len(line)):
                if line[j] == '.':
                    line[j] = 0
                else:
                    line[j] = int(line[j])
            m.append(line)
    return m

def draw_sudoku(m):
    for i in range(9):
        if i % 3 == 0:
            print('+---+---+---+')
        line = ''
        for j in range(9):
            if j % 3 == 0:
                line += '|'
            line += ' ' if m[i][j] == 0 else str(m[i][j])
        print(line + '|')
    print('+---+---+---+')

def update_forbidden(fm, row, col, entry):
    for j in range(9): 
        fm[row][j].add(entry)
    for i in range(9):
        fm[i][col].add(entry)
    ii = row // 3
    jj = col // 3
    for k in range(3):
        for l in range(3):
            fm[ii*3 + k][jj*3 + l].add(entry)

    

def forbidden_matrix(m):
    f = [[set() for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9): 
            if m[i][j] == 0:
                continue
            else: 
                update_forbidden(f, i, j, m[i][j])
    return f

def solve(m):
    ALL_DIGITS = {1,2,3,4,5,6,7,8,9}
    f = forbidden_matrix(m)
    ii, jj, size = None, None, -1
    for i in range(9):
        for j in range(9): 
            if m[i][j] != 0:
                continue
            if len(f[i][j]) > size:
                size = len(f[i][j])
                ii = i 
                jj = j 
    if ii is None: 
        return m 
    for d in ALL_DIGITS - f[ii][jj]:
        m2 = [l[:] for l in m]
        m2[ii][jj] = d 
        solution = solve(m2)
        if not solution is None : 
            return solution
        return None




    
    pass

s = load_sudoku('easy01.txt')
draw_sudoku(solve(s))
