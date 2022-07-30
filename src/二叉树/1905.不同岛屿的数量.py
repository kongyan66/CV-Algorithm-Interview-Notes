# 题目：统计不同形状岛屿的数量
# 思路：DFS的路径可以反映一个岛屿的形状，记录下来，再去重就是不同岛屿的数量


# 解法：DFS
class Solution:
    def __init__(self):
        self.island = set() # 保存所有岛屿路径
        self.path = ''   # 保存岛屿路径

    def findDifIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.path = ''
                    self.DFS(grid, i, j, 66)
                    self.island.add(self.path)
        return len(self.island)

    def DFS(self, grid, i, j, dir):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
            return 
        # 前序遍历位置：进入 (i, j)
        grid[i][j] = 0
        self.path += str(dir) + ','

        self.DFS(grid, i+1, j, 1)
        self.DFS(grid, i-1, j, 2)
        self.DFS(grid, i, j+1, 3)
        self.DFS(grid, i, j-1, 4)
        # 后序遍历位置：离开 (i, j) 这个就体现了递归的内部回溯过程
        self.path += str(-dir) + ','


if __name__ == '__main__':
    grid = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,1,1]]
    solution = Solution()
    res = solution.findDifIsland(grid)
    print(res)
   
 