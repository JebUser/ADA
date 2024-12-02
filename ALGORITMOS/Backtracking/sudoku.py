
"""
Implementación Solución Sudoku con Reintento
"""
def conflict(T, r, c, v):
    ans, i, T[r][c] = False, 0, 0
    while ans == False and i != 9:
        ans, i = T[r][i] == v or T[i][c] == v, i + 1
    i, rr, cc = 0, (r // 3) * 3, (c // 3) * 3
    while ans == False and i != 3:
        j = 0
        while ans == False and j != 3:
            ans, j = T[rr+i][cc+j] == v, j + 1
        i += 1
    #T[r][c] = v
    return ans

def solve(T, r, c):
    ans = None
    if r == 9: 
        ans = True
    else:
        if c == 8: 
            ans = solve(T, r + 1, 0)
        else:
            if T[r][c] != 0:
                if conflict(T, r, c, T[r][c]) == False:
                    ans = solve(T, r, c + 1)
                else: ans = False
            else:
                ans, v = False, 1
                while ans == False and v != 10:
                    if conflict(T, r, c, v) == False:
                        T[r][c] = v
                        ans = solve(T, r, c + 1)
                    v += 1
                if ans == False: T[r][c] = 0
    return ans


Tab1 = [[9, 5, 0, 0, 0, 1, 0, 0, 7],
        [0, 8, 0, 0, 0, 2, 0, 0, 4],
        [0, 0, 0, 0, 7, 5, 2, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 8, 6, 3, 0],
        [1, 9, 0, 4, 0, 7, 0, 0, 0],
        [6, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 4, 0]]

if solve(Tab1, 0, 0):
    for i in range(9):
        print(Tab1[i])
else:
    print("No solution")