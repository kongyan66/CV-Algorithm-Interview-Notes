# 题目：给定一个 row x col 的二维网格地图 grid， 整个网格被水完全包围，但其中恰好有一个岛屿。计算这个岛屿的周长。
# 思路：计算陆地的个数L(周长为4)与接壤的边数B 周长 = 4 * L - 2 * B

# 解法一：迭代法
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)  
        col = len(grid[0])
        land = 0   # 记录陆地个数
        boarder = 0 # 记录接壤的边数
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    land += 1 
                    # 容易疑问：为啥只算左边和下边的接壤边呢，每一个陆地都这么算，就能算齐且不用去重。
                    if i < row - 1 and grid[i+1][j] == 1:
                        boarder += 1
                    if j < col - 1 and grid[i][j+1] == 1:
                        boarder += 1
        return land * 4 - boarder * 2

# 解法二：锐化算法 
# 算周长说白了就是找边缘，找边缘说白了就是锐化，所以可以按照锐化的算法来算。
from scipy.signal import convolve2d
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return int(abs(convolve2d(grid,[[-2,1],[1,0]])).sum())

# 解法三：DFS
# 从陆地到海水或者从陆地到边界，则周长+1
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)  
        col = len(grid[0])
        land = 0   # 记录陆地个数
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return self.DFS(grid, i, j)
    
    def DFS(self, grid, i, j):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
            return 1
        # 如果访问过的节点就置2， 表明已经访问过
        if grid[i][j] == 2:
            return 0
        grid[i][j] = 2
        return self.DFS(grid, i+1, j) + self.DFS(grid, i-1, j) + self.DFS(grid, i, j+1) + self.DFS(grid, i, j-1)