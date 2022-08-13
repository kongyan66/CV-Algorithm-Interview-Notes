
map = {'W':[-1, 0], 'A':[0, -1], 'S':[1, 0], 'D':[0, 1]}

def move(steps, grid):
    i, j = 0, 0
    for step in steps:
        dir = map[step]
        grid[i + dir[0]][j + dir[i]] = 0    

def check(grid):
    row = len(grid)
    col = len(grid[0])
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                count += 1
    if count == 0:
        return True
    else:
        

if __name__ == '__main__':
    n, m, k = int(input().split(' '))
    steps = input()
    grid = [[1] * m for _ in range(n)]
    grid[0][0] = 0
    move(steps)
    check(grid)



    







 


