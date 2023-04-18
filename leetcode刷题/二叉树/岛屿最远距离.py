# 题目：求岛屿的数量及岛屿上任意两点的最长曼哈顿距离

# 思路：DFS求数量

class Solution:
    def __init__(self):
        self.island = set() # 保存所有岛屿路径
        self.path = ''   # 保存岛屿路径

    def findDifIsland(self, grid):
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += 1
                    self.DFS(grid, i, j)

    def DFS(self, grid, i, j):
        if not 0 <= i < len(grid) or 0 <= j < len(grid[0]) or grid[i][j] == 0:
            return 
        grid[i][j] = 0
        
        self.DFS(grid, i+1, j)
        self.DFS(grid, i-1, j)
        self.DFS(grid, i, j+1)
        self.DFS(grid, i, j-1)

if __name__ == "__main__":
    
