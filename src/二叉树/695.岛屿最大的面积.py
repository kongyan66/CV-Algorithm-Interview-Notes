# 题目：给你一个大小为 m x n 的二进制矩阵 grid表示的岛屿，0表示水，1表示陆地，找出最大的陆地面积。
# 思路：与200.数量区别是 在DFS/BFS的时需要返回岛屿的面积

# 解法一：DFS 递归实现 也可用栈实现
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, self.DFS(grid, i, j))
        return res
    # 1.确定入参与返回值
    # 返回值：当前岛屿的面积
    def DFS(self, grid, i, j):
        # 确定递归停止条件
        
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
            return 0
        # 3.确定单层递归逻辑
        grid[i][j] = 0
        t = self.DFS(grid, i+1, j)
        d = self.DFS(grid, i-1, j)
        l = self.DFS(grid, i, j+1)                   
        r = self.DFS(grid, i, j-1)
        return t + d + l + r + 1   # 岛屿面积 = 当前位置面积（1） + 上下左右位置面积（DFS）\

# BFS 队列实现
    def BFS(self, grid, i, j):
        que = [[i, j]]
        count = 0
        while que:
            [i, j] = que.pop()
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                que.extend([[i+1, j], [i-1, j], [i, j+1], [i, j-1]])
                count += 1
        return count