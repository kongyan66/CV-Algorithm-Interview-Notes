# 题目：给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 思路：让你在二维矩阵中求最优化问题（最大值或者最小值），肯定是动规问题

# 解法一：动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 1.确定dp数组含义 表示到达当前位置最小路径和
        dp = [[0] * n for _ in range(m)]
        # 2.初始化
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

# 解法二：暴力法 DFS(超时)
class Solution:
    def __init__(self):
        self.res = []
        self.sum_ = 0
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.DFS(grid, 0, 0)
        return min(self.res)
    
    def DFS(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        # 越界停止条件
        if i > m - 1 or j > n - 1:
            return 
        # 先保存当前路径，不然最后的位置就丢了
        self.sum_ += grid[i][j]
        if i == m - 1 and j == n - 1:
            self.res.append(self.sum_)
    
        self.DFS(grid, i+1, j)
        self.DFS(grid, i, j+1)
        self.sum_ -= grid[i][j]  # 回溯

# dp函数的写法
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return self.DFS(grid, m - 1, n - 1)

    def DFS(self, grid, i, j):
        # base case
        if i == 0 and j == 0:
            return grid[0][0]
        # 如果索引出界，返回一个很大的值，证在取 min 的时候不会被取到
        if i < 0 or j < 0:
            return float('inf')

        return min(self.DFS(grid, i - 1, j), self.DFS(grid, i, j - 1)) + grid[i][j]

# 解法三：记忆化递归（递归+备忘录）
class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return self.DFS(grid, m - 1, n - 1)

    def DFS(self, grid, i, j):
        # base case
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        self.memo[(i, j)] = min(self.DFS(grid, i - 1, j), self.DFS(grid, i, j - 1)) + grid[i][j]
        return self.memo[(i, j)]
        

        