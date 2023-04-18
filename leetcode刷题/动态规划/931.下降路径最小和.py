# 题目：给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）

# 解法一：记忆化递归
class Solution:
    def __init__(self):
        self.memo = {}

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = float('inf')
    
        # 终点可能在最后一行的任意一列
        for j in range(n):
            res = min(res, self.dp(matrix, n - 1, j))
        return res

    def dp(self, matrix, i, j):
        # 非法case
        if i < 0 or j < 0 or j > len(matrix) - 1:
            return float('inf')

        # base case
        if i == 0:
            return matrix[0][j]
        # 缓存值复用
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        # 状态转移
        self.memo[(i, j)] = min(
            self.dp(matrix, i - 1, j - 1),
            self.dp(matrix, i - 1, j),
            self.dp(matrix, i - 1, j + 1)
        ) + matrix[i][j]
        return self.memo[(i, j)]
        
     
    