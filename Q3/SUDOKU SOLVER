grid = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

def is_valid(r,c,n):
    for i in range(9):
        if grid[r][i]==n or grid[i][c]==n:
            return False
    
    sr, sc = (r//3)*3, (c//3)*3
    for i in range(3):
        for j in range(3):
            if grid[sr+i][sc+j]==n:
                return False
    return True

def solve():
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                for n in range(1,10):
                    if is_valid(i,j,n):
                        grid[i][j]=n
                        if solve():
                            return True
                        grid[i][j]=0
                return False
    return True

solve()

print("\nSudoku Solution:\n")
for row in grid:
    print(row)
