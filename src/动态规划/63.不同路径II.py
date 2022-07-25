# 题目：相比于62.不同路径，多了障碍物，障碍物不能通过
# 思路：和62大题一致，区别在于初始化和遍历过程，需要判断有误障碍物，有就跳过. 还有就是初始化化，有障碍物后面就为0

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 确定dp[i][j]及下标含义
        n = len(obstacleGrid)     # 行数
        m = len(obstacleGrid[0])  # 列数
        dp = [[0] * m for _ in range(n)]
        # dp初始化
        for i in range(n):
            # 遇到障碍区后面就不能赋值1了
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(m):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        # 确定遍历顺序
        for i in range(1, n):
            for j in range(1, m):
                # 遇到障碍物就跳过
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[n-1][m-1]